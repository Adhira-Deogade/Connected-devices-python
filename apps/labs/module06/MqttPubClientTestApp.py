# from time import sleep
from labs.module06.MqttClientConnector import MqttClientConnector

# import paho.mqtt.client as mqtt
import time
# import json
import random
import logging
from datetime import datetime

from labs.common import ConfigUtil
from labs.common import ConfigConst
# from labs.common import ActuatorData
from labs.common import SensorData

'''
    Setting values for Topic and address for MQTT broker
'''
topic = "Temperature Sensor"
config = ConfigUtil.ConfigUtil('../../../config/ConnectedDevicesConfig.props')
host = config.getProperty(ConfigConst.MQTT_GATEWAY_SECTION, ConfigConst.HOST_KEY)

'''
    Creating sensor data
'''
sensor = SensorData.SensorData()
sensor.curVal = random.uniform(float(sensor.getMinValue()), float(sensor.getMaxValue())); 
sensor.addValue(sensor.curVal);
sensor.diffVal = sensor.curVal - sensor.avgValue;
sensor.timestamp = datetime.now();
logging.info('SensorData to be sent:')
print("Sensor Value before converting to Json: "+str(sensor));

'''
Converting SensorData to json format
'''
# data = DataUtil()
json_data = sensor.toJSon();
logging.info('SensorData converted into Json:')
print("SensorData in Json Format before publishing\n"+str(json_data)+"\n")

# pub_client = MqttClientConnector();


'''
    Construct objects
'''
connector = MqttClientConnector()
connector.daemon = True
print("Starting system performance application daemon thread...")

'''
    Run thread
'''
brokers_out={"broker2":"test.mosquitto.org"}
print(brokers_out)
print("brokers_out is a ",type(brokers_out))
print("broker 2 address = ",brokers_out["broker2"])


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
# cont=input("enter to Continue")



print("Connecting to broker client 1 ",brokers_out["broker2"])
# topic="test/json_test"

print("Connecting to broker ",brokers_out["broker2"])

time.sleep(3)
print("sending data")
connector.Publish(topic, json_data, host)
time.sleep(15)
connector.Disconnect()