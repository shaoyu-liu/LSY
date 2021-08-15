import cv2
import math
import numpy as np

img_L = cv2.imread("F:/img4/chongjian1.jpg",0)
img_R = cv2.imread("F:/img4/moban.jpg",0)

#求图像块均值
def mean(v,hw,u,img):
    sum = 0; h = 2*hw+1
    for i in range(v-hw,v+hw+1):
        for j in range(u-hw,u+hw+1):
            sum = sum+img[i,j]
    return sum/(h*h)

def sum_def1(u,v,hw,img):
    sum = 0
    for i in range(v-hw,v+hw+1):
        for j in range(u-hw,u+hw+1):
            sum = sum+img[i,j]-mean(v,hw,u,img)
    return sum


def sum_def2(u,v,hw,img):
    sum = 0
    for i in range(v - hw, v + hw + 1):
        for j in range(u - hw, u + hw + 1):
            sum = sum + (img[i, j] - mean(v, hw, u, img))*(img[i, j] - mean(v, hw, u, img))
    return sum


def ZNCC(u1,v1,hw,img1,u2,v2,img2):
    nc = sum_def1(u1,v1,hw,img1)*sum_def1(u2,v2,hw,img2)/math.sqrt(sum_def2(u1,v1,hw,img1)*sum_def2(u2,v2,hw,img2))
    return nc

IL = cv2.imread('F:/img4/paishe1.jpg',0)
subL = IL[100:150,100:150]
subR = subL-5

def h(subL):
    [w,h] = subL.shape
    s = np.zeros((h,w))
    mean = np.sum(subL)/(w*h)
    for i in range(0,w):
        for j in range(0,h):
            m = (subL[i,j])-mean
            s[i,j] = m*m
            if s[i,j]>255:
                s[i,j] = 255
                return s





















