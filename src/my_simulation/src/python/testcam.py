import rospy
from sensor_msgs.msg import Image
import cv2
import numpy as np
import ros_numpy

def callback(data):
    # Chuyển đổi dữ liệu hình ảnh từ ROS message sang OpenCV
    
    image = ros_numpy.numpify(data).copy()
    frame = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)


    # Hiển thị hình ảnh
    cv2.imshow("Image window", frame)
    cv2.waitKey(3)

def main():
    rospy.init_node('image_subscriber', anonymous=True)
    image_sub = rospy.Subscriber("/iris_rplidar/usb_cam/image_raw", Image, callback)
    try:
        rospy.spin()
    except rospy.ROSInterruptException:
        pass

if __name__ == '__main__':
    main()