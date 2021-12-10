# import the necessary packages
#from imutils.video import VideoStream
#import argparse
#import imutils
import time
import cv2
import time
#import numpy as np
#from adafruit_crickit import crickit
from time import sleep
from scipy.spatial import distance as dist
from collections import OrderedDict
from pythonosc import osc_message_builder
from pythonosc import udp_client
import random

# colors = OrderedDict({
#     "brown":(82,0,0),
#     "darkred":(116,0,0),
#     "red":(179,0,0),
#     "lightred":(238,0,0),
#     "orange":(255,99,0),
#     "yellow":(255,236,0),
#     "lightgreen":(153,253,0),
#     "green":(40,255,0),
#     "lightblue":(0,255,232),
#     "blue":(0,124,255),
#     "darkblue":(5,0,255),
#     "purpleblue":(69,0,234),
#     "purple":(87,0,158)})

colors = OrderedDict({
    "red":(82,0,0),
    "orange":(116,0,0),
    "yellow":(179,0,0),
    "green":(238,0,0),
    "aqua":(255,99,0),
    "blue":(255,236,0),
    "purple":(153,253,0),
 })

def getColorName(R,G,B):
    minimum = 1000
    for (i,(name,rgb)) in enumerate(colors.items()):
        d = abs(R-int(rgb[0]))+ abs(G-int(rgb[1]))+ abs(B-int(rgb[2]))
        if (d<minimum):
            minimum = d
            color_name = name
    return color_name

# initialize the video stream and allow the camera sensor to warm up
print("Video Warm-Up")
capture = cv2.VideoCapture(0)

frame_rate = 0.5
previous = 0

# get the sender to Sonic Pi ready 
sender = udp_client.SimpleUDPClient('127.0.0.1', 4560)

while True:
    # grab the frame from the video stream, resize it
    # time.sleep(0.5)
    time_elapsed = time.time() - previous
    ret, frame = capture.read()
    frame = cv2.resize(frame,(400,400))
    
    if time_elapsed > 1./frame_rate:
        previous = time.time()
        
        b,g,r= frame[200,200]
        cv2.imshow("Frame", frame)
    
        colorname = getColorName(int(r),int(g),int(b))
        print(colorname)

    instrument = random.randint(0,3)
    amp = random.randint(0,3)

    if colorname == 'red': 
        #C
        sender.send_message('/play_this',[60, instrument, amp])
        # D
    elif colorname == 'orange':
        sender.send_message('/play_this',[62, instrument, amp])       
        # E
    elif colorname == 'yellow':   
        sender.send_message('/play_this',[64, instrument, amp])      
        # F
    elif colorname == 'green':
        sender.send_message('/play_this',[65, instrument, amp])           
        # G
    elif colorname == 'aqua':
        sender.send_message('/play_this',[67, instrument, amp])        
        # A
    elif colorname == 'blue':
        sender.send_message('/play_this',[69, instrument, amp])
        # B
    else:
        sender.send_message('/play_this',[71, instrument, amp])

        
    key = cv2.waitKey(1) & 0xFF
    sleep(1)
    
    key = cv2.waitKey(1) & 0xFF
    # if the `q` key was pressed, break from the loop
    if key == ord("q"):
        break
    
    
    
