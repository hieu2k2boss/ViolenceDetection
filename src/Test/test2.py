import tensorflow as tf
import numpy as np
import cv2
from ultralytics import YOLO
import time
import keras.backend as K

model_yolo = YOLO('model/yolov8n-pose.pt')
camera = "Video_Test/Video7.avi"
path_model = "model/Final_model_v1.h5"

font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 1
font_color = (0, 0, 255)  # Màu trắng
thickness = 2
x, y = 50, 50  # Vị trí để viết chữ

start_time = time.time()
frames_processed = 0
FRAMES_PER_VIDEO = 50 +1
VIDEO_HEIGHT = 100
VIDEO_WIDTH = 100
N_CHANNELS = 3
FRAME_FUNC = 'frame_diff'
# To use frame diff to weight t (current) or t+1
WEIGHT_CURRENT = True
thickness = 2
color_green = (0, 255, 0)
color_red = (0, 0, 255)
color_blue = (255, 0, 0)
color_yellow = (0, 255, 255)

index = 0
i = 0
frames_noBack = []
frames_Rgb = []
text = None
framesImage = [] 

def tf_frame_diff(video):
    return video[1:] - video[:-1]

def tf_frame_dist(video):
    video_diff = tf_frame_diff(video)
    return K.sqrt(K.sum(K.square(video_diff), axis=-1, keepdims=True))

if WEIGHT_CURRENT:
    def tf_frame_diff_dist_combined(video):
        video_diff = tf_frame_diff(video)
        video_diff_current = tf.nn.relu(-video_diff)
        video_diff_next = tf.nn.relu(video_diff)
        video_diff_next_norm = K.sqrt(K.sum(K.square(video_diff_next), axis=-1, keepdims=True))
        return K.concatenate([video_diff_current, video_diff_next_norm])
else:
    def tf_frame_diff_dist_combined(video):
        video_diff = tf_frame_diff(video)
        video_diff_current = tf.nn.relu(video_diff)
        video_diff_prev = tf.nn.relu(-video_diff)
        video_diff_prev_norm = K.sqrt(K.sum(K.square(video_diff_prev), axis=-1, keepdims=True))
        return K.concatenate([video_diff_current, video_diff_prev_norm])

frame_func_dict = {'frame_diff': tf_frame_diff, 'frame_dist': tf_frame_dist, 'frame_diff_dist_combined': tf_frame_diff_dist_combined}
frame_func = frame_func_dict[FRAME_FUNC]

def Model_Violence_detection(FRAMES_PER_VIDEO,VIDEO_HEIGHT, VIDEO_WIDTH, N_CHANNELS):

    inputs_raw = tf.keras.layers.Input(shape=(FRAMES_PER_VIDEO, VIDEO_HEIGHT, VIDEO_WIDTH, N_CHANNELS))
    inputs_openpose = tf.keras.layers.Input(shape=(FRAMES_PER_VIDEO, VIDEO_HEIGHT, VIDEO_WIDTH, N_CHANNELS))

    inputs_diff = tf.keras.layers.Lambda(lambda video: tf.map_fn(frame_func, video))(inputs_raw)
    inputs_to_weight = inputs_openpose[:, :-1] if WEIGHT_CURRENT else inputs_openpose[:, 1:]

    inputs_diff_norm = tf.keras.layers.BatchNormalization()(inputs_diff)
    inputs_diff_time_info_weight = tf.keras.layers.ConvLSTM2D(filters=9, kernel_size=(3, 3), return_sequences=True, data_format='channels_last', activation='tanh')(inputs_diff_norm)

    convolutional_layer = tf.keras.layers.Conv2D(filters=9, kernel_size=(3,3), activation='relu')
    inputs_openpose_soft = tf.keras.layers.TimeDistributed(convolutional_layer)(inputs_to_weight)

    inputs_openpose_norm = tf.keras.layers.BatchNormalization(scale=False, center=False)(inputs_openpose_soft)

    inputs_weighted = tf.keras.layers.Add()([inputs_openpose_norm, inputs_diff_time_info_weight])

    x = tf.keras.layers.ConvLSTM2D(filters=32, kernel_size=(3, 3), return_sequences=False, data_format='channels_last', activation='tanh')(inputs_weighted)

    x = tf.keras.layers.DepthwiseConv2D(kernel_size=(3, 3), depth_multiplier=2, activation='relu', data_format='channels_last')(x)

    x = tf.keras.layers.GlobalAveragePooling2D(data_format='channels_last')(x)

    x = tf.keras.layers.Dense(units=128, activation='relu')(x)
    x = tf.keras.layers.Dense(units=16, activation='relu')(x)
    outputs = tf.keras.layers.Dense(units=1, activation='sigmoid')(x)

    model = tf.keras.Model([inputs_raw, inputs_openpose], outputs)
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

    model.summary()
    return model

