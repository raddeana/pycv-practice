#!/usr/bin/python
# -*- coding: UTF-8 -*-
import cv2

# 读取图片
img = cv2.imread("L.jpg")

# 显示图像
cv2.imshow("Rose", img)

# 等待显示
key = cv2.waitKey(0)

if key == 27:
	cv2.destroyAllWindows()

# 写入图像
cv2.imwrite("_L.jpg", img);