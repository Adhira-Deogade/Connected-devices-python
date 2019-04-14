


'''
    Created on 09-Feb-2019
    @author: Adhira
'''
import smbus2
import threading
from time import sleep
from labs.common import ConfigUtil
from labs.common import ConfigConst

''' Instantiate i2c bus '''
i2cBus = smbus2.SMBus(1)                                                                     # Use I2C bus No.1 on Raspberry Pi3 +
 
'''
    Specify addresses for sensors to read data from I2C buffers
'''
enableControl = 0x2D
enableMeasure = 0x08

accelAddr = 0x1C                                                                            # address for IMU (accelerometer)
magAddr = 0x6A                                                                              # address for IMU (magnetometer)
pressAddr = 0x5C                                                                            # address for pressure sensor
humidAddr = 0x5F                                                                            # address for humidity sensor
begAddr = 0x28                                                                              # beginning address
totBytes = 6                                                                                # total bytes

DEFAULT_RATE_IN_SEC = 5


'''
    Thread class to read data from sensor
'''

class I2CSenseHatAdaptor(threading.Thread):
    rateInSec = DEFAULT_RATE_IN_SEC
    '''
        Constructor
        @summary: Load configurations
    '''
    def __init__(self):
        super(I2CSenseHatAdaptor, self).__init__()
             
        self.config = ConfigUtil.ConfigUtil(ConfigConst.DEFAULT_CONFIG_FILE_NAME)
        self.config.loadConfig()
             
        print('Configuration data...\n' + str(self.config))
        self.initI2CBus()
        
    '''
        Initialize addresses and bus
        @summary: At different sensor address, enable the buffers
    '''    
    def initI2CBus(self):
        print("Initializing I2C bus and enabling I2C addresses...")
        i2cBus.write_byte_data(accelAddr, enableControl, enableMeasure)
        i2cBus.write_byte_data(magAddr, enableControl, enableMeasure)
        i2cBus.write_byte_data(pressAddr, enableControl, enableMeasure)
        i2cBus.write_byte_data(humidAddr, enableControl, enableMeasure)
        ''' Read '''
#         self.accel = i2cBus.read_i2c_block_data(accelAddr, begAddr, totBytes)
#         self.mag = i2cBus.read_i2c_block_data(magAddr, begAddr, totBytes)
#         self.pres = i2cBus.read_i2c_block_data(pressAddr, begAddr, totBytes)
#         self.humid = i2cBus.read_i2c_block_data(humidAddr,begAddr, totBytes)
        
    '''
       Methods to display sensor data
    '''
    def displayAccelerometerData(self): 
        print('\t accelerometer:')
        self.accel = i2cBus.read_i2c_block_data(accelAddr, begAddr, totBytes)
        print(self.accel)
        
    def displayMagnetometerData(self):
            
        print('\t magnetometer:')
        self.mag = i2cBus.read_i2c_block_data(magAddr, begAddr, totBytes)
        print(self.mag)
    
    def displayPressureData(self):
        print('\t pressure sensor:')
        self.pres = i2cBus.read_i2c_block_data(pressAddr, begAddr, totBytes)
        print(self.pres)
        
    def displayHumidityData(self):
            
        print('\t humidity sensor:')
        self.humid = i2cBus.read_i2c_block_data(humidAddr,begAddr, totBytes)
        print(self.humid)
    
    '''
        Implement thread
        @summary: When adaptor is ON, sensor data is read and displayed
    '''

    def run(self):
        while True:
            if self.enableEmulator:
                self.displayAccelerometerData()
                self.displayMagnetometerData()
                self.displayPressureData()
                self.displayHumidityData()
            sleep(self.rateInSec)