import rospy
from sensor_msgs.msg import LaserScan

def lidar_callback(data):
    # In các giá trị khoảng cách đầu tiên
    print(data.ranges[-1])

if __name__ == '__main__':
    rospy.init_node('lidar_subscriber')
    sub = rospy.Subscriber("/lidar_1d_scan", LaserScan, lidar_callback)
    rospy.spin()