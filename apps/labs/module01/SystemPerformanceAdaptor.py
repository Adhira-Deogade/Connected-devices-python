'''
Created on 02-Feb-2019

@author: Adhira
'''

# Cycle time for running thread
DEFAULT_RATE = 10

# Import libraries
import psutil
from time import sleep
import threading

# Define thread class
class module01(threading.Thread):
    
    # Set the status of adaptor
    EnableAdaptor = False
    
    # Set rate of reading information
    rateInSec = DEFAULT_RATE
    
    # Assign value to the rate of accessing information
    # Set rate to run time of thread
    def __init__(self,rateInSec=DEFAULT_RATE):
        super(module01,self).__init__()
        
        if rateInSec > 0:
            self.rateInSec = rateInSec
    
    # Starting the thread
    def run(self):
        
        # Run continuously
        while True:
            
            # When the adaptor is ON
            if self.EnableAdaptor:
                print ('\n--------------------')
                print ('New system performance readings:')
                
                # Obtain system status and display on console
                print (' ' + str(psutil.cpu_stats()))
                print (' ' + str(psutil.virtual_memory()))
                
            # Sleep thread for 10 seconds    
            sleep(self.rateInSec)