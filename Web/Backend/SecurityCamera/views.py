from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
import cv2
import numpy as np
from django.http import StreamingHttpResponse
from keras.layers import *
from keras.models import Sequential
from keras.applications.mobilenet_v2 import MobileNetV2
from ultralytics import YOLO
import requests
from datetime import datetime

input_video_file_path = ""
pathModelYolo = 'H:/DaiHoc/DoAn/Code/ViolenceDetection/model/yolov8n.pt'
PathModel = "H:/DaiHoc/DoAn/Code/ViolenceDetection/model/violence_mobile_net.h5"
CLASSES_LIST = ["NonViolence","Violence"]
IMAGE_HEIGHT , IMAGE_WIDTH = 64, 64
SEQUENCE_LENGTH = 16
number = 0

model_yolo = YOLO(pathModelYolo)
# mobilenet
mobilenet = MobileNetV2(include_top=False , weights="imagenet")
mobilenet.trainable=True
for layer in mobilenet.layers[:-40]:
  layer.trainable=False
mobilenet.summary()

def create_model():

    model = Sequential()

  
    #Specifying Input to match features shape
    model.add(Input(shape = (SEQUENCE_LENGTH, IMAGE_HEIGHT, IMAGE_WIDTH, 3)))
    
    # Passing mobilenet in the TimeDistributed layer to handle the sequence
    model.add(TimeDistributed(mobilenet))
    
    model.add(Dropout(0.25))
    model.add(TimeDistributed(Flatten()))
    
    lstm_fw = LSTM(units=32)
    lstm_bw = LSTM(units=32, go_backwards = True)  

    model.add(Bidirectional(lstm_fw, backward_layer = lstm_bw))
    
    model.add(Dropout(0.25))

    model.add(Dense(256,activation='relu'))
    model.add(Dropout(0.25))

    model.add(Dense(128,activation='relu'))
    model.add(Dropout(0.25))

    model.add(Dense(64,activation='relu'))
    model.add(Dropout(0.25))
    
    model.add(Dense(32,activation='relu'))
    model.add(Dropout(0.25))
    
    
    model.add(Dense(2, activation = 'softmax'))
 
    
    model.summary()
    
    return model

MoBiLSTM_model = create_model()
MoBiLSTM_model.load_weights(PathModel) 

# Đọc API 
def fetch_data_from_api(api_url):
    try:
        response = requests.get(api_url)
        if response.status_code == 200:
            return response.json()
        else:
            print("Error:", response.status_code)
            return None
    except requests.exceptions.RequestException as e:
        print("Error:", e)
        return None

def ReadCamera():
    api_url = "http://127.0.0.1:8000/MyAPI/"
    
    data = fetch_data_from_api(api_url)
    if data:
        if (data[0]['path_video'] =="0"):
            return 0
        else:
            return data[0]['path_video']

def webcam_feed(request):
    input_video_file_path = ReadCamera()
    print(input_video_file_path)
    cap = cv2.VideoCapture(input_video_file_path)
    def generate_frames():      
        frames_list = []
        predicted_class_name = ''
        count = 0 
        text = ""
        font = cv2.FONT_HERSHEY_SIMPLEX
        font_scale = 2
        font_color = (0, 255, 0)  # Màu trắng
        thickness = 2
        x, y = 50, 50  # Vị trí để viết chữ
        while True:
            ret, frame = cap.read()
            results = model_yolo.track(frame,conf=0.6, classes=0, persist=True)
            annotated_frame = results[0].plot()
            #print (len(results[0].boxes.data.numpy()))
            number = len(results[0].boxes.data.numpy())
            
            if number >0:
                now = datetime.now()
                current_hour = now.hour
                current_minute = now.minute
                data = {
                        "id": 1,
                        "NumberPeople": number,
                        "Date": "2024-04-01"
                    }
                url = "http://127.0.0.1:8000/Result/"
                response = requests.put(url, data=data)
                # Kiểm tra mã trạng thái của response
                if response.status_code == 200:
                    print("PUT request đã được thực hiện thành công.")
                else:
                    print("Có lỗi xảy ra khi thực hiện PUT request.")
                    
            if not ret:
                break
            resized_frame = cv2.resize(frame, (IMAGE_HEIGHT, IMAGE_WIDTH))
            if count < SEQUENCE_LENGTH:
            # Normalize the resized frame.
                normalized_frame = resized_frame / 255
                # Appending the pre-processed frame into the frames list
                frames_list.append(normalized_frame)
                count +=1
            else:
                # Passing the  pre-processed frames to the model and get the predicted probabilities.
                predicted_labels_probabilities = MoBiLSTM_model.predict(np.expand_dims(frames_list, axis = 0))[0]
                count = 0
                frames_list = []
                predicted_label = np.argmax(predicted_labels_probabilities)
                predicted_class_name = CLASSES_LIST[predicted_label]
                print(f'Predicted: {predicted_class_name}\nConfidence: {predicted_labels_probabilities[predicted_label]}')
                text = predicted_class_name
            cv2.putText(annotated_frame, text, (x, y), font, font_scale, font_color, thickness)    
            #cv2.imshow("Camera",annotated_frame)
            frame = annotated_frame
            _, jpeg = cv2.imencode('.jpg', frame)
            frame_bytes = jpeg.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n\r\n')
    return StreamingHttpResponse(generate_frames(), content_type='multipart/x-mixed-replace; boundary=frame')

def ProcessVideo(request):

    if request.method == 'POST' and request.FILES['video']:
        video_file = request.FILES['video']
        video_data = video_file.read()
        nparr = np.frombuffer(video_data, np.uint8)
        cap = cv2.VideoCapture()
        cap.open(''.join(chr(i) for i in nparr))
        
        # Lặp qua các khung hình của video
        while True:
            ret, frame = cap.read()
            if not ret:
                break

            cv2.imshow('Processed Video', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        
        # Giải phóng tài nguyên
        cap.release()
        cv2.destroyAllWindows()
        
        return JsonResponse({'success': True})
    return render(request, 'hello.html' ,{'number': number})


