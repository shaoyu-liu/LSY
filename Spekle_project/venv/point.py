# -*- coding=GBK -*-s
import cv2
import time
import os
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import math
import copy

img = cv2.imread('F:/img4/paishe1.jpg')
dst=img.copy()
#img.copy为复制图像
# 判断图片通道数，返回值为图像的通道数
channels=img.ndim
#img.shape:2]取彩色图片的长和宽
h,w=img.shape[:2]
# 初始化一个空白的单通道图片
gray_img=np.zeros((3,3), dtype=np.uint8)

b_img=img[:,:,0]
cv2.namedWindow("image",cv2.WINDOW_FREERATIO)
cv2.imshow('image',b_img)
cv2.waitKey(0)
ret,bin_img=cv2.threshold(b_img,150,255,0)

cv2.imshow('bin_img',bin_img)
cv2.waitKey(0)
# 找轮廓 #轮廓检测函数，输入的图像只能为二值图像
contours, heridency = cv2.findContours(bin_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
# 存储中心点
centers=[]
# 圆的最大，最小半径
min_r=5
max_r=50

max_area = max_r*max_r*3.1415926
min_area = min_r*min_r*3.1415926
for i in range(len(contours)):
    # 求当前轮廓的面积
    temp_area = cv2.contourArea(contours[i])
    # 判断面积是否满足条件
    if temp_area > min_area and temp_area < max_area:
        # 填充轮廓
        cv2.drawContours(dst, contours, i, (0,255,0), -1)
        # 几何矩
        moment = cv2.moments(contours[i], True)
        # 轮廓中心坐标
        center_point = (int(moment['m10'] / moment['m00']), int(moment['m01'] / moment['m00']))
        centers.append(center_point)
        # 画十字
        cv2.line(dst, (center_point[0] - 15, center_point[1]), (center_point[0] + 15, center_point[1]),
                         (255, 0, 0), 5)
        cv2.line(dst, (center_point[0], center_point[1] - 15), (center_point[0], center_point[1] + 15),
                         (255, 0, 0), 5)

        print("数量：",len(centers))

        print("坐标：",centers)

