import numpy as np
from cv2 import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('data/messi5.jpg')

plt.imshow(img, cmap='gray', interpolation='bicubic')
plt.xticks([]), plt.yticks([])  # 隐藏 x 轴和 y 轴上的刻度值
plt.show()


"""
    OpenCV加载的彩色图像处于BGR模式。但是Matplotlib以RGB模式显示。
    因此，如果使用OpenCV读取彩色图像，则Matplotlib中将无法正确显示彩色图像。
    参考 http://stackoverflow.com/a/15074748/1134940
    method 1 : 
        cv.cvtColor(img, cv.COLOR_BGR2RGB)
    method 2 : 
        b,g,r = cv2.split(img)
        img2 = cv2.merge([r,g,b])
    method 3 : 
        img2 = img[:,:,::-1] # [::-1] 顺序相反操作 [B,G,R] -> [R,G,B]
"""


# img2 = cv.cvtColor(img, cv.COLOR_BGR2RGB)
# img2 = img[:,:,::-1]

b, g, r = cv.split(img)
img2 = cv.merge([r, g, b])

plt.subplot(121); plt.imshow(img)
plt.subplot(122); plt.imshow(img2)
plt.xticks([]), plt.yticks([])  # 隐藏 x 轴和 y 轴上的刻度值
plt.show()
