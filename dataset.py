import cv2
import numpy as np
import os


save_path  = "images"

list_video=os.listdir("videos")
print(list_video)
running_count = 1

count=1
for i in range(len(list_video)):
    path= "videos/"+list_video[i]
    cap=cv2.VideoCapture(path)
    while(cap.isOpened()):
        ret,frame=cap.read()
        count=count+1
        if ret==True:
            if(count%30==0):
                cv2.imwrite(save_path+"/"+str(running_count)+".jpg",frame)
                running_count=running_count+1
        else:
            cap.release()
