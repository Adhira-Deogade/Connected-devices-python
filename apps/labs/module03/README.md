# Sensor and actuator processing
#### A simple sensor processing and actuator engagement application on an IoT device
Summary: The app will perform processing data from an IoT sensor (e.g: Camera, GPIO-based sensor, etc) and triggering a simluated state change on a GPIO-based sensor/actuator (e.g: LED display) using both open source libraries and custom developed software to:
- handle sensor events
- notify local/remote system
- retrieve stage change/command
- trigger simulated state change on actuator

#### Fucntioning: The app will - 
1. Read basic communications configuration data from file
2. Read data from RaspberryPi - SenseHAT module
3. Send sensor data to both _the SMTP client_, and to *_thermostat_* actuator adaptor
4. Parse sensor data and signal actuator to adjust temperature (_up_ if temperature dropped, _down_ if temperature rose)
5. Update SenseHAT LED’s to display a relevant message indicating temp was updated


#### Diagram representation:
![alt text](https://github.com/Adhira-Deogade/Connected-devices-python/blob/master/apps/labs/module03/Module03.png)
___

#### How to run the app:
1. On RaspberryPi:
  a. Create a sub-directory under /home/pi named ‘workspace’ (/home/pi/workspace)
  b. Power off the Pi, plug the SenseHAT into the GPIO (correctly!), and power the Pi back on
  c. Access your Raspberry Pi via the same network your laptop / workstation is on and you know it’s IP / hostname
  d. Install the SenseHAT python package on the Raspberry Pi
  ```
  sudo apt-get install python3
  sudo apt-get install python3-pip
  pip3 install sense-hat
  ```
  e. On your workstation:
    i. Create tar file of this folder ```tar -cvf iot-device-sw.tar Connected-devices-python/```
    ii. ```scp iot-device-sw.zip pi@{your hostname or ip address}:/home/pi/workspace```
  f. On your RaspberryPi:
    i. ```tar -xvf iot-device-sw.tar```
    ii. If you have GPIO configured and a SenseHAT installed, delete the proxy / shadow files:
    ``` rm -rf Connected-devices-python/apps/sense_hat.py Connected-devices-python/apps/RPi/GPIO.py```
  g. ```python
  python3 TempManagementApp.py
  ```
  

#### Steps:
1. In the [config](https://github.com/Adhira-Deogade/Connected-devices-python/blob/master/config/ConnectedDevicesConfig.props) file, add ```nominalTemp = 20``` to the [device] section.
2. 
Initialize sense hat sensor and set the orientation. Continuously obtain at defined rate to display on sense hat.