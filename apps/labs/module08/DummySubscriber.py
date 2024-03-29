'''
Created on 18-Apr-2019

@author: Adhira
'''
import random
from IPython.core import payload
from labs.module07.CoapClientConnector import client
from paho.mqtt.subscribe import _on_message_simple

'''
Sends data to Ubidots using MQTT over TLS

Example provided by Jose Garcia @Ubidots Developer
'''

import paho.mqtt.client as mqttClient
import time
import json
import ssl

'''
global variables
'''

connected = False  # Stores the connection status
BROKER_ENDPOINT = "things.ubidots.com"
TLS_PORT = 8883  # Secure port
MQTT_USERNAME = "A1E-oIBRNfbQ3Soe81cuUBmR10PozvY5co"  # Put here your Ubidots TOKEN
MQTT_PASSWORD = ""  # Leave this in blank
TOPIC = "/v1.6/devices/"
DEVICE_LABEL = "HomeAutomation"
TLS_CERT_PATH = "/Users/Adhira/Desktop/pythonFiles/industrial.pem"  # Put here the path of your TLS cert

'''
Functions to process incoming and outgoing streaming
'''

def on_connect(client, userdata, flags, rc):
    if rc == 0:

        print("[INFO] Connected to broker")
        global connected  # Use global variable
        connected = True  # Signal connection
    else:
        print("[INFO] Error, connection failed")


def on_subscribe(client, userdata, mid, granted_qos):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))

def on_message(client, userdata, msg):
    d = json.loads(msg.payload)
#   print("Message received on topic "+msg.topic+" with QoS "+str(msg.qos)+" and payload "+msg.payload)
    client.send(msg.topic, [d])
    
   
def connect(mqtt_client, mqtt_username, mqtt_password, broker_endpoint, port):
    global connected

    if not connected:
        mqtt_client.username_pw_set(mqtt_username, password=mqtt_password)
        mqtt_client.on_connect = on_connect
        
        mqtt_client.on_subscribe = on_subscribe
        mqtt_client.on_message = on_message
        mqtt_client.tls_set(ca_certs=TLS_CERT_PATH, certfile=None,
                            keyfile=None, cert_reqs=ssl.CERT_REQUIRED,
                            tls_version=ssl.PROTOCOL_TLSv1_2, ciphers=None)
        mqtt_client.tls_insecure_set(False)
        mqtt_client.connect(broker_endpoint, port=port)
        mqtt_client.loop_start()

        attempts = 0

        while not connected and attempts < 5:  # Wait for connection
            print(connected)
            print("Attempting to connect...")
            time.sleep(1)
            attempts += 1

    if not connected:
        print("[ERROR] Could not connect to broker")
        return False

    return True


def subscribe(mqtt_client, topic):

    try:
        mqtt_client.subscribe(topic)

    except Exception as e:
        print("[ERROR] Could not subscribe data, error: {}".format(e))

def message(mqtt_client,topic):
    try:
        mqtt_client.message(topic)
    except Exception as e:
        print("[ERROR] Could not subscribe data, error: {}".format(e))
   
def main():
    
    topic = "{}{}".format(TOPIC, DEVICE_LABEL)

    mqtt_client = mqttClient.Client()
    
    while True:
#         payload = json.loads("Humidity")
        if not connect(mqtt_client, MQTT_USERNAME,
                       MQTT_PASSWORD, BROKER_ENDPOINT, TLS_PORT):
            return False
        
        msg = subscribe(mqtt_client, topic)
#         msg = message(mqtt_client, topic)
        print("Message is:", msg)
        time.sleep(10)
    return True
    


if __name__ == '__main__':
    while True:
        main()
        time.sleep(10)
