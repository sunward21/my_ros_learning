#!/usr/bin/env python3
# coding=utf-8

import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist

count = 0
def lidar_callback(msg):
    global vel_pub #这里全局变量是为啥
    global count #这里全局变量是为啥
    dist = msg.ranges[180]
    rospy.loginfo("正前方测距数值 = %f 米",dist)

    if count > 0:
        count = count - 1
        rospy.logwarn("持续转向 count = %d",count)
        return
    
    vel_cmd = Twist() #这里加括号是啥意思？
    if dist < 1.5 :
        vel_cmd.angular.z = 0.3
        count = 50
    else:
        vel_cmd.linear.x = 0.05

    vel_pub.publish(vel_cmd)
    
if __name__ == "__main__":
    rospy.init_node("lidar_node")
    sub = rospy.Subscriber("/scan", LaserScan,  lidar_callback, queue_size= 10 )
    vel_pub = rospy.Publisher("cmd_vel", Twist, queue_size= 10)
    rospy.spin()
