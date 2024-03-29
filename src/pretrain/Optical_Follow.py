import cv2
import numpy as np
import os



#Path_Save="data/Optical_follow/train/Fight"
#folder_path ="RWF_2000Dataset\\train\\Fight"

#Path_Save="data/Optical_follow/train/NonFight"
#folder_path ="RWF_2000Dataset\\train\\NonFight"

#Path_Save="data/Optical_follow/val/NonFight"
#folder_path ="RWF_2000Dataset\\val\\NonFight"

Path_Save="data/Optical_follow/val/Fight"
folder_path ="RWF_2000Dataset\\val\\Fight"

def Optical_Follow(Path_Video, id):

    # Đọc video từ file
    cap = cv2.VideoCapture(Path_Video)
    video_path = Path_Video


    # Định nghĩa màu của các vector Optical Flow
    color = (0, 255, 0)

    # Đọc frame đầu tiên
    ret, frame1 = cap.read()

    # Chuyển sang không gian màu xám
    prvs_gray = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)

    # Tạo một bức hình trắng có cùng kích thước với frame đầu tiên để vẽ các vector Optical Flow
    mask = np.zeros_like(frame1)

    Fps = cap.get(cv2.CAP_PROP_FPS)
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    path_save =  Path_Save+"/"+id+'output_No_Back.avi'
    print(path_save)
    
    out = cv2.VideoWriter( path_save, fourcc, Fps, (int(cap.get(3)), int(cap.get(4))))
    while True:
        # Đọc frame tiếp theo
        ret, frame2 = cap.read()
        if not ret:
            break
        
        # Chuyển sang không gian màu xám
        next_gray = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)

        # Tính toán Optical Flow bằng phương pháp Farneback
        flow = cv2.calcOpticalFlowFarneback(prvs_gray, next_gray, None, 0.5, 3, 15, 3, 5, 1.2, 0)

        # Trực quan hóa kết quả Optical Flow bằng cách vẽ các vector trên frame
        magnitude, angle = cv2.cartToPolar(flow[..., 0], flow[..., 1])
        mask[:, :, 0] = angle * 180 / np.pi / 2
        mask[:, :, 2] = cv2.normalize(magnitude, None, 0, 255, cv2.NORM_MINMAX)
        rgb = cv2.cvtColor(mask, cv2.COLOR_HSV2BGR)

        # Hiển thị frame với các vector Optical Flow
        #cv2.imshow('Optical Flow', rgb)
        out.write(rgb)
        # Chuyển frame hiện tại thành frame trước cho lần lặp tiếp theo
        prvs_gray = next_gray
        
        # Thoát khỏi vòng lặp khi nhấn phím 'q'
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

    # Giải phóng tài nguyên
    cap.release()
    out.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    a = 0
    for filename in os.listdir(folder_path):
        if filename.endswith('.mp4') or filename.endswith('.avi'):
            file_path = folder_path +"\\" +filename
            file_path = file_path.replace("\\", "/")
            Optical_Follow(file_path, str(a))
            a +=1
            