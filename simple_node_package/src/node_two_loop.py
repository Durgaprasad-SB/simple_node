#! /usr/bin/env python

import rospy

rospy.init_node("node_two")
rate = rospy.Rate(2)               
while not rospy.is_shutdown():     
   print "node is in active mode"
   rate.sleep()