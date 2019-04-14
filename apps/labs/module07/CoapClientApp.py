'''
Created on 06-Apr-2019

@author: Adhira
'''

from time import sleep
from labs.module07 import CoapClientConnector


'''
    Construct objects
'''
coapClientConnectorApp = CoapClientConnector.CoapClientConnector();
coapClientConnectorApp.daemon = True
print("Starting coap client...")

'''
    Run thread
'''
coapClientConnectorApp.HandleGETTest("Test");
coapClientConnectorApp.HandlePOSTTest("Test", "23");
coapClientConnectorApp.HandlePUTTest("Test", "23");
coapClientConnectorApp.HandleDELETETest("Test", "23");

while (True):
    sleep(10)               # Obtain data every 10 seconds
    

  
   
if __name__ == '__main__':
    pass