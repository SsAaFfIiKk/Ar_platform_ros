import cv2
import numpy as np
from cv2 import aruco


class ArucoAnalizer:
    def __init__(self):
        self.corners = []
        self.ids = []
        self.left_angels = []
        self.right_angels = []
        self.rejectedImgPoints = []
        self.left_x = 0
        self.left_y = 0
        self.right_x = 0
        self.right_y = 0