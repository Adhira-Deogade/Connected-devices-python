


'''
    This will connect to the MQTT broker using MqttClientConnector,
    subscribe to the ‘test’ topic, and wait for at least 65
    seconds.
'''


'''
    Created on 09-Feb-2019
    @author: Adhira
'''
from time import sleep
from labs.module06 import MqttClientConnector

'''
    Construct objects
'''
connector = MqttClientConnector.TempSensorAdaptor()
connector.daemon = True
print("Starting system performance application daemon thread...")

'''
    Run thread
'''

    
# import paho.mqtt.client as mqtt
import time
# import json
# brokers_out={"broker1":"192.168.1.206",
#          "broker2":"test.mosquitto.org",
#          "broker3":"iot.eclipse.org"
#          }
# print(brokers_out)
# print("brokers_out is a ",type(brokers_out))
# print("broker 1 address = ",brokers_out["broker1"])
# data_out=json.dumps(brokers_out)# encode oject to JSON
# print("\nConverting to JSON\n")
# print ("data -type ",type(data_out))
# print ("data out =",data_out)
# #At Receiver
# print("\nReceived Data\n")
# data_in=data_out
# print ("\ndata in-type ",type(data_in))
# print ("data in=",data_in)
# brokers_in=json.loads(data_in) #convert incoming JSON to object
# print("brokers_in is a ",type(brokers_in))
# print("\n\nbroker 2 address = ",brokers_in["broker2"])
cont=input("enter to Continue")
#########
###########


topic="test/json_test"

print("Connecting to broker client 1 ")

connector.Subscribe(topic)
time.sleep(3)
print("Ready for receiving data")
time.sleep(15)
connector.Disconnect()

