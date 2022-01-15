#!/usr/bin/python3

import rospy
import cv2
import numpy as np
from std_msgs.msg import String

def des_pos(pos):
    pub = rospy.Publisher('trpos', String, queue_size=10)
    rate = rospy.Rate(10)
    x,y=str(pos.data).split('%')
    desx=float(x)/640*5.5
    desy=float(y)/480*5.5
    
    # while not rospy.is_shutdown():
    pub.publish(str(desx)+'%'+str(desy))
    rate.sleep()

def publisher_fun():
    rospy.init_node('turtle_main')

    pose_subscriber = rospy.Subscriber('cvpos',String, des_pos)

    rospy.spin()

if __name__ == '__main__':
    publisher_fun()


