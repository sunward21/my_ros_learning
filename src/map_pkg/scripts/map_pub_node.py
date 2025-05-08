#!/usr/bin/env python
# encoding:utf8

import rospy
from nav_msgs.msg import OccupancyGrid

if __name__ == "__main__":
    rospy.init_node("map_node")
    rospy.logwarn("map_node is activated")
    vel_pub = rospy.Publisher("/map", OccupancyGrid, queue_size=10)
    rate = rospy.Rate(1)

    while not rospy.is_shutdown():
        vel_msg = OccupancyGrid()

        vel_msg.header.frame_id = "map"
        vel_msg.header.stamp = rospy.Time.now()

        vel_msg.info.origin.position.x = 0
        vel_msg.info.origin.position.y = 0
        vel_msg.info.resolution = 1.0
        vel_msg.info.width = 4
        vel_msg.info.height = 2

        vel_msg.data = [0]*4*2
        vel_msg.data[0] = 100
        vel_msg.data[1] = 100
        vel_msg.data[2] = 0
        vel_msg.data[3] = -1
        vel_pub.publish(vel_msg)
        rate.sleep()