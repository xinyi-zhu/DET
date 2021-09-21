from time import sleep
from pythonosc import osc_message_builder
from pythonosc import udp_client
import random 
from collections import OrderedDict


sender = udp_client.SimpleUDPClient('127.0.0.1', 4560)

object_list = ["banana","apple","orange","broccoli","carrot","donut","cake","sandwich"]

color_list = OrderedDict({
    "brown":(82,0,0),
    "darkred":(116,0,0),
    "red":(179,0,0),
    "lightred":(238,0,0),
    "orange":(255,99,0),
    "yellow":(255,236,0),
    "lightgreen":(153,253,0),
    "green":(40,255,0),
    "lightblue":(0,255,232),
    "blue":(0,124,255),
    "darkblue":(5,0,255),
    "purpleblue":(69,0,234),
    "purple":(87,0,158)})


while True:
    # pitch = random.randint(0,7)
    # sender.send_message('/play_fruit', (pitch+23) * 3)  
    # if object_list[pitch] in ['banana','apple','orange']:
    #     sender.send_message('/play_fruit', (pitch+23) * 3)
    # elif object_list[pitch] in ['broccoli','carrot']:
    #     sender.send_message('/play_vegetable', (pitch*10) + 5)
    # else:
    #     sender.send_message('/play_snack', (pitch*5) + 10)

    sender = udp_client.SimpleUDPClient('127.0.0.1', 4560)
    # get object label
    index = random.randint(0,7)
    #pitch = random.randint(60,90)
    # get object color and map to notes
    if object_list[index] == 'banana':
        sender.send_message('/play_this',1)
    elif object_list[index] == 'apple':
        sender.send_message('/play_this',2)
    elif object_list[index] == 'orange':
        sender.send_message('/play_this',3)
    elif object_list[index] == 'broccoli':
        sender.send_message('/play_this',4)
    elif object_list[index] == 'carrot':
        sender.send_message('/play_this',5)
    elif object_list[index] == 'donut':
        sender.send_message('/play_this',6)
    elif object_list[index] == 'cake':
        sender.send_message('/play_this',7)
    else:
        sender.send_message('/play_this',8)
        
    sleep(0.5)
