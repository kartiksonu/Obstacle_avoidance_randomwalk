#! /usr/bin/python

import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist
from geometry_msgs.msg import Vector3

def laser_callback(msg):

	scan_values = msg.ranges
	idx = [0, 45, 90, 135, 180, 225, 270, 315, 359]
	scan_segmented = [ scan_values[i] for i in idx ]

	collision_threshold = 1
	collision_detection_flag = 0

	velocity_publisher = rospy.Publisher('/cmd_vel', Twist, queue_size=3)
	vel_msg = Twist()

	for i in idx:
		if scan_values[i] <= collision_threshold:
			collision_detection_flag = 1


	if collision_detection_flag == 1 :
		
		#stop 
		rospy.loginfo('collision detected!')
		vel_msg.linear.x=0
		vel_msg.linear.y=0
		vel_msg.linear.z=0
		vel_msg.angular.x = 0
		vel_msg.angular.y = 0
		vel_msg.angular.z = 0


		#Change the angular direction
		vel_msg.linear.x=0
		vel_msg.linear.y=0
		vel_msg.linear.z=0
		vel_msg.angular.x = 0
		vel_msg.angular.y = 0
		vel_msg.angular.z = 0.05

		velocity_publisher.publish(vel_msg)

	else:
		rospy.loginfo('robot not in collision!')
		#Move with constant velocity
		vel_msg.linear.x=0.1
		vel_msg.linear.y=0
		vel_msg.linear.z=0
		vel_msg.angular.x = 0
		vel_msg.angular.y = 0
		vel_msg.angular.z = 0

		velocity_publisher.publish(vel_msg)




def randomwalk():
	rospy.init_node('laser_readings')
	laser_sub = rospy.Subscriber('/mybot/laser/scan', LaserScan, laser_callback)
	rospy.spin()




if __name__ == '__main__':
    try:
        # Testing our function
        randomwalk()
    except rospy.ROSInterruptException:
        pass





