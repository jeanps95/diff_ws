#! /usr/bin/env python


# import rospy
# from sensor_msgs.msg import LaserScan
# from sensor_msgs.msg import Image
# from geometry_msgs.msg import Twist
# from nav_msgs.msg import Odometry
# from tf import transformations
import numpy as np
import cv2, PIL
from cv2 import aruco
import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd
# %matplotlib nbagg
frame = cv2.imread("/home/jean/diff_ws/src/robotDiff/robot_diff_description/meshes/MarkerData_1234.png")
plt.figure()
plt.imshow(frame)
plt.show()

# %%time
# gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
# aruco_dict = aruco.Dictionary_get(aruco.DICT_6X6_250)
# parameters =  aruco.DetectorParameters_create()
# corners, ids, rejectedImgPoints = aruco.detectMarkers(gray, aruco_dict, parameters=parameters)
# frame_markers = aruco.drawDetectedMarkers(frame.copy(), corners, ids)

# plt.figure()
# plt.imshow(frame_markers)
# for i in range(len(ids)):
#     c = corners[i][0]
#     plt.plot([c[:, 0].mean()], [c[:, 1].mean()], "o", label = "id={0}".format(ids[i]))
# plt.legend()
# plt.show()