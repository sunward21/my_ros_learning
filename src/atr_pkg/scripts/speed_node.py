#!/usr/bin/env python
# encoding:utf8

import rospy
from std_msgs.msg import String

def lidar_callback(msg):{
    rospy.logwarn(msg.data)
}
    
def chao_callback(msg):{
    rospy.loginfo(msg.data)
}

if __name__ == "__main__":
    rospy.init_node("speed_node")
    sub = rospy.Subscriber("my_chao_topic", String,  lidar_callback, queue_size= 10 )
    sub2 = rospy.Subscriber("my_lidar_topic", String,  chao_callback, queue_size= 10 )
    while not rospy.is_shutdown():{
        rospy.spin()
    }