# This is going to be our main code
import os
import cv2
import numpy as np
import time
import darknet
from setEmail import email

#############################
#Send notification to email
#############################




############################
#write detections to log file
############################




#################################################
#Rules to decide if an detected object is valid
#rule 1: confident bigger or equal to 85%?
#rule 2: 
#################################################




##################################
#The main part
##################################
def main():
    #perform detection
    configPath = "./cfg/knockknock_cfg.cfg"
    weightPath = "./knockknock_cfg_best.weights"
    metaPath = "./cfg/obj.data"
    
    #decide input source
    cap = cv2.VideoCapture("")#<-enter input video address here    
    RTSP_URL = #enter RTSP URL here if using a camear
    cap = cv2.VedeoCapture(RTSP_URL)
    
    #set output video footage
    
    #a reuse image for each detection
    
    #loop through the video
        #a detection go through the rule
        #a detection go to send email and log if pass the rule
        
if __name__ == "__main__":
  main()
