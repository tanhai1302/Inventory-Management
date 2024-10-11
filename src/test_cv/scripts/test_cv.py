#!/usr/bin/env python

import rospy
import cv2
from cv_bridge import CvBridge
from sensor_msgs.msg import Image

def main():
    # Khởi tạo nút ROS
    rospy.init_node('camera_publisher', anonymous=True)

    # Tạo publisher cho topic "image_raw"
    image_pub = rospy.Publisher('image_raw', Image, queue_size=10)

    # Khởi tạo CvBridge
    bridge = CvBridge()

    # Mở camera
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        rospy.logerr("can not open camera")
        return

    rate = rospy.Rate(10)  # Tần suất publish 10Hz

    while not rospy.is_shutdown():
        # Đọc frame từ camera
        ret, frame = cap.read()
        if not ret:
            rospy.logerr("can not read camera")
            break

        # Chuyển đổi frame OpenCV thành ROS Image
        ros_image = bridge.cv2_to_imgmsg(frame, encoding="bgr8")

        # Publish hình ảnh lên topic
        image_pub.publish(ros_image)

        # Hiển thị hình ảnh (tuỳ chọn)
        # cv2.imshow("Camera Feed", frame)
        # if cv2.waitKey(1) & 0xFF == ord('q'):
        #    break

        rate.sleep()

    # Giải phóng camera và đóng tất cả cửa sổ
    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass

