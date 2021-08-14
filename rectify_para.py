import cv2
import numpy as np


img1 = cv2.imread('F:/img7/rectify/l.jpg')
img2 = cv2.imread('F:/img7/rectify/r.jpg')
left_K = np.array([[2841.19748840068,0,1277.32943109402],
          [0,2841.68101006102,998.108813927108],
          [0,0,1]])

left_distortion = np.array([-0.0805860281463889,
                 0.249844065078291,
                 0.000498026864412450,
                 -0.000595619161401241,
                 -0.403860765636576])

right_K =np.array( [[2870.54993856513,0,1294.00095866089],
          [0,2870.44121592984,985.654528905497],
          [0,0,1]])

right_distortion=np.array([-0.0517230491968472,
                  -1.07887076434802,
                  0.00103485446686674,
                  0.00193286437738706,
                  14.6107203936659])

R = np.array([[0.994726868935536,-0.00124427326589798,0.102551977073798],
                   [0.00135843631160404,0.999998532993470,-0.00104338952209819],
                   [-0.102550528367690,0.00117719792188071,0.994727099930710]])

T=np.array([[-194.021394132611],[0.119360227762203],[21.3256690533881]])


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

cv2.imwrite('F:/img7/rectify/img1.jpg',rectifyed_img1)
cv2.imwrite('F:/img7/rectify/img2.jpg',rectifyed_img2)

