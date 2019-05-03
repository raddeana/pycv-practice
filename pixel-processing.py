#!/usr/bin/python
# -*- coding: UTF-8 -*-
import cv2

# 读取图片
img = cv2.imread("L.jpg", cv2.IMREAD_UNCHANGED)

t = img[88,142]
print (t)

img[88,142] = [255, 255, 255]
print (t)

# 分别获取BGR通道像素
blue = img[88,142,0]
print(blue)

green = img[88,142,1]
print(green)

red = img[88,142,2]
print(red)

# 该行为100到200、列150到250的像素设置为白色
img[100:200, 150:250] = [255, 255, 255]

# 显示图像
cv2.imshow("Rose", img)

# 等待显示
key = cv2.waitKey(0)

if key == 27:
	cv2.destroyAllWindows()

# 写入图像
cv2.imwrite("_L.jpg", img)