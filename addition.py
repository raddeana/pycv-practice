#!/usr/bin/python
# -*- coding: UTF-8 -*-
import cv2  
import numpy as np  
import matplotlib.pyplot as plt
 
# 读取图片
img = cv2.imread('L.bmp')
test = img

# Numpy加法运算
result1 = img + test

# OpenCV加法运算
result2 = cv2.add(img, test)

# 显示图像
cv2.imshow("original", img)
cv2.imshow("result1", result1)
cv2.imshow("result2", result2)

# 等待显示
cv2.waitKey(0)
cv2.destroyAllWindows()