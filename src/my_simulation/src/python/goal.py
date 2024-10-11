import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from geometry_msgs.msg import PoseStamped

def send_goal(x, y, z, frame_id="map"):
    # Khởi tạo ROS node
    rospy.init_node('move_base_client')

    # Tạo client cho action MoveBase
    client = actionlib.SimpleActionClient('move_base', MoveBaseAction)

    # Đợi cho server sẵn sàng
    rospy.loginfo("Waiting for move_base action server...")
    client.wait_for_server()

    # Tạo một mục tiêu
    goal = MoveBaseGoal()
    goal.target_pose.header.frame_id = frame_id
    goal.target_pose.header.stamp = rospy.Time.now()

    # Thiết lập vị trí mục tiêu
    goal.target_pose.pose.position.x = x
    goal.target_pose.pose.position.y = y
    goal.target_pose.pose.orientation.z = z  # Hướng mục tiêu (quaternion)

    # Gửi mục tiêu
    rospy.loginfo("Sending goal: (%f, %f, %f)", x, y, z)
    client.send_goal(goal)

    # Chờ cho robot hoàn thành việc di chuyển
    client.wait_for_result()

    # Kiểm tra kết quả
    if client.get_state() == actionlib.GoalStatus.SUCCEEDED:
        rospy.loginfo("Goal reached!")
    else:
        rospy.logwarn("Failed to reach goal.")

if __name__ == "__main__":
    try:
        send_goal(0.32, 6.57, 0.72)  # Thay đổi tọa độ x, y theo ý muốn
    except rospy.ROSInterruptException:
        pass
