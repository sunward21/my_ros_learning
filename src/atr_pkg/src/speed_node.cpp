#include <ros/ros.h>
#include <std_msgs/String.h>
void lidar_callback(std_msgs::String msg)
{
    ROS_INFO(msg.data.c_str());
}

void chao_callback(std_msgs::String msg)
{
    ROS_WARN(msg.data.c_str());
}

int main(int argc, char *argv[])
{

    ros::init(argc, argv, "speed_node");
    setlocale(LC_CTYPE, ""); // 自动继承系统Locale
    
    ros::NodeHandle nh;
    ros::Subscriber sub = nh.subscribe<std_msgs::String>("my_lidar_topic", 10, lidar_callback);
    ros::Subscriber sub_2 = nh.subscribe<std_msgs::String>("my_chao_topic", 10, chao_callback);
    while (ros::ok())
    {
        ros::spinOnce();
    }

    return 0;
}