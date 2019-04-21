'''
Created on 20-Apr-2019

@author: Adhira
'''

import sys,os
sys.path.insert(0,'/home/pi/workspace/iot-device/connected-devices-python/apps')
import paho.mqtt.client as mqtt
from sense_hat import SenseHat
sense = SenseHat()

BROKER_ENDPOINT = "things.ubidots.com"
PORT = 1883
MQTT_USERNAME = "A1E-oIBRNfbQ3Soe81cuUBmR10PozvY5co"  # Put here your TOKEN
MQTT_PASSWORD = ""
TOPIC = "/v1.6/devices"
DEVICE_LABEL = "homeautomation"
VARIABLE_LABEL1 = "averagetemperature"
VARIABLE_LABEL2 = "temperature"
red = (255,0,0)

def on_connect(mqttc, obj, flags, rc):
    print("[INFO] Connected!")
    topic1 = "{}/{}/{}/lv".format(TOPIC, DEVICE_LABEL, VARIABLE_LABEL1)
    topic2 = "{}/{}/{}/lv".format(TOPIC, DEVICE_LABEL, VARIABLE_LABEL2)
    print(topic1)
    print(topic2)
    mqttc.subscribe((topic1,0),(topic2,0))

def on_message(mqttc, obj, msg):
    myMsg = float(msg.payload)
    print("[INFO] value received: {}".format(myMsg))
    if myMsg>35:
        sense.show_message( "High", text_colour=red)
    else:
        sense.show_message( "Medium", text_colour=red)
    sense.clear()


def on_publish(mqttc, obj, mid):
    print("[INFO] Published!")


def on_subscribe(mqttc, obj, mid, granted_qos):
    print("[INFO] Subscribed!")


def on_log(mqttc, obj, level, string):
    print("[INFO] Log info: {}".format(string))

def main():
    # Setup MQTT client
    mqttc = mqtt.Client()
    mqttc.username_pw_set(MQTT_USERNAME, password="")
    mqttc.on_message = on_message
    mqttc.on_connect = on_connect
    mqttc.on_publish = on_publish
    mqttc.on_subscribe = on_subscribe

    # Uncomment to enable debug messages
    # mqttc.on_log = on_log

    mqttc.connect(BROKER_ENDPOINT, PORT, 60)
    topic1 = "{}/{}/{}/lv".format(TOPIC, DEVICE_LABEL, VARIABLE_LABEL1)
    print(topic1)
    topic2 = "{}/{}/{}/lv".format(TOPIC, DEVICE_LABEL, VARIABLE_LABEL2)
    print(topic2)

    #mqttc.subscribe([topic1,topic2], [0,0])
    mqttc.subscribe((topic1,0),(topic2,0))


    mqttc.loop_forever()

if __name__ == '__main__':
    main()