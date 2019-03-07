 
 
'''
    this will contain the reference to the MQTT client library (Eclipse Paho).
    You will need to create this on your own,
    including the required call-backs for handling a message received, disconnect, and connection
failure.
'''
 
 
 
'''
    Created on 09-Feb-2019
    @author: Adhira
'''
import random 
from sense_hat import SenseHat
from time import sleep
from threading import Thread
from labs.common import SensorData
from labs.module02 import SmtpClientConnector
from labs.module05 import TempActuatorEmulator
import labs.common.ConfigConst as configconst
from labs.common import ConfigUtil
from labs.common import ActuatorData
 
 
def on_connect(mosq, obj, rc):
    print("Result Code: " + str(rc))

def on_message(client, userdata, msg):
    topic=msg.topic
    m_decode=str(msg.payload.decode("utf-8","ignore"))
    print("data Received type",type(m_decode))
    print("data Received",m_decode)
    print("Converting from Json to Object")
    m_in=json.loads(m_decode)
    print(type(m_in))
    print("broker 2 address = ",m_in["broker2"])

def on_publish(mosq, obj, mid):
    print("mid: " + str(mid))

def on_subscribe(mosq, obj, mid, granted_qos):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))

def on_log(mosq, obj, level, string):
    print(string)
# import json
'''
    Instantiate the data
'''
sensor = SensorData.SensorData()
actuator = ActuatorData.ActuatorData()
sen = SmtpClientConnector.SmtpClientConnector()
temp_actuator = TempActuatorEmulator.TempActuatorEmulator()
 
'''
    Define thread
'''
class TempSensorAdaptor(Thread):
     
    def __init__(self):      
        Thread.__init__(self)
        self.enableEmulator = True                                                                  # Turn the emulator ON
        self.sensor = SensorData.SensorData()                                                       # Obtain sensor data
        self.actuator = ActuatorData.ActuatorData()                                                 # Obtain actuator data
        self.alertDiff = 5                                                                          # Set time for obtaining values from sensor
        self.rateInSec = 5                                                                          # Import configurations
        self.config = ConfigUtil.ConfigUtil('../../../config/ConnectedDevicesConfig.props')
        self.mqttc = mqtt.Client()
    # Assign event callbacks
        self.mqttc.on_message = on_message
        self.mqttc.on_connect = on_connect
        self.mqttc.on_publish = on_publish
        self.mqttc.on_subscribe = on_subscribe
        # Connect
#         self.mqttc
        self.mqttc.connect("iot.eclipse.org")
        self.mqttc.loop_start()
        
        time.sleep(3)
        print("sending data")
 
    """ Implement thread
    @summary: 
    1. Get temperature information from sensor
    2. Parse and store the value in sensor data file
    3. Perform operations for alerting
    4. Switch actuator
    5. Call process message method to store values in actuator data
    """
    def run(self):                                                                                  
        while True:
            if self.enableEmulator:
                
                ''' Obtain temperature from SenseHat '''
                
                sense = SenseHat()
                temp = sense.get_temperature()
                
                '''
                Parse sensor data content
                Generate and store value in sensor data file for the current temperature
                '''
                
                self.sensor.curValue = random.uniform(float(self.sensor.getMinValue()), float(self.sensor.getMaxValue()))
                self.sensor.addValue(self.sensor.curValue)
                
                ''' Obtain difference in temperature '''
                
                temp_diff = temp - self.sensor.getValue()
                
                ''' Indicate temperature increase or decrease '''
                
                nominal = int(self.config.getProperty(configconst.CONSTRAINED_DEVICE, configconst.NOMINAL_TEMP_KEY))
                print('\n--------------------')
                print('New temperature is generating:')
                print('  ' + str(self.sensor))
                if(abs(temp_diff) >= self.alertDiff):
                    print('\n  Oops...Current temp exceeds average by > ' + str(self.alertDiff) + '. Sending notification...')
                    
                    '''
                    Publish message to console
                    '''
                    
