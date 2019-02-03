import random 
from sense_hat import SenseHat
from time import sleep
from threading import Thread
from labs.common import SensorData
from labs.module02 import SmtpClientConnector

class TempSensorAdaptor(Thread):
    

    """
    Defined many variables I will need in the run method. 
    Initialize the object of SensorData to have access the temperature.
    """
    

    def __init__(self):      
        Thread.__init__(self)
        self.enableEmulator = True
        self.sensor = SensorData.SensorData()
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
                self.sensor.curValue = random.uniform(float(self.sensor.getMinValue()), float(self.sensor.getMaxValue()))
                self.sensor.addValue(self.sensor.curValue)
                

                

                

                

                print('\n--------------------')
                print('New temperature is generating:')
                print('  ' + str(self.sensor))
                if (abs(self.sensor.curValue - self.sensor.getAvgValue()) >= self.alertDiff):
                    sen = SmtpClientConnector.SmtpClientConnector()
                    print('\n  Oops...Current temp exceeds average by > ' + str(self.alertDiff) + '. Sending notification...')
                    sen.publishMessage('This is the updated sensor information', self.sensor)
                    

                #self.connector.publishMessage('Exceptional sensor data [test]', self.sensor)
            sleep(self.rateInSec)
            

            

            

