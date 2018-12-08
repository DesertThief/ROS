import rospy
import numpy
import math
from std_msgs.msg import Float64MultiArray,MultiArrayLayout,MultiArrayDiesion,Float64






def talker():
    pub = rospy.Publisher('chatter', Float64MultiArray, queue_size=10)
    rospy.init_node('talker', anonymous=True)
	
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        radian1 = (angle1 * math.pi)/180
	radian2 = (angle2 * math.pi)/180
	radian3 = (angle3 * math.pi)/180
	radian4 = (angle4 * math.pi)/180
	radian5 = (angle5 * math.pi)/180
	radian6 = (angle6 * math.pi)/180
	
	float64[] array
	a = Float64List()
	a.array = [radian1,radian2,radian3,radian4,radian5]		
	
	pub.publish(a)

        rate.sleep()




def callback1(angle):
    angle1 = angle.data
def callback2(angle):
    angle2 = angle.data
def callback3(angle):
    angle3 = angle.data
def callback4(angle):
    angle4 = angle.data
def callback5(angle):
    angle5 = angle.data
def callback6(angle):
    angle6 = angle.data
def listener():

   
    

rospy.Subscriber("/standing2/JointState1", Float64,callback1)
rospy.Subscriber("/standing2/JointState2", Float64,callback2)
   rospy.Subscriber("/standing2/JointState3", Float64,callback3)
   rospy.Subscriber("/standing2/JointState4", Float64,callback4)
   rospy.Subscriber("/standing2/JointState5", Float64,callback5)   
rospy.Subscriber("/standing2/JointState6", Float64,callback6)

if _name_ == '_main_':
    try:
        talker()
    except rospy.ROS
InterruptException:
        pass
