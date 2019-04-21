
'''
    Created on 09-Feb-2019
    @author: Adhira
'''
from time import sleep
from labs.module03 import TempSensorAdaptor
from labs.module03 import RpiSensorAdaptor

'''
    Construct objects
'''
rpiAdaptor = RpiSensorAdaptor.RpiSensorAdaptor()
rpiAdaptor.daemon = True
# temp_sense_adaptor = TempSensorAdaptor.TempSensorAdaptor()
# temp_sense_adaptor.daemon = True
print("Starting system performance application daemon thread...")

'''
    Run thread
'''
# temp_sense_adaptor.start()
rpiAdaptor.start()
while (True):
    sleep(10)               # Obtain data every 10 seconds
    
