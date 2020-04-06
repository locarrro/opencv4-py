import numpy as np
from cv2 import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('data/messi5.jpg', 0)
"""
    OpenCV加载的彩色图像处于BGR模式。但是Matplotlib以RGB模式显示。
    因此，如果使用OpenCV读取彩色图像，则Matplotlib中将无法正确显示彩色图像。
    参考 http://stackoverflow.com/a/15074748/1134940
"""
plt.imshow(img, cmap='gray', interpolation='bicubic')
plt.xticks([]), plt.yticks([])  # 隐藏 x 轴和 y 轴上的刻度值
plt.show()
