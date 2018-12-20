import rospy
import numpy
from std_msgs.msg import sensor_msgsLaserScan,geometry msgsTwist


def Mesagger():
geometrypublishe = rospy.publisher('cmd_vel',geometrymsgsTwist,queue_size=10)
rospy.init_node('MazePublisher', anonymous=True)

    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        if((right.angle_max - right.angle_min) < (left.angle_max - left.angle_min)):
            msg.angular.z = -0.3333333
        if((right.angle_max - right.angle_min) > (left.angle_max - left.angle_min)):
            mag.angular.z = -0.3333333

        if((right.angle_max - right.angle_min) = (left.angle_max - left.angle_min)):
            msg.linear.x = 0.1
def laserAngle1(data):
right = data.data
def laserAngle2(data):
left = data.data
def laserAngle3(data):
mid = data.data



right = rospy.Subscriber("base_scan_2", sensor_msgsLaserScan,laserAngle1)
left = rospy.Subscriber("base_scan_1", sensor_msgsLaserScan,laserAngle2)
mid = rospy.Subscriber("base_scan_0", sensor_msgsLaserScan,laserAngle3)
