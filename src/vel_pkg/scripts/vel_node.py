#!/usr/bin/env python
# encoding:utf8

import rospy
from geometry_msgs.msg import Twist

if __name__ == "__main__":
    rospy.init_node("vel_node")
    rospy.logwarn("vel_node is activated")

    # vel_pub = rospy.Publisher("cmd/vel", Twist, queue_size=10) 
    #一般用这个，公司用的话题不太一样
    vel_pub = rospy.Publisher("/mobile_base/mobile_base_controller/cmd_vel", Twist, queue_size=10)
    vel_msg = Twist()
    vel_msg.linear.x = 0.1

    rate = rospy.Rate(30)

    while not rospy.is_shutdown():
        vel_pub.publish(vel_msg)
        rate.sleep()