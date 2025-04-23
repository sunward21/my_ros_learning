#!/usr/bin/env python
# coding=utf-8

import rospy
from sensor_msgs.msg import Imu
from tf.transformations import euler_from_quaternion
import math
from geometry_msgs.msg import Twist

def imu_callback(msg):
    if msg.orientation_covariance[0] < 0:
        return
    #获取四元数
    quaternion = [
        msg.orientation.x ,
        msg.orientation.y,
        msg.orientation.z,
        msg.orientation.w
    ]
    #转换成欧拉角
    (roll, pitch, yaw) = euler_from_quaternion(quaternion)
    #弧度制转换为角度制
    roll = roll*180/math.pi
    pitch = pitch*180/math.pi
    yaw = yaw*180/math.pi
    rospy.loginfo("翻滚%f  俯仰%f  朝向%f",roll, pitch, yaw)
    target_yaw = 90
    diff_angle = target_yaw - yaw
    vel_cmd = Twist()
    vel_cmd.angular.z = diff_angle*0.01
    vel_cmd.linear.x = 0.1
    global vel_pub
    vel_pub.publish(vel_cmd)
# 主函数
if __name__ == "__main__":
    rospy.init_node("imu_node")
    # 订阅激光雷达的数据话题
    # lidar_sub = rospy.Subscriber("imu/data",Imu,imu_callback,queue_size=10)
    lidar_sub = rospy.Subscriber("handsfree/imu", Imu, imu_callback,queue_size=10)
    vel_pub = rospy.Publisher("/mobile_base/mobile_base_controller/cmd_vel", Twist, queue_size= 10)
    # vel_pub = rospy.Publisher("cmd_vel", Twist, queue_size= 10)
    rospy.spin()