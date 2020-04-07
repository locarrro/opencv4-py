import numpy as np
import cv2 as cv

# cap = cv.VideoCapture('data/vtest.avi')
cap = cv.VideoCapture('/home/lo/Videos/bilibili/asakix264.mp4')

"""
    创建一个 VideoWriter 对象。
    我们应该指定输出文件名(例如: output.avi)。
    然后我们应该指定 FourCC 代码(详见下一段)。
    然后传递帧率的数量和帧大小。最后一个是颜色标志。
    如果为 True，编码器期望颜色帧，否则它与灰度帧一起工作。
"""
fourcc = cv.VideoWriter_fourcc(*'x265')
out = cv.VideoWriter('build/asaki.mp4', fourcc, 20.0, (640,  480))

while cap.isOpened():
    ret, frame = cap.read()
    # 如果正确读取帧，ret为True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    out.write(frame)

    # cv.imshow('frame', frame)       # 彩色输出
    # if cv.waitKey(10) == ord('q'):  # cv.waitKey( )
    #     break
cap.release()
out.release()
cv.destroyAllWindows()

