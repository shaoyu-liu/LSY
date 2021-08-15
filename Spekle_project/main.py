import cv2
import numpy as np
import math

def yasuo(image):
    image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    [M,N] = image.shape
    X = math.floor(M/2)
    Y = math.floor(N/2)
    x = 1 ; y = 1

    A = np.zeros([X,Y],np.uint8)
    for m in range(0,M,2):
        for n in range(0,N,2):
            A[x,y] = image[m,n]
            y = y+1
            if y>Y :
                x = x+1
                y = 1
    A = np.uint8(A)

    return A

def my_c(subL):
    [w,h] = subL.shape
    s = np.zeros((h,w))
    mean = np.sum(subL)/(w*h)
    for i in range(0,w):
        for j in range(0,h):
            m = subL[i,j]-mean
            s[i,j] = m*m
            if s[i,j]>255:
                s[i,j] = 255
                n = np.sum(s)
                return n


def point(img):
    dst = img.copy()
    channels = img.ndim
    h, w = img.shape[:2]
    gray_img = np.zeros((3, 3), dtype=np.uint8)

    b_img = img[:, :, 0]
    cv2.namedWindow("image", cv2.WINDOW_FREERATIO)
    cv2.imshow('image', b_img)
    cv2.waitKey(0)
    ret, bin_img = cv2.threshold(b_img, 150, 255, 0)

    cv2.imshow('bin_img', bin_img)
    cv2.waitKey(0)
    contours, heridency = cv2.findContours(bin_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    centers = []
    min_r = 5
    max_r = 50

    max_area = max_r * max_r * 3.1415926
    min_area = min_r * min_r * 3.1415926
    for i in range(len(contours)):
        temp_area = cv2.contourArea(contours[i])
        if temp_area > min_area and temp_area < max_area:
            cv2.drawContours(dst, contours, i, (0, 255, 0), -1)
            moment = cv2.moments(contours[i], True)
            center_point = (int(moment['m10'] / moment['m00']), int(moment['m01'] / moment['m00']))
            centers.append(center_point)
            cv2.line(dst, (center_point[0] - 15, center_point[1]), (center_point[0] + 15, center_point[1]),
                     (255, 0, 0), 5)
            cv2.line(dst, (center_point[0], center_point[1] - 15), (center_point[0], center_point[1] + 15),
                     (255, 0, 0), 5)
            return center_point


hw = 25
IL = cv2.imread('F:/img4/paishe1.jpg',0)
IR = cv2.imread('F:/img4/paishe1.jpg',0)
# for vL in range(100,150):
#     for uL in range(100,150):
#         subL = IL[vL-hw:vL+hw,uL-hw:uL+hw]
#         [h,w] = subL.shape
#         mean1 = np.sum(subL)/(h*w)
#         s1 = np.sum(subL-mean1)
#         for uR in range(100,150):
#             for vR in range (100,150):
#                 subR = IR[vR-hw:vR+hw,uR-hw:uR+hw]
#                 [h2,w2] = subR.shape
#                 mean2 = np.sum(subR)/(h2*w2)
#                 s2 = np.sum(subR-mean2)
#                 s3 = my_c(subL)
#                 s4 = my_c(subR)
#                 kindex = 0
#                 ZNCC = np.zeros(((h2*w2),1))
#                 ZNCC[kindex] = (s1*s2)/math.sqrt(s3*s4)
#                 kindex = kindex+1

uL = 100 ; vL =100
s = IL[uL,vL]
subL = IL[uL-25:uL+25,vL-25:vL+25]
[h,w] = subL.shape
mean1 = np.sum(subL)/(h*w)
s1 = np.sum(subL-mean1)
s3 = my_c(subL)

for uR in range(uL-25,uL+25):
    for vR in range(vL-25,vL+25):
        subR = IR[uR-25:uR+25,vR-25:vR+25]
        [h2,w2] = subR.shape
        mean2 = np.sum(subR)/(h2*w2)
        s2 = np.sum(subR-mean2)
        s4 = my_c(subR)
        ZNCC = np.zeros((2500,1))
        kindex = 0
        ZNCC[kindex] = (s1*s2)/math.sqrt(s3*s4)
        kindex = kindex+1
        s = max(ZNCC)
















