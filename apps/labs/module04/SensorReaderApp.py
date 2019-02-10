

'''
    Created on 09-Feb-2019
    @author: Adhira
'''

import sys,os
sys.path.insert(0,'/home/pi/workspace/connected-devices-python/apps')
from time import sleep
from labs.module04 import I2CSenseHatAdaptor


'''
    Instantiate sense hat adaptor
'''
TempAd = I2CSenseHatAdaptor.I2CSenseHatAdaptor()

print("Starting...")

'''
    Turn emulator ON
'''
TempAd.enableEmulator = True
TempAd.daemon = True
TempAd.start()

'''
    Run thread continuously every 5 minutes to read the buffers
'''
while (True):
    sleep(5)
    pass