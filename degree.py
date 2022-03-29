#!/usr/bin/env python

import rospy
import tf
import math
from tf.transformations import euler_from_quaternion
from nav_msgs.msg import Odometry

class degree():
    def __init__ (self):
        rospy.init_node("odom_degree")
        rospy.Subscriber("odom",Odometry,self.callback)
        rospy.spin()

    def callback(self,data):

        self.br = tf.TransformBroadcaster()
        
        orientation_q = data.pose.pose.orientation
        orientation_list = [orientation_q.x, orientation_q.y, orientation_q.z, orientation_q.w]
        (roll, pitch, yaw) = euler_from_quaternion (orientation_list)
        print(yaw)
        degree = yaw * 180 / ( math.pi)



        # self.br.sendTransform((data.pose.pose.orientation.x,data.pose.pose.orientation.y, 0),tf.transformations.quaternion_from_euler(0, 0, yaw),
        # rospy.Time.now(),"base_link","odom")

        print("degree : {0}".format(degree))
        print("X speed : {0} Z speed : {1}".format(data.twist.twist.linear.x,data.twist.twist.angular.z))
        print("X position : {0} Y position : {1}".format(data.pose.pose.position.x,data.pose.pose.position.y))


if __name__ == "__main__":
    degree()
