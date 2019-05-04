#!/usr/bin/python
# -*- coding: UTF-8 -*-
import cv2  
import numpy as np  
import matplotlib.pyplot as plt
 
# 读取图片
src1 = cv2.imread('L.jpg')
src2 = cv2.imread('_L.bmp')

# 图像融合
result = cv2.addWeighted(src1, 1, src2, 1, 0)

# 显示图像
cv2.imshow("src1", src1)
cv2.imshow("src2", src2)
cv2.imshow("result", result)

# 等待显示
cv2.waitKey(0)
cv2.destroyAllWindows()