#                     sen.publishMessage('This is the updated sensor information', self.sensor)
                    
                '''
                Save in JSon file                
                '''
                senData = self.sensor.toJSon()
                self.sensor.fromJSon(senData)
#                 sen.publishMessage('JSon data: \n', self.sensor)
                
                '''
                Send json object to email
                '''
                sen.publishMessage("JSon file:",senData)
                
                '''
                Write JSON to file
                '''
                f = open( 'SensorDataFile.json', 'w' )
                f.write( 'Sensor data:\n' + senData + '\n' )
                f.close()

                '''
                Actuator data - to json
                '''
                actData = self.actuator.tojson()
                self.actuator.fromjson(actData)
#                 sen.publishMessage("ActData", self.actuator)
              
                '''
                Actuator data
                '''
                if(self.sensor.getValue()!=nominal):
                    diff_val = self.sensor.getValue() - nominal
                    self.actuator.setValue(str(diff_val))
                    
                    ''' 
                        Switch for actuator data
                        Send commands for indicating temperature difference
                        Process message for displaying info
                    '''
                    
                    if diff_val > 0:
                        self.actuator.setCommand(1)
                    else:
                        self.actuator.setCommand(0)
                    print('I will show something on the Sense Hat, are you ready?')
                    
                    ''' Invoke process message method to store value in actuator data'''
                    
                    temp_actuator.processMessage(actuator)

            print('Please wait for ')
            sleep(self.rateInSec)
            
             
  









    def Publish(self, topic):
        
        self.mqttc.publish(topic=topic, payload=self.sensor.senData,qos=2)
        
    def Subscribe(self,topic):
        self.mqttc.subscribe(topic=topic, qos=2)
        print(self.sensor.fromJSon(self.sensor.senData))
        
    def Disconnect(self):
        time.sleep(10)
        self.mqttc.loop_stop()
        self.mqttc.disconnect()


##################### Client connector #################



'''
Created on 06-Mar-2019

@author: Adhira
'''
import json
import time
import paho.mqtt.client as mqtt
message = 'My message'

# class MqttClientConnector():
    


# def on_connect(mosq, obj, rc):
#     print("Result Code: " + str(rc))
# 
# def on_message(client, userdata, msg):
#     topic=msg.topic
#     m_decode=str(msg.payload.decode("utf-8","ignore"))
#     print("data Received type",type(m_decode))
#     print("data Received",m_decode)
#     print("Converting from Json to Object")
#     m_in=json.loads(m_decode)
#     print(type(m_in))
#     print("broker 2 address = ",m_in["broker2"])
# 
# def on_publish(mosq, obj, mid):
#     print("mid: " + str(mid))
# 
# def on_subscribe(mosq, obj, mid, granted_qos):
#     print("Subscribed: " + str(mid) + " " + str(granted_qos))
# 
# def on_log(mosq, obj, level, string):
#     print(string)
# 
# 
# 
# class MqttClientConnector():
#     def __init__(self):
#         self.mqttc = mqtt.Client()
#     # Assign event callbacks
#         self.mqttc.on_message = on_message
#         self.mqttc.on_connect = on_connect
#         self.mqttc.on_publish = on_publish
#         self.mqttc.on_subscribe = on_subscribe
#         # Connect
# #         self.mqttc
#         self.mqttc.connect("iot.eclipse.org")
#         self.mqttc.loop_start()
#         
#         time.sleep(3)
#         print("sending data")
#         
# #         return self.mqttc
#     def Publish(self, topic, message):
#         
#         self.mqttc.publish(topic=topic, payload=message,qos=2)
#         
#     def Subscribe(self,topic):
#         self.mqttc.subscribe(topic=topic, qos=2)
#         
#     def Disconnect(self):
#         time.sleep(10)
#         self.mqttc.loop_stop()
#         self.mqttc.disconnect()

