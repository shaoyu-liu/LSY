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
#img.copyΪ����ͼ��
# �ж�ͼƬͨ����������ֵΪͼ���ͨ����
channels=img.ndim
#img.shape:2]ȡ��ɫͼƬ�ĳ��Ϳ�
h,w=img.shape[:2]
# ��ʼ��һ���հ׵ĵ�ͨ��ͼƬ
gray_img=np.zeros((3,3), dtype=np.uint8)

b_img=img[:,:,0]
cv2.namedWindow("image",cv2.WINDOW_FREERATIO)
cv2.imshow('image',b_img)
cv2.waitKey(0)
ret,bin_img=cv2.threshold(b_img,150,255,0)

cv2.imshow('bin_img',bin_img)
cv2.waitKey(0)
# ������ #������⺯���������ͼ��ֻ��Ϊ��ֵͼ��
contours, heridency = cv2.findContours(bin_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
# �洢���ĵ�
centers=[]
# Բ�������С�뾶
min_r=5
max_r=50

max_area = max_r*max_r*3.1415926
min_area = min_r*min_r*3.1415926
for i in range(len(contours)):
    # ��ǰ���������
    temp_area = cv2.contourArea(contours[i])
    # �ж�����Ƿ���������
    if temp_area > min_area and temp_area < max_area:
        # �������
        cv2.drawContours(dst, contours, i, (0,255,0), -1)
        # ���ξ�
        moment = cv2.moments(contours[i], True)
        # ������������
        center_point = (int(moment['m10'] / moment['m00']), int(moment['m01'] / moment['m00']))
        centers.append(center_point)
        # ��ʮ��
        cv2.line(dst, (center_point[0] - 15, center_point[1]), (center_point[0] + 15, center_point[1]),
                         (255, 0, 0), 5)
        cv2.line(dst, (center_point[0], center_point[1] - 15), (center_point[0], center_point[1] + 15),
                         (255, 0, 0), 5)

        print("������",len(centers))

        print("���꣺",centers)

