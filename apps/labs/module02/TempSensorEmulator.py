'''
Created on 02-Feb-2019

@author: Adhira
'''

# Import libraries
import random 
from time import sleep
from threading import Thread
from labs.common import SensorData
from labs.module02 import SmtpClientConnector
from test.test_enum import threading

## Define thread class
class module02(threading.Thread):

    # Define variables
    
    def __init__(self):
        super(module02,self).__init__()
    
        # Turn Emulator ON
        self.enableEmulator = True
        
        # Obtain Sensor data from file
        # Initialize object of sensor data
        self.sensor = SensorData.SensorData()
        
        # Define alert parameter and rate of obtaining data
        self.alertDiff = 5
        self.rateInSec = 5
        
    """
    Initialize the temperature information using object in sensor data and operate them
    Then define the output format. Finally use the object of SmtpClientConnector to publish 
    the whole information about temperature.
    """
    
    def run(self):
        while True:
            if self.enableEmulator:
                
                # Generate random value of current temperature between max and min values from Sensor data file
                self.sensor.curValue = random.uniform(float(self.sensor.getMinValue()), float(self.sensor.getMaxValue()))
                
                # Add the generated temperature value in the sensor data file
                self.sensor.addValue(self.sensor.curValue)
                
                # Generate readable output
                print('\n--------------------')
                print('New temperature is generating:')
                print('  ' + str(self.sensor))
                
                k = abs(self.sensor.curValue - self.sensor.getAvgValue())
                
                # Condition for sending message
                if (k >= self.alertDiff):
                    
                    # Initialize object of SmtpClientConnector to publish the message 
                    sen = SmtpClientConnector.SmtpClientConnector()
                    print('\n  Oops...Current temperature exceeds average by > ' + str(k) + '. Sending notification...')
                    sen.publishMessage('This is the updated sensor information', self.sensor)
                    
            sleep(self.rateInSec)
            
            
    
