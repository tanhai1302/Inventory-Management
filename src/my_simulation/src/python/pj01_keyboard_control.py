import threading
import tkinter as tk
import copy
import time
import math
import cv2
import numpy as np
from PIL import Image, ImageTk
from env.main_enviroment import Drone_Enviroment as ENV
from pyzbar.pyzbar import decode
from sensor_msgs.msg import LaserScan
import rospy
'''
Tutorial:

w : forward
s : go back
a : left
d : right

i : up
k : down
j : counterClockwise
l : Clockwise

p : lock the drone
n : unlock the drone
h : back to initial point

'''

Done = False                # Kiem tra theard xu ly ban phim con hay ket thuc 
observation = None          # Quan sat trang thai hien tai cua PX4 tu moi truong
action = None               # Hanh dong cua Drone thuc hien
press_time = time.time()    # Thoi diem nhan phim cuoi cung de xu ly delay trong dieu khien  
drone_lock = True           # Co flag de lock and unlock ( cho phep drone di chuyen hoac dung)
already_locked = False      # Kiem tra Drone da khoa truoc do chua
back_to_home = False        # Kiem tra Drone quay lai vi tri ban dau 

class TK_KeyBoardThread(threading.Thread):          # Nhan su kien cac phim nhan tu ban phim va cap nhat cac hanh dong dieu khien Drone
    def __init__(self):
        super().__init__()
        self.x = 0
        self.y = 0
        self.z = 0
        self.yaw = 0
        self.start_control = False
    
    def xFunc_press(self, event):               # Khi duoc nhan nut 
        # forward / go_back / left / right
        global action, press_time, drone_lock, already_locked, back_to_home, i,k
        if action is not None and self.start_control:               # Kiem tra action flag and start_control khoi tao chua?
            
            # forward / back / left / right
            # action [0][0] : di chuyen theo truc X (toi lui)
            # action [0][1] : di chuyen theo truc Y (trai phai)
            # action [0][2] : di chuyen theo truc Z (len xuong)

            if event.char == 'w':             
                if action[0][0] < 2: 
                    action[0][0] += 0.1  
                i = 0
                k = 0      
            elif event.char == 's':
                if action[0][0] > -2: 
                    action[0][0] -= 0.1
                i = 0
                k = 0
            elif event.char == 'a':
                if action[0][1] < 2: 
                    action[0][1] += 0.1   
                i = 0
                k = 0        
            elif event.char == 'd':
                if action[0][1] > -2: 
                    action[0][1] -= 0.1
                i = 0
                k = 0          
            # up / down / counterClockwise / Clockwise
            elif event.char == 'i':
                i = 1
                if action[0][2] < 5: 
                    action[0][2] += 0.1
            elif event.char == 'k':
                k = 1
                if action[0][2] > -5: 
                    action[0][2] -= 0.1
            elif event.char == 'j':
                if action[1][2] < 0.5: 
                    action[1][2] += 0.1
            elif event.char == 'l':
                if action[1][2] > -0.5: 
                    action[1][2] -= 0.1
            
            # drone lock
            elif event.char == 'p':                # Phim P : Khoa Drone  
                drone_lock = True 
            
            elif event.char == 'n':                # Phim N : Mo khoa Drone
                drone_lock = False
                already_locked = False

            elif event.char == 'h':                # phim H : Drone bay ve vi tri ban dau va khoa Drone 
                back_to_home = True
                drone_lock = True 
                already_locked = False
            
            press_time = time.time()                # Update thoi gian cuoi cung cua phim nhan duoc nhan (de tinh toan delay giua cac action) 

    def run(self):
        global Done
        # Collect events until released
        win = tk.Tk()
        win.title("KeyBoard Controller")
        win.geometry("640x360")

        # Chuyen doi sang dang hinh anh cuar Tkinter
        img = Image.open('img/controller_640x360.jpg')
        tk_img = ImageTk.PhotoImage(img)            

        # Hien thi label va hinh anh tren cua so 
        label = tk.Label(win, image=tk_img, width=640, height=360)
        label.pack()     

        # Doc tu phim nhan, khi nhan thi keyboard duoc show 
        win.bind("<KeyPress>", self.xFunc_press)
        win.mainloop()
        Done = True


