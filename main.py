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
    
    configPath = "./cfg/knockknock_cfg.cfg"
    weightPath = "./knockknock_cfg_best.weights"
    metaPath = "./cfg/obj.data"
if __name__ == "__main__":
  main()
