#! /usr/bin/env python

import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist

rospy.init_node('topics_quiz_node')

pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
vel = Twist()

# while not rospy.is_shutdown():
#     pub.publish(vel)
#     rate.sleep()


def callback(msg):
    center = msg.ranges[360]
    left = msg.ranges[700]
    right = msg.ranges[20]
    # print("new readings ----------------- ")

    if (center < 1):
        # print("turn left")
        vel.linear.x = 0
        vel.angular.z = 0.5
    elif (left < 1):
        # print("turn right")
        vel.linear.x = 0
        vel.angular.z = -0.5
    elif (right < 1):
        # print("turn left too")
        vel.linear.x = 0
        vel.angular.z = 0.5
    else:
        # print("move forward")
        vel.linear.x = 0.5
        vel.angular.z = 0

    pub.publish(vel)


sub = rospy.Subscriber('/kobuki/laser/scan', LaserScan, callback)

rospy.spin()
