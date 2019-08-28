# On-device processing
#### An application that reads data directly from the SenseHAT on a Raspberry Pi-3

Summary: The app will interact with various sensors connected to RPi's GPIO with I2C protocol, SenseHat and python libraries. It will read data from SenseHAT sensor module and display it on SenseHAT LEDs.

#### Diagram representation:
![alt text](https://github.com/Adhira-Deogade/Connected-devices-python/blob/master/apps/labs/module04/Module4.png)
___

#### How to run the app:
  1. Follow steps 1, 2 and 3 from [module03](apps/labs/module03/README.md)
  2. Run the app on RPi: ```python3 SensorReaderApp.py```
  
#### Steps:
  1. Create [sensehat-adaptor](https://github.com/Adhira-Deogade/Connected-devices-python/blob/master/apps/labs/module04/I2CSenseHatAdaptor.py) python file which - 
      - initializes ***SMBus***
      - specifies addresses for sensors to read data from I2C buffers
      - load configurations
      - read and write data to bus
      - display all collected sensor values
      - **Thread** for periodically running these functions
      
  2. Run the [app](https://github.com/Adhira-Deogade/Connected-devices-python/blob/master/apps/labs/module04/SensorReaderApp.py)

#### Sample output:
![alt text](https://github.com/Adhira-Deogade/Connected-devices-python/blob/master/apps/labs/module04/Op4.png)
___
