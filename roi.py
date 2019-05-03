#!/usr/bin/python
# -*- coding: UTF-8 -*-
import cv2
import numpy as np

# 读取图片
img = cv2.imread("L.jpg", cv2.IMREAD_UNCHANGED)

# 定义 300 * 100 矩阵，3对应BGR
# face = np.ones((200, 200, 3))

# 显示ROI区域
face = img[0:200, 250:450]
img[0:200, 0:200] = face
cv2.imshow("Rose", img)

# 等待显示
key = cv2.waitKey(0)

if key == 27:
	cv2.destroyAllWindows()