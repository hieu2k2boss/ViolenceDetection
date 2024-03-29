import tensorflow as tf
import numpy as np
import cv2
from ultralytics import YOLO
import time


model_yolo = YOLO('model/YOLOv8n.pt')
camera = "Video_Test/Video8.avi"
path_model = "model/my_model.h5"


start_time = time.time()
frames_processed = 0
FRAMES_PER_VIDEO = 50
VIDEO_HEIGHT = 100
VIDEO_WIDTH = 100
N_CHANNELS = 3

def Model_Violence_detection(FRAMES_PER_VIDEO,VIDEO_HEIGHT, VIDEO_WIDTH, N_CHANNELS):

    inputs = tf.keras.layers.Input(shape=(FRAMES_PER_VIDEO, VIDEO_HEIGHT, VIDEO_WIDTH, N_CHANNELS))

    x = tf.keras.layers.ConvLSTM2D(filters=32, kernel_size=(3, 3), return_sequences=False, data_format='channels_last', activation='tanh')(inputs)

    x = tf.keras.layers.DepthwiseConv2D(kernel_size=(3, 3), depth_multiplier=2, activation='relu', data_format='channels_last')(x)

    x = tf.keras.layers.GlobalAveragePooling2D(data_format='channels_last')(x)

    x = tf.keras.layers.Dense(units=128, activation='relu')(x)
    x = tf.keras.layers.Dense(units=16, activation='relu')(x)
    outputs = tf.keras.layers.Dense(units=1, activation='sigmoid')(x)

    model = tf.keras.Model(inputs, outputs)
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

    model.summary()
    return model

model =  Model_Violence_detection(FRAMES_PER_VIDEO,VIDEO_HEIGHT, VIDEO_WIDTH, N_CHANNELS)

# Load weights
model.load_weights(path_model)

# Khởi tạo video capture từ webcam
cap = cv2.VideoCapture(camera)

index = 0
i = 0
frames = []
text = None

while True:
    ret, frame = cap.read()
    image = frame
    if not ret:
        break

    results = model_yolo.track(frame,conf=0.6, classes=0, tracker="bytetrack.yaml", persist=True)
    annotated_frame = results[0].plot()    

    # Resize frame to match model's input size
    frame = cv2.resize(frame, (VIDEO_WIDTH, VIDEO_HEIGHT)).astype(np.float32)
    image = cv2.resize(image, (600, 500))


    if index < FRAMES_PER_VIDEO:
        frames.append(frame)
        index += 1
    else:
        a = np.array(frames)
        print("Hơn 50")
        print(a.shape)
        text=str(model.predict(np.expand_dims(a, axis=0)))  # Add an extra dimension for batch
        index = 0
        i = 0
        frames = []  

    # Viết chữ lên hình ảnh
    
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 1
    font_color = (255, 255, 255)  # Màu trắng
    thickness = 2
    x, y = 50, 50  # Vị trí để viết chữ
    cv2.putText(annotated_frame, text, (x, y), font, font_scale, font_color, thickness)

    frames_processed += 1
    elapsed_time = time.time() - start_time
    fps = frames_processed / elapsed_time
    text_fps = "FPS: {:.2f}".format(fps)
    cv2.putText(annotated_frame, text_fps, (10, 30), font, font_scale, font_color, thickness)

    cv2.imshow("Video", annotated_frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
