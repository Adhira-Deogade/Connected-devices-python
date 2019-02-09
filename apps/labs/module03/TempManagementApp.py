
'''
    Created on 09-Feb-2019
    @author: Adhira
'''
from time import sleep
from labs.module03 import TempSensorAdaptor

'''
    Construct objects
'''
temp_sense_adaptor = TempSensorAdaptor.TempSensorAdaptor()
temp_sense_adaptor.daemon = True
print("Starting system performance application daemon thread...")

'''
    Run thread
'''
temp_sense_adaptor.start()
while (True):
    sleep(10)               # Obtain data every 10 seconds
    