model =  Model_Violence_detection(FRAMES_PER_VIDEO,VIDEO_HEIGHT, VIDEO_WIDTH, N_CHANNELS)

# Load weights
model.load_weights(path_model)
text = None

if __name__ == "__main__":
    cap = cv2.VideoCapture(camera)
    while True:
        ret, frame = cap.read() 
        
        #frame = frame.astype(np.float32) / 255.0
        #gamma = 2
        #corrected_image = np.power(frame, gamma)
        #frame = (corrected_image * 255).astype(np.uint8)
        
        image = frame
        frame = cv2.resize(frame, (VIDEO_WIDTH, VIDEO_HEIGHT)).astype(np.float32)   
        frame_Rgb = frame 
        results = model_yolo(frame, conf=0.6, classes=0)
        height, width, channels = frame.shape
        
        background = np.zeros((height, width, 3), dtype=np.uint8)
        keypoints = results[0].keypoints.xy.numpy().astype(int)
        frame = background
       
        if  not keypoints.any():
            print("No detect")
        else:
        # Vẽ các điểm keypoint
            for i in range(0, len(keypoints)):

                Mat_Trai_x, Mat_Trai_y = keypoints[i][1]
                Mat_Phai_x, Mat_Phai_y = keypoints[i][2]
                Mui_x, Mui_y = keypoints[i][0]

                Vai_Trai_x, Vai_Trai_y = keypoints[i][5]
                Vai_Phai_x, Vai_Phai_y = keypoints[i][6]

                Khuy_tay_Trai_x, Khuy_tay_Trai_y = keypoints[i][7]
                Khuy_tay_Phai_x, Khuy_tay_Phai_y = keypoints[i][8]

                Ban_tay_Trai_x, Ban_tay_Trai_y = keypoints[i][9]
                Ban_tay_Phai_x, Ban_tay_Phai_y = keypoints[i][10]

                Hong_Trai_x, Hong_Trai_y = keypoints[i][11]
                Hong_Phai_x, Hong_Phai_y = keypoints[i][12]

                DauGoi_Trai_x, DauGoi_Trai_y = keypoints[i][13]
                DauGoi_Phai_x, DauGoi_Phai_y = keypoints[i][14]

                BanChan_Trai_x, BanChan_Trai_y = keypoints[i][15]
                BanChan_Phai_x, BanChan_Phai_y = keypoints[i][16]

                TrungDiemVai_x, TrungDiemVai_y = 0, 0
                TrungDiemHong_x, TrungDiemHong_y = 0, 0

                if Vai_Trai_x > Vai_Phai_x:
                    TrungDiemVai_x = int((Vai_Trai_x - Vai_Phai_x) / 2 + Vai_Phai_x)
                else:
                    TrungDiemVai_x = int((Vai_Phai_x - Vai_Trai_x) / 2 + Vai_Trai_x)

                if Vai_Trai_y > Vai_Phai_y:
                    TrungDiemVai_y = int((Vai_Trai_y - Vai_Phai_y) / 2 + Vai_Phai_y)
                else:
                    TrungDiemVai_y = int((Vai_Phai_y - Vai_Trai_y) / 2 + Vai_Trai_y)
                ### Hong
                if Hong_Trai_x > Hong_Phai_x:
                    TrungDiemHong_x = int((Hong_Trai_x - Hong_Phai_x) / 2 + Hong_Phai_x)
                else:
                    TrungDiemHong_x = int((Hong_Phai_x - Hong_Trai_x) / 2 + Hong_Trai_x)

                if Hong_Trai_y > Hong_Phai_y:
                    TrungDiemHong_y = int((Hong_Trai_y - Hong_Phai_y) / 2 + Hong_Phai_y)
                else:
                    TrungDiemHong_y = int((Hong_Phai_y - Hong_Trai_y) / 2 + Hong_Trai_y)

                # print( (Mat_Trai_x,Mat_Trai_y))

                if (Mat_Trai_x != 0) and (Mat_Trai_y != 0) and (Mui_x != 0) and (Mui_y != 0):
                    image_with_line = cv2.line(frame, (Mat_Trai_x, Mat_Trai_y), (Mui_x, Mui_y), color_green, thickness)
                if (Mat_Phai_x != 0) and (Mat_Phai_y != 0) and (Mui_x != 0) and (Mui_y != 0):
                    image_with_line = cv2.line(frame, (Mui_x, Mui_y), (Mat_Phai_x, Mat_Phai_y), color_green, thickness)

                if ((TrungDiemVai_x != 0) and (TrungDiemVai_y != 0) and (Mui_x != 0) and (Mui_y != 0)):
                    image_with_line = cv2.line(frame,(Mui_x, Mui_y),(TrungDiemVai_x, TrungDiemVai_y),color_red,thickness,)

                if ((Vai_Phai_x != 0)and (Vai_Phai_y != 0)and (Vai_Trai_x != 0)and (Vai_Trai_y != 0)):
                    image_with_line = cv2.line(frame,(Vai_Phai_x, Vai_Phai_y),(Vai_Trai_x, Vai_Trai_y),color_blue,thickness,)
                if ((Khuy_tay_Trai_x != 0)and (Khuy_tay_Trai_y != 0)and (Vai_Trai_x != 0)and (Vai_Trai_y != 0)):
                    image_with_line = cv2.line(frame,(Khuy_tay_Trai_x, Khuy_tay_Trai_y),(Vai_Trai_x, Vai_Trai_y),color_green,thickness,)

                if ((Khuy_tay_Phai_x != 0) and (Khuy_tay_Phai_y != 0)  and (Vai_Phai_x != 0) and (Vai_Phai_y != 0) ):
                    image_with_line = cv2.line(frame,  (Khuy_tay_Phai_x, Khuy_tay_Phai_y),  (Vai_Phai_x, Vai_Phai_y), color_green, thickness,)
                if ( (Khuy_tay_Trai_x != 0)and (Khuy_tay_Trai_y != 0)and (Ban_tay_Trai_x != 0) and (Ban_tay_Trai_y != 0) ):
                    image_with_line = cv2.line( frame,   (Khuy_tay_Trai_x, Khuy_tay_Trai_y), (Ban_tay_Trai_x, Ban_tay_Trai_y),color_yellow, thickness, )

                if ((Khuy_tay_Phai_x != 0)  and (Khuy_tay_Phai_y != 0)  and (Ban_tay_Phai_x != 0) and (Ban_tay_Phai_y != 0) ):
                    image_with_line = cv2.line( frame, (Khuy_tay_Phai_x, Khuy_tay_Phai_y),  (Ban_tay_Phai_x, Ban_tay_Phai_y),  color_yellow,  thickness,  )
                if ((Hong_Trai_x != 0) and (Hong_Trai_y != 0)and (Hong_Phai_x != 0) and (Hong_Phai_y != 0) ):
                    image_with_line = cv2.line( frame, (Hong_Trai_x, Hong_Trai_y),(Hong_Phai_x, Hong_Phai_y), color_blue,thickness, )
                if ( (TrungDiemVai_x != 0) and (TrungDiemVai_y != 0)  and (TrungDiemHong_x != 0)and (TrungDiemHong_y != 0)):
                    image_with_line = cv2.line( frame,  (TrungDiemVai_x, TrungDiemVai_y),  (TrungDiemHong_x, TrungDiemHong_y), color_red,thickness,)
                if (  (Hong_Trai_x != 0)  and (Hong_Trai_y != 0)  and (DauGoi_Trai_x != 0) and (DauGoi_Trai_y != 0)  ):
                    image_with_line = cv2.line( frame,  (Hong_Trai_x, Hong_Trai_y),  (DauGoi_Trai_x, DauGoi_Trai_y),  color_green, thickness, )
                if ((DauGoi_Phai_x != 0) and (DauGoi_Phai_y != 0)  and (Hong_Phai_x != 0) and (Hong_Phai_y != 0) ):
                    image_with_line = cv2.line( frame,(DauGoi_Phai_x, DauGoi_Phai_y), (Hong_Phai_x, Hong_Phai_y),  color_green,  thickness, )
                if ( (BanChan_Trai_x != 0)and (DauGoi_Trai_x != 0)and (BanChan_Trai_y != 0)and (DauGoi_Trai_y != 0)):
                    image_with_line = cv2.line(  frame,  (BanChan_Trai_x, BanChan_Trai_y),  (DauGoi_Trai_x, DauGoi_Trai_y),  color_yellow,  thickness, )
                if (  (BanChan_Phai_x != 0)  and (BanChan_Phai_y != 0)  and (DauGoi_Phai_x != 0)  and (DauGoi_Phai_y != 0) ):
                    image_with_line = cv2.line(  frame, (BanChan_Phai_x, BanChan_Phai_y), (DauGoi_Phai_x, DauGoi_Phai_y),  color_yellow,  thickness, )
        
        # Thêm các frame vào thành 1 vector 
        
        if index < FRAMES_PER_VIDEO:
            frames_Rgb.append(frame_Rgb)
            frames_noBack.append(frame)
            #framesImage = [frames_Rgb, frames_noBack]
            index += 1
            
        else:
            #a = np.concatenate((frames_Rgb, frames_noBack), axis=0)
            a = np.array(frames_Rgb)
            b = np.array(frames_noBack)
            
            c = np.expand_dims(a, axis=0)
            d = np.expand_dims(b, axis=0)
            

            print("Hơn 50")
            #print(a.shape)
            text=str(model.predict([c,d]))  # Add an extra dimension for batch
            #print(model.predict([c,d])) 
            
            index = 0
            i = 0
            frames_Rgb = []
            frames_noBack = [] 
            
        cv2.putText(image, text, (10, 30), font, font_scale, font_color, thickness)    
        cv2.imshow("Video", image)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    
    
    cap.release()