

'''
    Created on 09-Feb-2019
    @author: Adhira
'''

from time import sleep
from sense_hat import SenseHat
import threading

'''
    Define thread for obtaining data from sense hat
'''
class SenseHatLedActivator(threading.Thread):
    enableLed  = False                        
    rateInSec  = 1                            
    rotateDeg  = 270
    sh = None 
    displayMsg = None
    
    ''' Constructor
        @param rotateDeg: Orientation for senseHat (default)
        @param rateInSec: Rate of obtaining data from sense hat
        @summary: Initialize sense hat sensor and set the orientation
    '''
    
    def __init__(self, rotateDeg = 270, rateInSec = 1):
        super(SenseHatLedActivator, self).__init__()
        if rateInSec > 0:
            self.rateInSec = rateInSec
        if rotateDeg >= 0:
            self.rotateDeg = rotateDeg
        self.sh = SenseHat()                    
        self.sh.set_rotation(self.rotateDeg)
        
        ''' Running thread
        @summary: Continuously obtain data from code at defined rate to display on sense hat.
                  Set condition for displaying data on sense hat
        '''
    def run(self):
        while True:
            if self.enableLed:
                if self.displayMsg != None:
                    self.sh.show_message(str(self.displayMsg))
                else:
                    self.sh.show_letter(str('R'))
                sleep(self.rateInSec)
                self.sh.clear()
            sleep(self.rateInSec)
            
        ''' 
        Define frequency of obtaining data
        @return: rate of sensing data
        '''
    def getRateInSeconds(self):
        return self.rateInSec
    
    '''
         Switch for sense hat 
         @param enable: Switch status - ON or OFF
    '''
    def setEnableLedFlag(self, enable):
        self.sh.clear()
        self.enableLed = enable
        
        '''
        Method to display message
        '''
    def setDisplayMessage(self, msg):
        self.displayMsg = msg
