

# Import libraries
from time import sleep
from labs.module02 import TempSensorEmulator


# Initialize the object of TempSensorEmulator.
sysPerfAdaptor = TempSensorEmulator.module02()

sysPerfAdaptor.daemon = True
print("Starting system performance app daemon thread...")


# Call the start method as to call the run method in TemSensorEmulator thread class.
sysPerfAdaptor.start()
while (True):
    sleep(10)
    
