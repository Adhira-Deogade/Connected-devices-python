##################### Client connector #################




'''
Created on 06-Mar-2019

@author: HaoZhou
'''
import json
import time
import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish
from asyncio.tasks import sleep
message = 'My message'   


def on_connect(mosq, obj, rc):
    print("Connected with client with result Code: " + str(rc))

def on_message(client, userdata, msg):
    global json_data
#     topic=msg.topic
    m_decode=str(msg.payload.decode("utf-8","ignore"))
#     print("data Received type",type(m_decode))
#     print("data Received",m_decode)
#     print("Converting from Json to Object")
#     m_in=json.loads(m_decode)
#     print(type(m_in))
#     print("broker 2 address = ",m_in["broker2"])
    
    json_data = m_decode
    client.loop_stop()

def on_publish(mosq, obj, mid):
    print("Published with mid: " + str(mid))

#def on_subscribe(mosq, obj, mid, granted_qos):
#   print("Subscribed: " + str(mid) + " " + str(granted_qos))

def on_log(mosq, obj, level, string):
    print(string)




class MqttClientConnector():
    host = "test.mosquitto.org"
    json_data = "Hello"
    
    def on_connect(self,client,userdata,flags,rc):
        print("Connected with Client: "+str(rc))
        client.subscribe(self.topic,2)
    
    def on_message(self,client,userdata,msg):
        global json_data
        json_data = str(msg.payload.decode("utf-8"))
        client.loop_stop()

    def __init__(self,topic=None):
        self.topic = topic;
        self.client = mqtt.Client()
        
    def Publish(self,topic,message,host):
        #client = mqtt.Client();
        self.client.connect(host,1883)
        self.client.publish(topic,message)
        
    def subscribe(self,host):
        #client = mqtt.Client()
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.client.connect(host,1883,60)
        self.client.loop_start()
        time.sleep(10)
        
    def Disconnect(self):
        time.sleep(10)
        self.client.loop_stop()
        self.client.disconnect()
        print("Client Disconnected!!")
        
    def message(self):
        global json_data
        return json_data
