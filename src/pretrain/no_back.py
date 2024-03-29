import tensorflow as tf
import numpy as np
import cv2
from ultralytics import YOLO
import time

def No_back(path_video, path_model):
    model_yolo = YOLO(path_model)

    cap = cv2.VideoCapture(path_video)
    color_green = (0, 255, 0)
    color_red = (0, 0, 255)
    color_blue = (255, 0, 0)
    color_yellow = (0, 255, 255)

    thickness = 2

    while True:
        ret, frame = cap.read()
        results = model_yolo(frame, conf=0.6, classes=0)
        annotated_frame = results[0].plot()
        height, width, channels = frame.shape

        background = np.zeros((height, width, 3), dtype=np.uint8)
        keypoints = results[0].keypoints.xy.numpy().astype(int)
        frame = background
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
                image_with_line = cv2.line(
                    frame, (Mat_Trai_x, Mat_Trai_y), (Mui_x, Mui_y), color_green, thickness
                )
            if (Mat_Phai_x != 0) and (Mat_Phai_y != 0) and (Mui_x != 0) and (Mui_y != 0):
                image_with_line = cv2.line(
                    frame, (Mui_x, Mui_y), (Mat_Phai_x, Mat_Phai_y), color_green, thickness
                )

            if (
                (TrungDiemVai_x != 0)
                and (TrungDiemVai_y != 0)
                and (Mui_x != 0)
                and (Mui_y != 0)
            ):
                image_with_line = cv2.line(
                    frame,
                    (Mui_x, Mui_y),
                    (TrungDiemVai_x, TrungDiemVai_y),
                    color_red,
                    thickness,
                )

            if (
                (Vai_Phai_x != 0)
                and (Vai_Phai_y != 0)
                and (Vai_Trai_x != 0)
                and (Vai_Trai_y != 0)
            ):
                image_with_line = cv2.line(
                    frame,
                    (Vai_Phai_x, Vai_Phai_y),
                    (Vai_Trai_x, Vai_Trai_y),
                    color_blue,
                    thickness,
                )
            if (
                (Khuy_tay_Trai_x != 0)
                and (Khuy_tay_Trai_y != 0)
                and (Vai_Trai_x != 0)
                and (Vai_Trai_y != 0)
            ):
                image_with_line = cv2.line(
                    frame,
                    (Khuy_tay_Trai_x, Khuy_tay_Trai_y),
                    (Vai_Trai_x, Vai_Trai_y),
                    color_green,
                    thickness,
                )

            if (
                (Khuy_tay_Phai_x != 0)
                and (Khuy_tay_Phai_y != 0)
                and (Vai_Phai_x != 0)
                and (Vai_Phai_y != 0)
            ):
                image_with_line = cv2.line(
                    frame,
                    (Khuy_tay_Phai_x, Khuy_tay_Phai_y),
                    (Vai_Phai_x, Vai_Phai_y),
                    color_green,
                    thickness,
                )
            if (
                (Khuy_tay_Trai_x != 0)
                and (Khuy_tay_Trai_y != 0)
                and (Ban_tay_Trai_x != 0)
                and (Ban_tay_Trai_y != 0)
            ):
                image_with_line = cv2.line(
                    frame,
                    (Khuy_tay_Trai_x, Khuy_tay_Trai_y),
                    (Ban_tay_Trai_x, Ban_tay_Trai_y),
                    color_yellow,
                    thickness,
                )

            if (
                (Khuy_tay_Phai_x != 0)
                and (Khuy_tay_Phai_y != 0)
                and (Ban_tay_Phai_x != 0)
                and (Ban_tay_Phai_y != 0)
            ):
                image_with_line = cv2.line(
                    frame,
                    (Khuy_tay_Phai_x, Khuy_tay_Phai_y),
                    (Ban_tay_Phai_x, Ban_tay_Phai_y),
                    color_yellow,
                    thickness,
                )
            if (
                (Hong_Trai_x != 0)
                and (Hong_Trai_y != 0)
                and (Hong_Phai_x != 0)
                and (Hong_Phai_y != 0)
            ):
                image_with_line = cv2.line(
                    frame,
                    (Hong_Trai_x, Hong_Trai_y),
                    (Hong_Phai_x, Hong_Phai_y),
                    color_blue,
                    thickness,
                )
            if (
                (TrungDiemVai_x != 0)
                and (TrungDiemVai_y != 0)
                and (TrungDiemHong_x != 0)
                and (TrungDiemHong_y != 0)
            ):
                image_with_line = cv2.line(
                    frame,
                    (TrungDiemVai_x, TrungDiemVai_y),
                    (TrungDiemHong_x, TrungDiemHong_y),
                    color_red,
                    thickness,
                )
            if (
                (Hong_Trai_x != 0)
                and (Hong_Trai_y != 0)
                and (DauGoi_Trai_x != 0)
                and (DauGoi_Trai_y != 0)
            ):
                image_with_line = cv2.line(
                    frame,
                    (Hong_Trai_x, Hong_Trai_y),
                    (DauGoi_Trai_x, DauGoi_Trai_y),
                    color_green,
                    thickness,
                )
            if (
                (DauGoi_Phai_x != 0)
                and (DauGoi_Phai_y != 0)
                and (Hong_Phai_x != 0)
                and (Hong_Phai_y != 0)
            ):
                image_with_line = cv2.line(
                    frame,
                    (DauGoi_Phai_x, DauGoi_Phai_y),
                    (Hong_Phai_x, Hong_Phai_y),
                    color_green,
                    thickness,
                )
            if (
                (BanChan_Trai_x != 0)
                and (DauGoi_Trai_x != 0)
                and (BanChan_Trai_y != 0)
                and (DauGoi_Trai_y != 0)
            ):
                image_with_line = cv2.line(
                    frame,
                    (BanChan_Trai_x, BanChan_Trai_y),
                    (DauGoi_Trai_x, DauGoi_Trai_y),
                    color_yellow,
                    thickness,
                )
            if (
                (BanChan_Phai_x != 0)
                and (BanChan_Phai_y != 0)
                and (DauGoi_Phai_x != 0)
                and (DauGoi_Phai_y != 0)
            ):
                image_with_line = cv2.line(
                    frame,
                    (BanChan_Phai_x, BanChan_Phai_y),
                    (DauGoi_Phai_x, DauGoi_Phai_y),
                    color_yellow,
                    thickness,
                )

        cv2.imshow("Video", frame)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    cap.release()
