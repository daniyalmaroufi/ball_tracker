#!/usr/bin/python3

import rospy
import cv2
import numpy as np
from std_msgs.msg import String

def publisher_fun():
    max_radius=0
    max_center=(0,0)

    lower=np.array([7,137,132])
    upper=np.array([25,255,255])

    cap=cv2.VideoCapture(0)

    rospy.init_node('camvi')
    pub = rospy.Publisher('cvpos', String, queue_size=10)
    rate = rospy.Rate(10)

    while not rospy.is_shutdown():
        ret, frame = cap.read()
        if frame is None:
            break

        hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
        out=cv2.inRange(hsv,lower,upper)

        erosion=cv2.erode(out,None,iterations=1)
        dilate=cv2.dilate(erosion,None,iterations=2)
        cnts,_=cv2.findContours(dilate,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

        for c in cnts:
            (x, y),r=cv2.minEnclosingCircle(c)
            center=(int(x),int(y))

            r=int(r)
            if r>max_radius:
                max_radius=r
                max_center=center

        cv2.circle(frame,center,r,(0,255,0),2)
        cv2.imshow("image",frame)

        pub.publish(str(x)+'%'+str(y))
        rate.sleep()

        if cv2.waitKey(30)==ord('q'):
            break


    cv2.destroyAllWindows()
    cap.release()


if __name__ == '__main__':
    publisher_fun()