def main():
    global Done, high, i, k
    global action, press_time, drone_lock, already_locked, back_to_home
    error = 0
    high = 0
    pre_high = 2
    speed_z =0
    i = 0
    k = 0
    env = ENV()
    observation = env.reset()

    KB_T = TK_KeyBoardThread()
    KB_T.start()

    action = np.array([[0,0,0],[0,0,0]])        # [[x,y,z],[0,0,yaw]]
    KB_T.start_control = True

    # Control Loop
    while True:
        sub = rospy.Subscriber("/lidar_1d_scan", LaserScan, lidar_callback)
        
        #print(env.current_pos.pose.position.z)
        # Drone is locked
        if drone_lock:
            if already_locked:
                pass 
            else:
                old_observation = copy.copy(observation)
                already_locked = True

            #print("Drone is locked, press [n-key] to unlock!!, press [p-key] to lock again!!   ", end='\r')
            next_observation, reward, done, info = env.position_step(old_observation.pose)
            observation = next_observation

        # Drone is unlocked
        else:           # Drone giam toc cho toi khi dung lai 
            # fly
            #print(high)
            if (time.time() - press_time) > 0.5:                # If not press keyboard, Drone stop here 
                if (time.time() - press_time) < 0.7:
                    pre_high = high
                error = high - pre_high
                if error < -0.1 :
                    if speed_z < 0.4: 
                        speed_z += 0.1
                elif error > 0.1 :
                    if speed_z > -0.4: 
                        speed_z -= 0.1
                else:
                    speed_z = 0

                action = np.array([[0, 0, speed_z], [0, 0, 0]])
                


            elif (time.time() - press_time) > 0.1:              # Sau 0,1s tu khi nhan phim, Drone giam toc dan dan toi 0.5s thi dung lai
                action = action / 4
                action[1][2] = 0
            elif (time.time() - press_time) <= 0.1:
                if not (i == 1 or k == 1):
                    error = high - pre_high
                    if error < -0.1 :
                        if action[0][2] < 0.4: 
                            action[0][2] += 0.1
                    elif error > 0.1 :
                        if action[0][2] > -0.4: 
                            action[0][2] -= 0.1
                    else:
                        action[0][2] = 0
                    print(high,pre_high)
                
            #print("Action XYZyaw : {:.2f}, {:.2f}, {:.2f}, {:.2f}".format(action[0][0], action[0][1], action[0][2], action[1][2]), end='\r')
            next_observation, reward, done, info = env.velocity_step(action)
            observation = next_observation
            #print(action[0][2])
        if back_to_home:
            observation = env.reset()
            back_to_home = False
            drone_lock = True
            already_locked = False

        frame = observation.img               # Lay hinh anh tu trang thai hien tai cua Drone 
        '''try:
            barcodes = decode(frame)
            if barcodes:
                for barcode in barcodes:
                    # Lay toa do cua hinh chu nhat bao quanh ma QR
                    points = barcode.polygon
                    pts = [(point.x, point.y) for point in points]
                    pts = np.array(pts, np.int32)
                    pts = pts.reshape((-1, 1, 2))
                    # Neu so diem khong bang 4, bo qua ma nay
                    if len(pts) == 4:
                        #print(p)
                        barcode_data = barcode.data.decode('utf-8')
                        barcode_type = barcode.type
                        text = f"{barcode_data}"
                        #print(pts)
                        frame = cv2.polylines(frame, [pts], True, (0, 255, 0), 3)
                        cv2.putText(frame, text, (pts[0][0][0], pts[0][0][1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 1,(0, 0, 255), 3, cv2.LINE_AA)
        except AssertionError as e:
            print(f"Error decoding barcode: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")'''                                                                              
        cv2.imshow('QR_code',frame)
        #cv2.imshow("Image window", cur_img)
        cv2.waitKey(3)

        if Done:
            break

    # wait for KeyBoardThread to finish
    cv2.destroyAllWindows()
    KB_T.join()
    env.reset()
    env.shotdown()
def lidar_callback(data):
    global high
    # In các giá trị khoảng cách đầu tiên
    high = data.ranges[-1]
    #print(high)

if __name__ == "__main__":
    #rospy.init_node('lidar_subscriber')
    
    main()
    
