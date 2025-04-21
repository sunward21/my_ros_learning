#!/usr/bin/env python3
# coding=utf-8

import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist

count = 0
def lidar_callback(msg):
    global vel_pub ,last_action
    global count 
    # dist = msg.ranges[180]
    dist_front = msg.ranges[305] #公司的是前180度分成610份，所以正前方应该是305
    dist_left = msg.ranges[609]
    dist_mid_left = msg.ranges[609]
    dist_right = msg.ranges[0]
    dist_mid_right = msg.ranges[0]
    vel_cmd = Twist()
    rospy.loginfo("正前方测距数值 = %f 米",dist_front)
    rospy.loginfo("正左方测距数值 = %f 米",dist_left)
    rospy.loginfo("正右方测距数值 = %f 米",dist_right)
    if count > 0:
        count = count - 1
        rospy.logwarn("持续转向 count = %d",count)
        # if 0 < dist_mid_left < 0.3:  # 左前有障碍
        #         vel_cmd.linear.x = 0.05
        #         vel_cmd.angular.z = -0.6  # 右转避开
        #         rospy.logwarn("动态右转避开左侧障碍")
                
        # elif 0 < dist_mid_right < 0.3:  # 右前有障碍
        #     vel_cmd.linear.x = 0.05
        #     vel_cmd.angular.z = 0.6  # 左转避开
        #     rospy.logwarn("动态左转避开右侧障碍")
                
        # else:  # 维持原转向逻辑
                # vel_cmd.angular.z = last_action['angular']  
                # vel_cmd.linear.x = last_action['linear']
        vel_cmd.angular.z = last_action['angular']  
        vel_cmd.linear.x = last_action['linear']
        vel_pub.publish(vel_cmd)
        return  # 退出，避免进入后续判断
    else:
        if 0<dist_front < 0.4 :
            if 0<dist_mid_left<0.3 and 0<dist_mid_left<0.3:
                vel_cmd.linear.x = -0.1
                vel_cmd.angular.z = 0.4
                last_action = {'linear': -0.1, 'angular': 0.4}
            vel_cmd.angular.z = 0.4
            last_action = {'linear': 0, 'angular': 0.4}
            count = 40
        elif 0<dist_mid_left<0.5:
            vel_cmd.linear.x = 0.1
            vel_cmd.angular.z =-0.4
            last_action = {'linear': 0.1, 'angular': -0.4}
            count = 40
        elif 0<dist_mid_right<0.5:
            vel_cmd.linear.x = 0.1
            vel_cmd.angular.z =0.4
            last_action = {'linear': 0.1, 'angular': 0.4}
            count = 40
        else:
            vel_cmd.linear.x = 0.1

    vel_pub.publish(vel_cmd)
    
if __name__ == "__main__":
    rospy.init_node("lidar_node")
    sub = rospy.Subscriber("/scan", LaserScan,  lidar_callback, queue_size= 10 )
    vel_pub = rospy.Publisher("/mobile_base/mobile_base_controller/cmd_vel", Twist, queue_size= 10)
    rospy.spin()
