import numpy as np
from cv2 import cv2 as cv

"""
    cv.IMREAD_COLOR： 加载彩色图像。任何图像的透明度都会被忽视。它是默认标志。
    cv.IMREAD_GRAYSCALE：以灰度模式加载图像
    cv.IMREAD_UNCHANGED：加载图像，包括alpha通道
    注意 除了这三个标志，你可以分别简单地传递整数1、0或-1。
"""
# 加载彩色灰度图像
img = cv.imread('data/messi5.jpg')
cv.imshow('image', img)
cv.waitKey(0)
cv.destroyAllWindows()
"""
    注意 在特殊情况下，你可以创建一个空窗口，然后再将图像加载到该窗口。
    在这种情况下，你可以指定窗口是否可调整大小。
    这是通过功能cv.namedWindow()完成的。
    默认情况下，该标志为cv.WINDOW_AUTOSIZE。
    但是，如果将标志指定为cv.WINDOW_NORMAL，则可以调整窗口大小。
    当图像尺寸过大以及向窗口添加跟踪栏时，这将很有帮助。
"""
# cv.namedWindow('messi5', cv.WINDOW_AUTOSIZE)
# cv.imshow('messi5', img)
# cv.waitKey(0)
# cv.destroyAllWindows()
"""
    OpenCV加载的彩色图像处于BGR模式。
    cv.cvtColor() 转成 rgb 显示会出现颜色错误
"""
img2 = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.namedWindow('cvtColor', cv.WINDOW_AUTOSIZE)
cv.imshow('cvtColor', img2)
cv.waitKey(0)
cv.destroyAllWindows()