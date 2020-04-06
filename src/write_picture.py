import numpy as np
from cv2 import cv2 as cv

# 加载彩色灰度图像
img = cv.imread('data/messi5.jpg', 0)
cv.imshow('image',img)
k = cv.waitKey(0)
if k == 27:         # 等待ESC退出
    cv.destroyAllWindows()
elif k == ord('s'): # 等待关键字，保存和退出
    cv.imwrite('build/messigray.png',img)
    cv.destroyAllWindows()