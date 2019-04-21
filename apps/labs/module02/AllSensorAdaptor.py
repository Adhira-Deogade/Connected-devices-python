'''
Created on 13-Apr-2019

@author: Adhira
'''
import sys
sys.path.insert(0,'/home/pi/workspace/iot-device/connected-devices-python/apps')
import random 
from sense_hat import SenseHat
from time import sleep
from threading import Thread
from labs.common import SensorData
from labs.module02 import SmtpClientConnector
from labs.module03 import TempActuatorEmulator
import labs.common.ConfigConst as configconst
from labs.common import ConfigUtil
from labs.common import ActuatorData
from awscli.customizations.emr.constants import TRUE


sen = SmtpClientConnector.SmtpClientConnector()


# red = (255, 0, 0)
blue = (255,0,0)

    

class allSensorAdaptor(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.flag = True
        self.rateInSec=5
        
    def run(self):
        while True:
            if self.flag==True:
                sense = SenseHat()
                acceleration = sense.get_accelerometer_raw()
                tempData = sense.get_temperature()
                humidData = sense.get_humidity()
                pressureData = sense.get_pressure()
                
                x = acceleration['x']
                y = acceleration['y']
                z = acceleration['z']
             
                x = abs(x)
                y = abs(y)
                z = abs(z)
                
                print("Temperature - ", tempData, "Pressure - ", pressureData, "Humidity - ", humidData)
                if x > 1 or y > 1 or z > 1:
                    sense.show_letter("!", blue)
                    print("Sending notification...")
                    sen.publishMessage("Alert", humidData)
                    print("Message sent.!")
                else:
                    sense.clear()
            print('Please wait for ')
            sleep(self.rateInSec)