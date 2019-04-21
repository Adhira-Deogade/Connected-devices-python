'''
Created on 18-Apr-2019

@author: Adhira
'''


'''
Sends data to Ubidots using MQTT over TLS

Example provided by Jose Garcia @Ubidots Developer
'''
import sys
sys.path.insert(0,'/home/pi/workspace/iot-device/connected-devices-python/apps')
import random
import paho.mqtt.client as mqttClient
import time
import json
import ssl
from labs.module02 import SmtpClientConnector
from sense_hat import SenseHat
import pygame
pygame.mixer.init()
pygame.mixer.music.load("song.mp3")
from labs.common import SensorData
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
TLS_CERT_PATH = "/home/pi/workspace/iot-device/connected-devices-python/apps/labs/module08/industrial.pem"  # Put here the path of your TLS cert
sen = SmtpClientConnector.SmtpClientConnector()
red = (255,0,0)
sensor = SensorData.SensorData()
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


def on_publish(client, userdata, result):
    print("Published!")


def connect(mqtt_client, mqtt_username, mqtt_password, broker_endpoint, port):
    global connected

    if not connected:
        mqtt_client.username_pw_set(mqtt_username, password=mqtt_password)
        mqtt_client.on_connect = on_connect
        mqtt_client.on_publish = on_publish
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


def publish(mqtt_client, topic, payload):

    try:
        mqtt_client.publish(topic, payload)

    except Exception as e:
        print("[ERROR] Could not publish data, error: {}".format(e))


def main():
    
    topic = "{}{}".format(TOPIC, DEVICE_LABEL)

    mqtt_client = mqttClient.Client()
    
    while True:
        sense = SenseHat()
        acceleration = sense.get_accelerometer_raw()
        tempData = sense.get_temperature()
        humidData = sense.get_humidity()
        pressureData = sense.get_pressure()
        
        x1 = acceleration['x']
        y1 = acceleration['y']
        z1 = acceleration['z']
     
        x = abs(x1)
        y = abs(y1)
        z = abs(z1)
        sensor.addValue(tempData, pressureData, humidData)
        print("Sending sensor data...")
        sen.publishMessage("Updated sensor information", sensor)
        print("Temperature - ", tempData, "Pressure - ", pressureData, "Humidity - ", humidData)
        if x > 1 or y > 1 or z > 1:
            sense.show_letter("!", red)
            print("Sending notification...")
            sen.publishMessage("Alert", "Intruder Detected")
            print("Message sent.!")
        pygame.mixer.music.play()
        time.sleep(10)
        pygame.mixer.music.pause()
    #while pygame.mixer.music.get_busy() == True:
    #continue
        #else:
            #break
        payload = json.dumps({"Temperature": tempData,
                              "Pressure":pressureData,
                              "Humidity":humidData,
                "acc_x":x, "acc_y":y, "acc_z":z})
        if not connect(mqtt_client, MQTT_USERNAME,
                       MQTT_PASSWORD, BROKER_ENDPOINT, TLS_PORT):
            return False
        publish(mqtt_client, topic, payload)
        time.sleep(5)
    sense.clear()
    return True
    


if __name__ == '__main__':
    while True:
        main()
        time.sleep(5)
