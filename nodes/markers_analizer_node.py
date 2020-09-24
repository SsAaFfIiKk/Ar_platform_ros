#!/usr/bin/env python3

import rospy
from platform.msg import ArucoData
from vision.MarkersAnalizer import MarkersAnalizer


analizer = MarkersAnalizer()

rospy.spin()