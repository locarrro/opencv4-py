import numpy as np
import cv2 as cv

# cap = cv.VideoCapture('data/vtest.avi')
cap = cv.VideoCapture('/home/lo/Videos/bilibili/asakix264.mp4')
fps = cap.get(cv.CAP_PROP_FPS)
width = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))
print(fps, width, height)
"""
    创建一个 VideoWriter 对象。
    我们应该指定输出文件名(例如: output.avi)。
    然后我们应该指定 FourCC 代码(详见下一段)。
    然后传递帧率的数量和帧大小。最后一个是颜色标志。
    如果为 True，编码器期望颜色帧，否则它与灰度帧一起工作。
"""
fourcc = cv.VideoWriter_fourcc(*'avc1')     # x254不支持，会默认转成 avc1, 不支持 hevc/x265
out = cv.VideoWriter('build/asaki.mp4', fourcc, fps, (width, height))

ret, frame = cap.read()
while cap.isOpened():
    ret, frame = cap.read()
    # 如果正确读取帧，ret为True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    # cv.imshow('frame', frame)       # 彩色输出
    cv.waitKey(int(1000/fps))  # cv.waitKey( )
    out.write(frame)

cap.release()
out.release()
cv.destroyAllWindows()

