import numpy as np
from cv2 import cv2 as cv

cap = cv.VideoCapture('data/vtest.avi')
while cap.isOpened():
    ret, frame = cap.read()
    # 如果正确读取帧，ret为True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    # gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    # cv.imshow('frame', gray)      #灰色输出

    color = cv.cvtColor(frame, cv.COLOR_BGR2RGB)  # 默认读取是 BGR, 默认输出也是BGR，不用转成 RGB
    # cv.imshow('frame', color)


    cv.imshow('frame', frame)       # 彩色输出
    if cv.waitKey(1) == ord('q'):  # cv.waitKey( )
        break
cap.release()
cv.destroyAllWindows()
