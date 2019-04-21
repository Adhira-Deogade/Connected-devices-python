'''
Created on 20-Apr-2019

@author: Adhira
'''
'''
Change address to Rpi module directory
'''
import sys,os
sys.path.insert(0,'/home/pi/workspace/iot-device/connected-devices-python/apps')
import paho.mqtt.client as mqtt
from sense_hat import SenseHat

''' Create sense hat object '''
sense = SenseHat()

''' Variables '''
BROKER_ENDPOINT = "things.ubidots.com"
PORT = 1883
MQTT_USERNAME = "A1E-oIBRNfbQ3Soe81cuUBmR10PozvY5co"  # Put here your TOKEN
MQTT_PASSWORD = ""
TOPIC = "/v1.6/devices"
DEVICE_LABEL = "homeautomation"
VARIABLE_LABEL1 = "averagetemperature"
VARIABLE_LABEL2 = "temperature"
red = (255,0,0)

'''
Functions to process incoming and outgoing streaming
'''
'''
    @summary: Handling connection callback
    @param mqttc: Specify the client to be connected
    @param obj: Specifying the user data/topic
    @param flags, rc: Flag and return code 
'''
def on_connect(mqttc, obj, flags, rc):
    print("[INFO] Connected!")
    topic1 = "{}/{}/{}/lv".format(TOPIC, DEVICE_LABEL, VARIABLE_LABEL1)
    topic2 = "{}/{}/{}/lv".format(TOPIC, DEVICE_LABEL, VARIABLE_LABEL2)
    print(topic1)
    print(topic2)
    mqttc.subscribe((topic1,0),(topic2,0))

'''
    @summary: Obtain data from cloud as message, call sensehat object and display the information
    @param mqttc: Specify the client to be connected
    @param obj: Specifying the user data/topic
    @param msg: Define the message 
'''
def on_message(mqttc, obj, msg):
    myMsg = float(msg.payload)
    print("[INFO] value received: {}".format(myMsg))
    if myMsg>35:
        sense.show_message( "High", text_colour=red)
    else:
        sense.show_message( "Medium", text_colour=red)
    sense.clear()

'''
    @summary: Handling publishing callback
    @param mqttc: Specify the client to be connected
    @param obj: Specifying the user data/topic
    @param mid: Specifying message id 
'''
def on_publish(mqttc, obj, mid):
    print("[INFO] Published!")

'''
    @summary: Handling subscription callback
    @param mqttc: Specify the client to be connected
    @param obj: Specifying the user data/topic
    @param granted_qos: specifying quality of service 
'''
def on_subscribe(mqttc, obj, mid, granted_qos):
    print("[INFO] Subscribed!")

'''
    @summary: Handling log callback
    @param mqttc: Specify the client to be connected
    @param obj: Specifying the user data/topic
    @param String: Specifying the string to be displayed in log message 
'''
def on_log(mqttc, obj, level, string):
    print("[INFO] Log info: {}".format(string))

'''
    @summary: Main function to connect to broker, publish and subscribe to specified topics.
              Perform this continuously in a loop.
              Subscribing and obtaining data from 2 topics
'''
def main():
    # Setup MQTT client
    mqttc = mqtt.Client()
    mqttc.username_pw_set(MQTT_USERNAME, password="")
    mqttc.on_message = on_message
    mqttc.on_connect = on_connect
    mqttc.on_publish = on_publish
    mqttc.on_subscribe = on_subscribe

    mqttc.connect(BROKER_ENDPOINT, PORT, 60)
    topic1 = "{}/{}/{}/lv".format(TOPIC, DEVICE_LABEL, VARIABLE_LABEL1)
    print(topic1)
    topic2 = "{}/{}/{}/lv".format(TOPIC, DEVICE_LABEL, VARIABLE_LABEL2)
    print(topic2)

    mqttc.subscribe((topic1,0),(topic2,0))
    mqttc.loop_forever()

if __name__ == '__main__':
    main()