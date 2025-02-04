#!/usr/bin/env python3

import rospy        # giao tiep voi ROS 
import argparse
import time
import math
import cv2
import numpy as np
import ros_numpy    # chuyen doi massage ros thanh cac mang numpy 
from sensor_msgs.msg import Imu, Image
from geometry_msgs.msg import PoseStamped
from geometry_msgs.msg import TwistStamped
from mavros_msgs.msg import State
from mavros_msgs.srv import CommandBool, CommandBoolRequest, SetMode, SetModeRequest
from sensor_msgs.msg import LaserScan

CONMAND_FPS = 60

'''
Ref：https://github.com/danielyugoodboy/NCRL-AIDrone-Platform/tree/master/src
Flying Mode：https://docs.px4.io/main/zh/getting_started/flight_modes.html
MAVROS Basics: http://edu.gaitech.hk/gapter/mavros-basics.html
MAVROS_Tutorial: https://masoudir.github.io/mavros_tutorial/
'''

class Drone_observation():
    def __init__(self):
        '''
        1. action :
        numpy array
        shape = (2, 3)
        np.array([x,y,z],[pitch, roll, yaw])

        2. observation.pose :
        numpy array
        shape = (2, 3)
        np.array([x,y,z],[pitch, roll, yaw])

        3. observation.img :
        numpy array
        shape = (240, 320, 3)
        '''
        self.pose = None
        self.img = None

