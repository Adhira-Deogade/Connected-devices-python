'''
Created on 02-Feb-2019

@author: Adhira
'''

# Import libraries
from time import sleep
from labs.module01 import SystemPerformanceAdaptor

# Instantiate the adaptor class
sysPerfAdaptor = SystemPerformanceAdaptor.module01()

# Set the daemon to True so as the thread stops at system shutdown
sysPerfAdaptor.daemon = True

# Indicate the starting of thread
print("Starting system performance app daemon thread...")

# Set the status of the adaptor to ON
sysPerfAdaptor.EnableAdaptor = True

# Start the adaptor
sysPerfAdaptor.start()

# Run the application continuously
while (True):
    
    # Delay the command to access the information via app by 5 seconds
    sleep(5)
    
    # Continue running the application
    pass