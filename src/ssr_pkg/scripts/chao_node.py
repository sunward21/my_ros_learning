#!/usr/bin/env python
# encoding:utf8

import rospy
from std_msgs.msg import String
from qq_msgs.msg import carry
if __name__ == "__main__":
    rospy.init_node("chao_node")
    rospy.logwarn("chao!py!")

    pub = rospy.Publisher("my_chao_topic", carry, queue_size=10)
    rate = rospy.Rate(10)

    while not rospy.is_shutdown():
        rospy.loginfo("chao!!!py")
        msg = carry()
        msg.data = "msg_of_chao_py"
        msg.star = 10
        msg.grade = "wangzhe"
        pub.publish(msg)
        rate.sleep()