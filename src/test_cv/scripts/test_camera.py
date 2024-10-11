#!/usr/bin/env python

import rospy
from cv_bridge import CvBridge
from sensor_msgs.msg import Image
import cv2

class ImageSubscriber:
    def __init__(self):
        # Khởi tạo nút ROS
        rospy.init_node('image_subscriber', anonymous=True)

        # Khởi tạo CvBridge
        self.bridge = CvBridge()

        # Đăng ký subscriber cho topic "image_raw"
        self.image_sub = rospy.Subscriber('image_raw', Image, self.callback)

    def callback(self, data):
        # Chuyển đổi ROS Image thành OpenCV Image
        try:
            cv_image = self.bridge.imgmsg_to_cv2(data, "bgr8")
        except Exception as e:
            rospy.logerr("Error: %s", str(e))
            return

        # Hiển thị hình ảnh
        cv2.imshow("Received Image", cv_image)
        cv2.waitKey(1)  # Thời gian chờ để hiển thị hình ảnh

if __name__ == '__main__':
    try:
        image_subscriber = ImageSubscriber()
        rospy.spin()  # Giữ nút hoạt động
    except rospy.ROSInterruptException:
        pass
    finally:
        cv2.destroyAllWindows()  # Đóng tất cả cửa sổ khi kết thúc

