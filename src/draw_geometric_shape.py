# -*- coding: utf-8 -*-
# !/usr/bin/env python

import numpy as np
from cv2 import cv2 as cv

# 创建黑色的图像
img = np.zeros((512, 512, 3), np.uint8)
# 绘制一条厚度为5的蓝色对角线
cv.line(img, (0, 0), (511, 511), (255, 0, 0), 5)
cv.imshow("geometric", img)
cv.waitKey(0)
cv.destroyAllWindows()

# 创建黑色的图像
circle = np.zeros((512, 512, 3), np.uint8)
# 绘制 圆
cv.circle(circle, (447, 63), 63, (0, 0, 255), -1)
cv.imshow("circle", circle)
cv.waitKey(0)
cv.destroyAllWindows()

# 创建黑色的图像
ellipse = np.zeros((512, 512, 3), np.uint8)
# 绘制 椭圆
cv.ellipse(ellipse, (256, 256), (100, 50), 0, 0, 180, 255, -1)
cv.imshow("ellipse", ellipse)
cv.waitKey(0)
cv.destroyAllWindows()
