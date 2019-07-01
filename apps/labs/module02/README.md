# Basic data processing

#### A simple data processing application on an IoT device (real or emulated)

Summary: The app will perform processing of basic data from an IoT device sensor (e.g. camera, GPIO-based sensor, etc.) using both open source libraries and custom developed software to handle sensor events and notify a local or remote system using one or more IoT protocols.

#### Functioning:
1. The app will emulate temperature sensor data
2. Based on threshold crossing, send well-informed SMS/ e-mail alert to account

#### Diagram represntation:
![alt text](https://github.com/Adhira-Deogade/cd-github-python/blob/master/apps/labs/module02/Module2.png)

#### How to run the app:
```
cd apps/labs/module02
python3 TempSimulatorApp.py
```

#### Steps:
1. Create *_[Configuration.props](https://github.com/Adhira-Deogade/cd-github-python/blob/master/config/ConnectedDevicesConfig.props)_* to specify email addresses to send from and receive from and host
2. Create [TempSensorAdaptor](apps/labs/module03/TempSensorAdaptor.py) to specify the conditions on temperature monitoring data that will initiate alert and send email
3. Generate random temperature values periodically in [TempSensorEmulator](apps/labs/module02/TempSensorEmulator.py)
4. Create [SMTP server](apps/labs/module02/SmtpClientConnector.py) from email and host conifgurations to send email alerts.
5. Create [SensorData](apps/labs/common/SensorData.py) to specify data processing functions.
6. Create [ConfigUtil](apps/labs/common/ConfigUtil.py) where we specify getters and setters for configuration parameters.
7. Create [ConfigConst](apps/labs/common/ConfigConst.py) which is a replica of environment variables, looking up default configuration values
8. Create [ActuatorData](apps/labs/common/ActuatorData.py) to update and diplay data processing conditions and alert message for email.

#### Sample output:
###### 1. Data processing updates:
![alt text](https://github.com/Adhira-Deogade/cd-github-python/blob/master/apps/labs/module02/Picture2.png)

###### 2. Email alert:
![alt text](https://github.com/Adhira-Deogade/cd-github-python/blob/master/apps/labs/module02/Picture3.png)
