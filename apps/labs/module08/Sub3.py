'''
Created on 19-Apr-2019

@author: Adhira
'''
'''
This Example sends harcoded data to Ubidots using the Paho MQTT
library.

Please install the library using pip install paho-mqtt

Made by Jose García @https://github.com/jotathebest/
Adapted from the original Paho Subscribe example at
https://github.com/eclipse/paho.mqtt.python/blob/master/examples/client_sub.py
'''

import paho.mqtt.client as mqtt
import ssl

BROKER_ENDPOINT = "things.ubidots.com"
PORT = 1883
MQTT_USERNAME = "A1E-oIBRNfbQ3Soe81cuUBmR10PozvY5co"  # Put here your TOKEN
MQTT_PASSWORD = ""
TOPIC = "/v1.6/devices"
DEVICE_LABEL = "HomeAutomation"
VARIABLE_LABEL = "Temperature"
TLS_CERT_PATH = "/Users/Adhira/Desktop/pythonFiles/industrial.pem"  # Put here the path of your TLS cert

def on_connect(mqttc, obj, flags, rc):
    print("[INFO] Connected!")
    topic = "{}/{}/{}/lv".format(TOPIC, DEVICE_LABEL, VARIABLE_LABEL)
    print(topic)
    
    

def on_message(mqttc, obj, msg):
    print("received message =",str(msg.payload.decode("utf-8")))


def on_publish(mqttc, obj, mid):
    print("[INFO] Published!")


def on_subscribe(mqttc, obj, mid, granted_qos):
    print("[INFO] Subscribed!")
    
### TEMPERATURE
def on_message_temp(mosq, obj, msg):
    print(str(msg.payload)[0:4]+chr(223)+"C")

def on_log(mqttc, obj, level, string):
    print("[INFO] Log info: {}".format(string))

def main():
    # Setup MQTT client
    
    mqttc = mqtt.Client()
    mqttc.username_pw_set(MQTT_USERNAME, password="")
   
#     mqttc.message_callback_add('iDomus/RPiS/Rel1/Read', on_message_temp)
    mqttc.on_message = on_message
    mqttc.on_connect = on_connect
#     mqttc.tls_set(TLS_CERT_PATH, tls_version=ssl.PROTOCOL_TLSv1_2)
#     mqttc.tls_insecure_set(True)
    mqttc.on_subscribe = on_subscribe
    
    mqttc.on_log = on_log
    mqttc.connect(BROKER_ENDPOINT, PORT, 60)
    topic = "{}/{}/{}/lv".format(TOPIC, DEVICE_LABEL, VARIABLE_LABEL)
    print(topic)    
    
    mqttc.on_message
    mqttc.subscribe(topic, 0)
    mqttc.on_message
    
    mqttc.loop_forever()

if __name__ == '__main__':
    main()