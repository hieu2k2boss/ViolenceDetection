import cv2
import numpy as np
from keras.layers import *
from keras.models import Sequential
from keras.applications.mobilenet_v2 import MobileNetV2
from ultralytics import YOLO

input_video_file_path = "Video_Test/Video4.mp4"
pathModelYolo = 'model/yolov8n.pt'
PathModel = "model/violence_mobile_net.h5"
CLASSES_LIST = ["NonViolence","Violence"]
IMAGE_HEIGHT , IMAGE_WIDTH = 64, 64
SEQUENCE_LENGTH = 16


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

def predict_video(video_file_path, SEQUENCE_LENGTH):

    video_reader = cv2.VideoCapture(video_file_path)
    frames_list = []
    predicted_class_name = ''
    count = 0 
    text = ""
    
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 1
    font_color = (0, 255, 0)  # Màu trắng
    thickness = 2
    x, y = 50, 50  # Vị trí để viết chữ
    # Iterating the number of times equal to the fixed length of sequence.
    while True:
        success, frame = video_reader.read() 
        results = model_yolo.track(frame,conf=0.6, classes=0, persist=True)
        annotated_frame = results[0].plot()
        
        if not success:
            break
        # Resize the Frame to fixed Dimensions.
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
        cv2.imshow("Camera",annotated_frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break 
    video_reader.release()

if __name__=="__main__": 
    MoBiLSTM_model = create_model()
    MoBiLSTM_model.load_weights(PathModel)   
    # Perform Single Prediction on the Test Video.
    predict_video(input_video_file_path, SEQUENCE_LENGTH)