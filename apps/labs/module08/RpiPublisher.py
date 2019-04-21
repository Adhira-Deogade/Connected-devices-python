'''
>>>>>>> 4eaf05aa0d6bc70bd0ebf64f5183eb090e28f527
Created on 18-Apr-2019

@author: Adhira
'''
'''
Sends data to Ubidots using MQTT over TLS

Example provided by Jose Garcia @Ubidots Developer
'''
'''
Change address to Rpi module directory
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
'''
<<<<<<< HEAD
=======
Create pygame object and inmort song for starting music as alarm
'''
import pygame
pygame.mixer.init()
pygame.mixer.music.load("song.mp3")

'''
Import sensor data object to send sensor data information to email
'''
from labs.common import SensorData

'''
>>>>>>> 4eaf05aa0d6bc70bd0ebf64f5183eb090e28f527
global variables
'''

connected = False  # Stores the connection status
BROKER_ENDPOINT = "things.ubidots.com"
TLS_PORT = 8883  # Secure port
MQTT_USERNAME = "A1E-oIBRNfbQ3Soe81cuUBmR10PozvY5co"  # Ubidots TOKEN
MQTT_PASSWORD = ""  
TOPIC = "/v1.6/devices/"
DEVICE_LABEL = "HomeAutomation"
TLS_CERT_PATH = "/home/pi/workspace/iot-device/connected-devices-python/apps/labs/module08/industrial.pem" # Path of your TLS cert
sen = SmtpClientConnector.SmtpClientConnector()
red = (255,0,0)
sensor = SensorData.SensorData()

'''
Functions to process incoming and outgoing streaming
'''
'''
    @summary: Handling connection callback
    @param client: Specify the client to be connected
    @param userdata: Specifying the user data/topic
    @param flag, rc: Flag and return code 
    @return: Connection flag as True/False  
'''
def on_connect(client, userdata, flags, rc):
    if rc == 0:

        print("[INFO] Connected to broker")
        global connected  # Use global variable
        connected = True  # Signal connection
    else:
        print("[INFO] Error, connection failed")

'''
    @summary: Handle publishing callback
    @param client: Specify the client to be connected
    @param userdata: Specifying the user data/topic 
    @return: Published as True/False  
'''
def on_publish(client, userdata, result):
    print("Published!")

'''
    @summary: Connecting to broker with certificate
    @param mqtt_client: Specify the client to be connected
    @param mqtt_username, mqtt_password Specifying user details
    @param broker_endpoint, port: specifying connection details
    @return: Connection flag as True/False  
'''
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

'''
    @summary: Publishing to broker
    @param mqtt_client: Specify the client to be connected
    @param topic: Specifying topic to be published
    @param payload: Specifying the data to be sent under the topic 
'''
def publish(mqtt_client, topic, payload):

    try:
        mqtt_client.publish(topic, payload)

    except Exception as e:
        print("[ERROR] Could not publish data, error: {}".format(e))

'''
    @summary: Main function to obtain data from sensor,create condition and send email message by calling SMTP client connector
              Creating payload and sending sensor data in json format, and publish to broker. Perform this continuously in a loop,
              Obtain fresh data by clearing the sensehat.
    @return: Success flag as True/False  
'''
def main():
    
    topic = "{}{}".format(TOPIC, DEVICE_LABEL)

    mqtt_client = mqttClient.Client()
    
    while True:
        ''' Create sense hat object'''
        sense = SenseHat()
        acceleration = sense.get_accelerometer_raw()
        tempData = sense.get_temperature()
        humidData = sense.get_humidity()
        pressureData = sense.get_pressure()
        
        ''' Obtain acceleration information'''
        x1 = acceleration['x']
        y1 = acceleration['y']
        z1 = acceleration['z']
        
        ''' Obtain absolute value to  indicate motion'''
        x = abs(x1)
        y = abs(y1)
        z = abs(z1)
        
        ''' Send data to sensor object in order to send to email'''
        sensor.addValue(tempData, pressureData, humidData)
        print("Sending sensor data...")
        sen.publishMessage("Updated sensor information", sensor)
        print("Temperature - ", tempData, "Pressure - ", pressureData, "Humidity - ", humidData)
        
        ''' Condition to  send intrusion detection information'''
        if x > 1 or y > 1 or z > 1:
            sense.show_letter("!", red)
            print("Sending notification...")
            sen.publishMessage("Alert", "Intruder Detected")
            print("Message sent.!")
            
        ''' Turn the speaker ON and start playing music'''
        pygame.mixer.music.play()
        time.sleep(10)
        pygame.mixer.music.pause()
    
        ''' Create payload by dumping sensor data information in json object and publish'''
        payload = json.dumps({"Temperature": tempData,
                              "Pressure":pressureData,
                              "Humidity":humidData,
                "acc_x":x, "acc_y":y, "acc_z":z})
        if not connect(mqtt_client, MQTT_USERNAME,
                       MQTT_PASSWORD, BROKER_ENDPOINT, TLS_PORT):
            return False
        publish(mqtt_client, topic, payload)
        time.sleep(5)
        
    ''' Clear the information from sense hat'''
    sense.clear()
    return True
    


if __name__ == '__main__':
    while True:
        main()
        time.sleep(5)
