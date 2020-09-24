#!/usr/bin/env python3

import rospy
from platform.msg import ArucoData
from src.vision.Search_aruco import SearchAruco


analizer = SearchAruco()

rospy.spin()