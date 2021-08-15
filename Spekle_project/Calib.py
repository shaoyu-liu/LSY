# Calib.py
import numpy as np

class USB_Camera(object):
    def __init__(self):
        # 左相机内参 及 畸变系数
        self.cam_matrix_left = np.array([[2938.5,0,2014.6],[0.,2947.0,1510.0],[0.,0.,1.]])
        self.distortion_l = np.array([[0.1186,-0.2492,0.0036,-0.0054,0]])
        # 右相机内参 及 畸变系数
        self.cam_matrix_right = np.array([[1798.5,0,580.9],[0.,1810.6,374.2],[0.,0.,1.]])
        self.distortion_r = np.array([[-0.2009,1.5151,-0.0050,-0.0070,0]])
        # 右边相机相对于左边相机的 旋转矩阵 R ， 平移矩阵 T
        self.R = np.array([[0.9705,0.0098,-0.2408],[-0.0143,0.9998,-0.0167],[0.2406,0.0196,0.9704]])
        self.T = np.array([[127.0640],[-7.6009],[-39.7516]])
        # 焦距
        #self.focal_length = 6.00
        # 左右相机之间的距离 取 T 向量的第一维数值 单位 mm
        #self.baseline = np.abs(self.T[0])
