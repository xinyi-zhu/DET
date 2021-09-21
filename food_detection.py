import cv2
import numpy as np
import argparse
from time import sleep
import time
#from adafruit_crickit import crickit
#from adafruit_seesaw.neopixel import NeoPixel
from scipy.spatial import distance as dist
from collections import OrderedDict
from pythonosc import osc_message_builder
from pythonosc import udp_client
import random 
from collections import OrderedDict


sender = udp_client.SimpleUDPClient('127.0.0.1', 4560)

object_list = ["banana","apple","orange","broccoli","carrot","donut","cake","sandwich"]

# color_list = OrderedDict({
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

# def getColorName(R,G,B):
#     minimum = 1000
#     #sio.savemat('colors.mat',colors)
#     for (i,(name,rgb)) in enumerate(color_list.items()):
#         d = abs(R-int(rgb[0]))+ abs(G-int(rgb[1]))+ abs(B-int(rgb[2]))
#         if (d<minimum):
#             minimum = d
#             color_name = name
#     return color_name

def getColorName(H):
    #sio.savemat('colors.mat',colors)
    if h in range(0,10):
        return "red"
    elif h in range(10,25):
        return "orange"
    elif h in range(25,35):
        return "yellow"
    elif h in range(35,50):
        return "lightgreen"
    elif h in range(50,75):
        return "green"
    elif h in range(75,95):
        return "lightblue"
    elif h in range(95,110):
        return "blue"
    elif h in range(110,125):
        return "darkblue"
    elif h in range(125,145):
        return "purple"
    elif h in range(145,155):
        return "lightpink"
    elif h in range(144,165):
        return "darkpink"
    else:
        return "coral"

# color_list = OrderedDict({
#     "red":[''],
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

net = cv2.dnn.readNet('yolov3.weights','yolov3.cfg')
classes = []
with open('yolov3.txt','r') as f:
    classes = f.read().splitlines()

cap = cv2.VideoCapture(0)
#img = cv2.imread('fruits.jpg')
width = 400
height = 400

frame_rate = 0.5
previous = 0

# get the sender to Sonic Pi ready 
sender = udp_client.SimpleUDPClient('127.0.0.1', 4560)

while True:
    
    _,frame = cap.read()
    #height, width, _ = frame.shape
    frame = cv2.resize(frame,(width,height))

    # run the pretrained data
    blob = cv2.dnn.blobFromImage(frame, 1/255, (416,416), (0,0,0), swapRB=True, crop=False)
    net.setInput(blob)
    output_layers_names = net.getUnconnectedOutLayersNames()
    layerOutputs = net.forward(output_layers_names)

    boxes = []
    confidences = []
    class_ids = []

    for output in layerOutputs:
        for detection in output:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > 0.5:
                center_x = int(detection[0] * width)
                center_y = int(detection[1] * height)
                w = int(detection[2] * width)
                h = int(detection[3] * height)
                
                x = int(center_x - w/2)
                y = int(center_y - h/2)
                
                boxes.append([x,y,w,h])
                confidences.append((float(confidence)))
                class_ids.append(class_id)

    indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)       
    font = cv2.FONT_HERSHEY_PLAIN
    colors = np.random.uniform(0,255,size=(len(boxes),3))
    
    #if object detected
    if len(indexes) >0 :
        for i in indexes.flatten():
            x,y,w,h = boxes[i]
            label = str(classes[class_ids[i]])
            confidence = str(round(confidences[i],2))
            color = colors[i]
            cv2.rectangle(frame, (x,y), (x+w, y+h), color, 2)
            cv2.putText(frame, label, (x,y+20), font, 1, (255,255,255), 2)

        #time_elapsed = time.time() - previous

        #return the color that is in the center of the frame
        #and send message to the Sonic pi: label(group) + color 
        #if time_elapsed > 1./frame_rate:
        #    previous = time.time()
        
            # Hue range is [0,179], Saturation range is [0,255] and Value range is [0,255]
        hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) # hue, sat, val
            
        #convert rgb to hsv and use vision 
        H = hsv_frame[:, :, 0].astype(np.float32)  # hue
        S = hsv_frame[:, :, 1].astype(np.float32)  # saturation
        V = hsv_frame[:, :, 2].astype(np.float32)  # value

        #b,g,r= frame[center_x,center_y]
        #cv2.imshow("Frame", frame)

        # get object label
        text = getColorName(H)    
        print(label, text)  
        key = cv2.waitKey(1) & 0xFF
        sender = udp_client.SimpleUDPClient('127.0.0.1', 4560)

        pitch = random.randint(50,90)
            # get object color and map to notes
        if label == 'banana':
            sender.send_message('/play_this',1)
        elif label == 'apple':
            sender.send_message('/play_this',2)
        elif label == 'orange':
            sender.send_message('/play_this',3)
        elif label == 'broccoli':
            sender.send_message('/play_this',4)
        elif label == 'carrot':
            sender.send_message('/play_this',5)
        elif label == 'donut':
            sender.send_message('/play_this',6)
        elif label == 'cake':
            sender.send_message('/play_this',7)
        else:
            sender.send_message('/play_this',8)
        
        sleep(1)
            
    else:
        continue
        
    if key == ord("q"):
        break
  
cap.release()