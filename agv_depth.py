import cv2
import sys
import numpy
from realsense_camera import *
numpy.set_printoptions(threshold=sys.maxsize)
rs=RealsenseCamera()

red_color=(0,0,255)

while True:
    ret,bgr_frame,depth_frame=rs.get_frame_stream()
    
    depth_frame=np.where(depth_frame==0,10000,depth_frame)
    temp=depth_frame[0:240,0:848].min()
    # cv2.imshow("depth_frame",depth_frame)
    print(temp)
    if temp<400:
        print(temp)
        print("Collision detected!")
        # collided_pixel=np.where(depth_frame[0:180]==np.min(depth_frame[0:180]))
        # for spot in collided_pixel:
        #     print(spot)
        cv2.rectangle(bgr_frame,(0,0),(848,240),red_color,3)
        cv2.imshow("bgr_frame",bgr_frame)
    else:
        cv2.imshow("bgr_frame",bgr_frame)
        
    key=cv2.waitKey(1)
    if key==27:
        rs.release()
        break