class Drone_Enviroment():           # Class de tuong tac Drone trong mo phong 
    def __init__(self):
        print("[State] : Start Drone Enviroment")
        rospy.init_node("main_enviroemnt")

        # *********************** INITIAL PARAMETER ********************* #
        # Initial parameter setup
        self.last_req = rospy.Time.now()
        self.current_state = State()
        self.current_pos = PoseStamped()
        self.current_img = Image()
        self.done = False
        self.observation = Drone_observation()

        # ************************* PX4 SETTING ************************* #

        # Set subscriber    ( nhan du lieu ve trang thai, vi tri, camera cua Drone)
        state_sub = rospy.Subscriber("/mavros/state", State, callback=self.state_cb)
        local_pos_sub = rospy.Subscriber("/mavros/local_position/pose", PoseStamped, callback=self.pos_cb)
        local_img_sub = rospy.Subscriber("/iris_rplidar/usb_cam/image_raw", Image, callback=self.img_cb)

        # Set publisher     ( gui lenh dieu khien cho Drone)
        self.local_pos_pub = rospy.Publisher("/mavros/setpoint_position/local", PoseStamped, queue_size=10)
        self.setpoint_velocity_pub = rospy.Publisher("/mavros/setpoint_velocity/cmd_vel", TwistStamped, queue_size=10)

        # Set client           ()
        print("[State] : Wait for Arming service")
        rospy.wait_for_service("/mavros/cmd/arming")  # wait service
        self.arming_client = rospy.ServiceProxy("/mavros/cmd/arming", CommandBool)      # Cap quyen bay cho Drone

        print("[State] : Wait for Set_mode service")
        rospy.wait_for_service("/mavros/set_mode")  # wait service
        self.set_mode_client = rospy.ServiceProxy("/mavros/set_mode", SetMode)          # Thiet lap che do bay cho Drone

        # Setpoint publishing MUST be faster than 2Hz
        self.rate = rospy.Rate(CONMAND_FPS)

        # Wait for Flight Controller connection
        print("[State] : Wait for Connection")
        while not rospy.is_shutdown() and not self.current_state.connected:
            self.rate.sleep()

        print("[State] : Set SetModeRequest")
        self.offb_set_mode = SetModeRequest()
        self.offb_set_mode.custom_mode = 'OFFBOARD'

        print("[State] : Set CommandBoolRequest")
        self.arm_cmd = CommandBoolRequest()
        self.arm_cmd.value = True

    def state_cb(self, data):
        self.current_state = data

    def pos_cb(self, data):
        self.current_pos = data

    def img_cb(self, data):
        image = ros_numpy.numpify(data).copy()
        self.current_img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    def position_step(self, action):
        # Confirm current_state.mode == "OFFBOARD"，give 5 sec to wait
        if self.current_state.mode != "OFFBOARD" and (rospy.Time.now() - self.last_req) > rospy.Duration(5.0):
            if self.set_mode_client.call(self.offb_set_mode).mode_sent == True:
                rospy.loginfo("OFFBOARD enabled")

            self.last_req = rospy.Time.now()

        # Confirm current_state.armed == True，give 5 sec to wait
        else:
            if not self.current_state.armed and (rospy.Time.now() - self.last_req) > rospy.Duration(5.0):
                if self.arming_client.call(self.arm_cmd).success == True:
                    rospy.loginfo("Vehicle armed")

                self.last_req = rospy.Time.now()

        # Publish action
        self.local_pos_pub.publish(self._np2PoseStamped(action))

        # Get observation
        self.observation.pose = self._PoseStamped2np(self.current_pos)
        self.observation.img = self.current_img

        # Calculate reward (for reinforcement learning)
        reward = 0

        # Done or not
        linear_distant = np.sum(np.square(self.observation.pose[0]))**0.5
        if linear_distant >= 10:
            self.done = True
        
        # Info
        info = "Nothing"

        self.rate.sleep()
        return self.observation, reward, self.done, info

    def velocity_step(self, action):
        # Confirm current_state.mode == "OFFBOARD"，give 5 sec to wait
        if self.current_state.mode != "OFFBOARD" and (rospy.Time.now() - self.last_req) > rospy.Duration(5.0):
            if self.set_mode_client.call(self.offb_set_mode).mode_sent == True:
                rospy.loginfo("OFFBOARD enabled")

            self.last_req = rospy.Time.now()

        # Confirm current_state.armed == True，give 5 sec to wait
        else:
            if not self.current_state.armed and (rospy.Time.now() - self.last_req) > rospy.Duration(5.0):
                if self.arming_client.call(self.arm_cmd).success == True:
                    rospy.loginfo("Vehicle armed")

                self.last_req = rospy.Time.now()
        
        # Publish action
        set_velocity = TwistStamped()
        yaw = self._PoseStamped2np(self.current_pos)[1][2]
        set_velocity.twist.linear.x = action[0][0]*math.cos(yaw)-action[0][1]*math.sin(yaw)
        set_velocity.twist.linear.y = action[0][0]*math.sin(yaw)+action[0][1]*math.cos(yaw)
        set_velocity.twist.linear.z = action[0][2]
        set_velocity.twist.angular.z = action[1][2]
        self.setpoint_velocity_pub.publish(set_velocity)

        # Get observation
        self.observation.pose = self._PoseStamped2np(self.current_pos)
        self.observation.img = self.current_img

        # Calculate reward (for reinforcement learning)
        reward = 0

        # Done or not
        linear_distant = np.sum(np.square(self.observation.pose[0]))**0.5
        if linear_distant >= 10:
            self.done = True
        
        # Info
        info = "Nothing"

        self.rate.sleep()
        return self.observation, reward, self.done, info

    def reset(self):
        # ************************ FLY TO INITIAL *********************** #
        # Publish inital point before start
        init_action = np.array([[0,0,2],[0,0,0*(math.pi/180)]])  # [x, y, z],[pitch, roll, yaw]
        
        for i in range(100):   
            if rospy.is_shutdown():
                break
            else:
                print("Wait for reset setpoint : {}".format(i+1) + " % ", end='\r')
                self.local_pos_pub.publish(self._np2PoseStamped(init_action))
                self.rate.sleep()
        
        # Wait the Drone to the initial point
        print("[State] : Reset & Wait the Drone to the initial point")
        init_time = time.time()
        self.last_req = rospy.Time.now()
        while not rospy.is_shutdown():
            C_1 = abs(self.current_pos.pose.position.x - init_action[0][0]) < 0.2
            C_2 = abs(self.current_pos.pose.position.y - init_action[0][1]) < 0.2
            C_3 = abs(self.current_pos.pose.position.z - init_action[0][2]) < 0.2

            if C_1 and C_2 and C_3:  # 1cm
                print("[State] : Initialize Done")
                break
            else:
                self.position_step(init_action)
        
            # calculate FPS
            current_time = time.time()
            print("Waiting Reset... / FPS : " + "{:.1f}".format(1/(current_time-init_time)), end='\r')
            init_time = current_time
        
        self.done = False
        print("[State] : Reset Done")

        self.observation.pose = self._PoseStamped2np(self.current_pos)
        self.observation.img = self.current_img

        return self.observation

    def shotdown(self):
        rospy.on_shutdown(self._myhook)

    def _np2PoseStamped(self, np_action):
        '''
        Eularian to Quaternion
        這邊的姿態使用的是四元數（Quaternion）
        q = cos(theta/2)+sin(theta/2)n
        q = cos(theta/2)+sin(theta/2)i+sin(theta/2)j+sin(theta/2)k
        q = w + xi + yj + zk
        '''
        pose = PoseStamped()
        pose.pose.position.x = np_action[0][0]
        pose.pose.position.y = np_action[0][1]
        pose.pose.position.z = np_action[0][2]
        pose.pose.orientation.x = 0*math.sin(np_action[1][2]/2)
        pose.pose.orientation.y = 0*math.sin(np_action[1][2]/2)
        pose.pose.orientation.z = 1*math.sin(np_action[1][2]/2)
        pose.pose.orientation.w = math.cos(np_action[1][2]/2)

        return pose

    def _PoseStamped2np(self, pose):
        '''
        Quaternion to Eularian
        https://www.cnblogs.com/21207-ihome/p/6894128.html
        這邊的姿態使用的是四元數（Quaternion）

        q = cos(theta/2)+sin(theta/2)n
        q = cos(theta/2)+sin(theta/2)i+sin(theta/2)j+sin(theta/2)k
        q = w + xi + yj + zk
        
        第一二象限： z:- w:- or z:+ w:+
        第三四象限： z:+ w:- or z:- w:+
        '''
        pos_X = pose.pose.position.x
        pos_Y = pose.pose.position.y
        pos_Z = pose.pose.position.z
        
        q_w = pose.pose.orientation.w
        q_x = pose.pose.orientation.x
        q_y = pose.pose.orientation.y
        q_z = pose.pose.orientation.z

        # roll
        #roll = math.atan2(2*(q_w*q_x + q_y*q_z), 1-2*(q_x**2 + q_y**2))
        
        # pitch
        #pitch  = math.asin(np.clip(2*(q_w*q_y - q_z*q_z), -1.0, 1.0))

        # yaw
        yaw = math.atan2(2*(q_w*q_z + q_x*q_y), 1-2*(q_y**2 + q_z**2))

        return np.array([[pos_X,pos_Y,pos_Z],[0, 0, yaw]])

    def _myhook(self):
        print("[State] : ROS shutdown, Drone Back to home !")


def test_main(self,data):
    env = Drone_Enviroment()
    observation = env.reset()
    action = np.array([[0,2,0],[0,0,0]])
    while True:
        print(data.ranges[-1])
        print(self.current_pos.pose.position.z)
        
        env.velocity_step(action)


if __name__ == "__main__":
    rospy.init_node('lidar_subscriber')
    sub = rospy.Subscriber("/lidar_1d_scan", LaserScan, test_main)
    