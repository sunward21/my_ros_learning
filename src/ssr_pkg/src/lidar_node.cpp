#include <ros/ros.h>
#include<std_msgs/String.h>

int main(int argc, char  *argv[])
{
    ros::init(argc, argv, "lidar_node");
    ros::NodeHandle nh;
    ros::Publisher  pub =  nh.advertise<std_msgs::String>("my_lidar_topic", 10);
    ros::Rate loop_rate(10);

    while (ros::ok())
    {
        printf("lidar!!!\n");
        std_msgs::String msg;
        msg.data = "lidar_msg";
        pub.publish(msg);
        loop_rate.sleep();
    }

    return 0;
} 