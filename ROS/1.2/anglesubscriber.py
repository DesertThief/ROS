import rospy
import numpy
import math
from std_msgs.msg import Float64MultiArray,MultiArrayLayout,MultiArrayDiesion,Float64


def stats_callback(data):

median = data.median
mean = data.mean

rospy.logwarn(median)
rospy.logwarn(mean)
def AngleListener():


    rospy.init_node('AngleListener', anonymous=True)

    rospy.Subscriber("AnglesWithStats", Float64, callback)

    rospy.spin()

if __name__ == '__main__':
    angleListener()
