import cv2
import numpy as np
import keras.backend as K
import os


def tf_frame_diff(video):
    return video[1:] - video[:-1]

def tf_frame_dist(video):
    video_diff = tf_frame_diff(video)
    return K.sqrt(K.sum(K.square(video_diff), axis=-1, keepdims=True))


#Path_Save="data/distant/train/Fight"
#folder_path ="RWF_2000Dataset\\train\\Fight"

#Path_Save="data/distant/train/NonFight"
#folder_path ="RWF_2000Dataset\\train\\NonFight"

#Path_Save="data/distant/val/NonFight"
#folder_path ="RWF_2000Dataset\\val\\NonFight"

Path_Save="data/distant/val/Fight"
folder_path ="RWF_2000Dataset\\val\\Fight"

def distant(Path_Video, id):

    # Đường dẫn đến video
    video_path = Path_Video

    # Mở video để đọc
    video_capture = cv2.VideoCapture(video_path)

    if not video_capture.isOpened():
        print("Không thể mở video")
        exit()
    Fps = video_capture.get(cv2.CAP_PROP_FPS)
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    path_save =  Path_Save+"/"+id+'output_No_Back.avi'
    print(path_save)
        
    out = cv2.VideoWriter( path_save, fourcc, Fps, (int(video_capture.get(3)), int(video_capture.get(4))))
    # Đọc hai khung hình đầu tiên
    success, frame1 = video_capture.read()
    success, frame2 = video_capture.read()
    
    # Chuyển đổi khung hình sang định dạng phù hợp cho việc tính toán
    frame1 = np.expand_dims(frame1, axis=0).astype('float32') / 255.0
    frame2 = np.expand_dims(frame2, axis=0).astype('float32') / 255.0

    # Duyệt qua các khung hình trong video và tính khoảng cách giữa hai khung hình liên tiếp
    while success:
        # Hiển thị hai khung hình

        # Tính toán khoảng cách giữa hai khung hình và hiển thị ảnh dựa trên khoảng cách
        video_diff = tf_frame_diff(np.concatenate([frame1, frame2]))
        frame_distance = tf_frame_dist(np.concatenate([frame1, frame2]))

        # Chuyển đổi tensor thành mảng numpy trước khi sử dụng hàm normalize
        frame_distance_np = K.eval(frame_distance)[0]
        distance_image = cv2.normalize(frame_distance_np, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)
        cv2.imshow('Frame Distance', distance_image)
        out.write(distance_image)
        # Chờ phím nhấn từ người dùng (nhấn 'q' để thoát)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

        # Đọc khung hình tiếp theo
        frame1 = frame2
        success, frame2 = video_capture.read()
        frame2 = np.expand_dims(frame2, axis=0).astype('float32') / 255.0
        
    # Giải phóng tài nguyên
    video_capture.release()
    out.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    a = 0
    for filename in os.listdir(folder_path):
        if filename.endswith('.mp4') or filename.endswith('.avi'):
            file_path = folder_path +"\\" +filename
            file_path = file_path.replace("\\", "/")
            distant(file_path, str(a))
            a +=1
            
