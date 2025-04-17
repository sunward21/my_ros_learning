#include <ros/ros.h>
#include<std_msgs/String.h>

int main(int argc, char  *argv[])
{
    ros::init(argc, argv, "chao_node");
    ros::NodeHandle nh;
    ros::Publisher  pub =  nh.advertise<std_msgs::String>("my_chao_topic", 10);
    ros::Rate loop_rate(10);

    while (ros::ok())
    {
        printf("chao!\n");
        std_msgs::String msg;
        msg.data = "msg_of_chao";
        pub.publish(msg);
        loop_rate.sleep();
    }

    return 0;
} 