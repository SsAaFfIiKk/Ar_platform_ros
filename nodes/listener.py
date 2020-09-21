#!/usr/bin/env python3

import cv2
import rospy
from std_msgs.msg import String
from sensor_msgs.msg import Image
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

cv_bridge = CvBridge()

def img_callback(data):
    cv_image = cv_bridge.imgmsg_to_cv2(data, "bgr8")
    img = cv_bridge
    cv2.imshow("img", img)
    cv2.waitKey(0)

def listener():
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber('camera_node', Image, img_callback)
    rospy.spin()


if __name__ == '__main__':
    listener()
