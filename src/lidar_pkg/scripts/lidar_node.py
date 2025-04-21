#!/usr/bin/env python3
# coding=utf-8

import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist

count = 0
def lidar_callback(msg):
    global vel_pub #这里全局变量是为啥
    global count #这里全局变量是为啥
    # dist = msg.ranges[180]
    dist_front = msg.ranges[305] #公司的是前180度分成610份，所以正前方应该是305
    dist_left = msg.ranges[609]
    dist_right = msg.ranges[0]
    rospy.loginfo("正前方测距数值 = %f 米",dist_front)
    rospy.loginfo("正左方测距数值 = %f 米",dist_left)
    rospy.loginfo("正右方测距数值 = %f 米",dist_right)
    if count > 0:
        count = count - 1
        rospy.logwarn("持续转向 count = %d",count)
        return
    
    vel_cmd = Twist() #这里加括号是啥意思？
    if dist_front < 0.2 :
        vel_cmd.angular.z = 1.5
        count = 50
    else:
        vel_cmd.linear.x = 0.3

    vel_pub.publish(vel_cmd)
    
if __name__ == "__main__":
    rospy.init_node("lidar_node")
    sub = rospy.Subscriber("/scan", LaserScan,  lidar_callback, queue_size= 10 )
    vel_pub = rospy.Publisher("/mobile_base/mobile_base_controller/cmd_vel", Twist, queue_size= 10)
    rospy.spin()
