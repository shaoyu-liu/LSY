import cv2
import numpy as np


img1 = cv2.imread('F:/img7/rectify/1.jpg')
img2 = cv2.imread('F:/img7/rectify/2.jpg')
left_K = np.array([[2854.7438,0,1275.4631],
          [0,2854.71704,991.68540],
          [0,0,1]])

left_distortion = np.array([-0.08464,0.284904,0.000193,-0.000811,-0.52550])

right_K =np.array( [[2859.42855,0,1291.6637],
          [0,2859.3680,987.46299],
          [0,0,1]])

right_distortion=np.array( [-0.07351,0.163047,0.001028,0.0011899,0.061290])

R = np.array([[0.971018,-0.05993,0.23136],
                   [0.054323,0.99805,0.0305],
                   [-0.23274,-0.017109,0.97238]])

T=np.array( [-376.9965,-38.0407,39.7114])

width = 2592
height = 1944

R1, R2, P1, P2, Q,roi1,roi2 = cv2.stereoRectify(left_K, left_distortion, right_K, right_distortion,
                                                      (width, height), R, T, alpha=0)

map1x, map1y = cv2.initUndistortRectifyMap(left_K, left_distortion, R1, P1, (width, height), cv2.CV_32FC1)
map2x, map2y = cv2.initUndistortRectifyMap(right_K, right_distortion, R2, P2, (width, height), cv2.CV_32FC1)

rectifyed_img1 = cv2.remap(img1, map1x, map1y, cv2.INTER_AREA)
rectifyed_img2 = cv2.remap(img2, map2x, map2y, cv2.INTER_AREA)

cv2.namedWindow("img1",cv2.WINDOW_KEEPRATIO)
cv2.namedWindow("img2",cv2.WINDOW_KEEPRATIO)
cv2.imshow("img1",rectifyed_img1)
cv2.imshow("img2",rectifyed_img2)
cv2.waitKey(0)

cv2.imwrite('img1.jpg',rectifyed_img1)
cv2.imwrite('img2.jpg',rectifyed_img2 )

