#!/usr/bin/env python
# encoding:utf8

import rospy
from geometry_msgs.msg import Twist

if __name__ == "__main__":
    rospy.init_node("vel_node")
    rospy.logwarn("vel_node is activated")

    vel_pub = rospy.Publisher("cmd/vel", Twist, queue_size=10)
    vel_msg = Twist()+
    vel_msg.linear.x = 1

    rate = rospy.Rate(30)

    while not rospy.is_shutdown():
        vel_pub.publish(vel_msg)
        rate.sleep()