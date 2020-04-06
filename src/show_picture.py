import numpy as np
from cv2 import cv2 as cv

# 加载彩色灰度图像
img = cv.imread('data/messi5.jpg', 0)
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
cv.namedWindow('messi5', cv.WINDOW_AUTOSIZE)
cv.imshow('messi5', img)
cv.waitKey(0)
cv.destroyAllWindows()