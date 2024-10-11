#!/usr/bin/env python3
import rospy
import tf2_ros
from geometry_msgs.msg import TransformStamped,PoseStamped
from tf2_ros import TransformBroadcaster
#from tf2_geometry_msgs import do_transform_quaternion


def handle_odom(msg):
    br = TransformBroadcaster()
    ts = TransformStamped()

    ts.header.stamp = rospy.Time.now()
    ts.header.frame_id = "odom"
    ts.child_frame_id = "base_link"
    ts.transform.translation.x = msg.pose.position.x
    ts.transform.translation.y = msg.pose.position.y
    ts.transform.translation.z = msg.pose.position.z
    ts.transform.rotation = msg.pose.orientation
    #ts.transform.rotation = do_transform_quaternion(msg.pose.pose.orientation, tf2_ros.Transform())
    #print(msg.pose.pose.orientation)


    br.sendTransform(ts)

if __name__ == '__main__':
    rospy.init_node('rplidar_tf_node')
    rospy.Subscriber("/mavros/local_position/pose", PoseStamped, handle_odom)
    rospy.spin()