'''
    This will connect to the MQTT broker using MqttClientConnector,
    subscribe to the ‘test’ topic, and wait for at least 65
    seconds.
'''
# from psutil import msg
'''
    Created on 09-Feb-2019
    @author: HaoZhou
'''
from time import sleep
from labs.module06.MqttClientConnector import MqttClientConnector
from labs.common.ConfigUtil import ConfigUtil
from labs.common import ConfigConst
from labs.common import ActuatorData
from labs.common import SensorData

import paho.mqtt.client as mqtt
import time
import json
import logging
# topic="test/json_test"
'''
    Setting values for Topic and address for MQTT broker
'''
topic = "Temperature Sensor"
config = ConfigUtil('../../../config/ConnectedDevicesConfig.props');
host = config.getProperty(ConfigConst.MQTT_GATEWAY_SECTION, ConfigConst.HOST_KEY)


'''

'''


'''
    Construct objects
'''
connector = MqttClientConnector(topic)
connector.daemon = True
print("Starting system performance application daemon thread...")


### Create an object for sensor data
##  call the function 
## PAss JSon data into the function

connector.subscribe(host)
time.sleep(3)
print("Ready for receiving data")

msg =connector.message()  

logging.debug('JSon Data Received:')
print("Json Data Received:\n "+str(msg)+"\n")

''' 
    Run thread
'''
# 
# brokers_out={"broker2":"test.mosquitto.org"}
# print(brokers_out)
# print("brokers_out is a ",type(brokers_out))
# print("broker 1 address = ",brokers_out["broker2"])
# data_out=json.dumps(brokers_out)# encode object to JSON
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
# cont=input("enter to Continue")
#########
###########
'''
    Sensor data instance
'''

sensor = SensorData.SensorData()
actuator = ActuatorData.ActuatorData()

senData = sensor.fromJSon(msg)
'''
Save in JSon file                
'''



logging.debug('Json data converted into SensorData')
print("Received message in SensorData format"+ str(senData))

# json = senData.to(sensor)
# logging.debug('SensorData converted into Json Data: ')
# print('SensorData converted to Json Data again: \n'+str(json))




# senData = sensor.toJSon()
# sensor.fromJSon(msg)



# print("Connecting to broker client 1 ",brokers_out["broker2"])




time.sleep(15)
connector.Disconnect()