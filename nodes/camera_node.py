#!/usr/bin/env python3

import rospy
import cv2
from cv2 import aruco
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

# size = aruco.DICT_4X4_250
size = aruco.DICT_5X5_250
# size = aruco.DICT_6X6_250

aruco_dict = aruco.Dictionary_get(size)
parameters = aruco.DetectorParameters_create()

rospy.init_node("camera_node", anonymous=True)

cv_bridge = CvBridge()
image_publisher = rospy.Publisher("image", Image, queue_size=30)

cap = cv2.VideoCapture(0)
RUN = True
while RUN and not rospy.is_shutdown():
    ret, img = cap.read()

    if ret:
        img_message = cv_bridge.cv2_to_imgmsg(img, "bgr8")
        image_publisher.publish(img_message)
    else:
        print("Incorrect camera index")
        RUN = not RUN

cap.release()
cv2.destroyAllWindows()
