from pyA20.gpio import gpio
from pyA20.gpio import port

#import RPi.GPIO as GPIO
import dht22
import time
import datetime
import paho.mqtt.publish as publish
import os

# initialize GPIO
#gpio.setwarnings(False)
#gpio.setmode(GPIO.BCM)
PIN2 = port.PA6
gpio.init()
#gpio.cleanup()

# read data using pin 14
instance = dht22.DHT22(pin=PIN2)

TEMP = 0
HUM = 0

def pub (topic, val):
     publish.single("orangepipc2/"+topic, val, client_id="OrangPI", hostname="192.168.0.104", auth={'username':"hassio",'password':"LF78RLL4FL9"})

def readDHT22 ():
    while True:
        result = instance.read()
        if result.is_valid():
            TEMP1 = ("%.2f" % result.temperature)
            HUM1 = ("%.2f" % result.humidity)
            return TEMP1, HUM1
        time.sleep(1)

while True:

    val = readDHT22()
    TEMP1 = val[0]
    HUM1 = val[1]
    if TEMP1 != TEMP:
        TEMP = TEMP1
       # print(TEMP)
        pub("TEMP", TEMP)
    if HUM1 != HUM:
        HUM = HUM1
       # print(HUM)
        pub("HUM", HUM)
    time.sleep(120)
