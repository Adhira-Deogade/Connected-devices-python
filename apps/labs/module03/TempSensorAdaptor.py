

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
from labs.module03 import TempActuatorEmulator
import labs.common.ConfigConst as configconst
from labs.common import ConfigUtil
from labs.common import ActuatorData


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
                    sen.publishMessage('This is the updated sensor information', self.sensor)
                if(self.sensor.getValue()!=nominal):
                    diff_val = self.sensor.getValue() - nominal
                    self.actuator.setValue(str(diff_val))
                    
                    ''' 
                        Switch for actuator data
                        Send commands for indicating temperature difference to process message for displaying info
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
            