# Basic data processing

#### A simple data processing application on an IoT device (real or emulated)

Summary: The app will perform processing of basic data from an IoT device sensor (e.g. camera, GPIO-based sensor, etc.) using both open source libraries and custom developed software to handle sensor events and notify a local or remote system using one or more IoT protocols.

#### Functioning:
1. The app will emulate temperature sensor data
2. Based on threshold crossing, send well-informed SMS/ e-mail alert to account

#### Diagram represntation:
![alt text](https://github.com/Adhira-Deogade/cd-github-python/blob/master/apps/labs/module02/Module2.png)
____

#### How to run the app:
```
cd apps/labs/module02
python3 TempSimulatorApp.py
```

#### Steps:
1. Specify email addresses to send from and receive from and host in *_[Configuration.props](https://github.com/Adhira-Deogade/cd-github-python/blob/master/config/ConnectedDevicesConfig.props)_*
2. Specify the conditions on temperature monitoring data that will initiate alert and send email in [TempSensorAdaptor](apps/labs/module03/TempSensorAdaptor.py)
3. Generate random temperature values periodically in [TempSensorEmulator](apps/labs/module02/TempSensorEmulator.py)
4. Configure email and host for email alerts in [SMTP server](apps/labs/module02/SmtpClientConnector.py)
5. Specify data processing functions in [SensorData](apps/labs/common/SensorData.py)
6. Specify getters and setters for configuration parameters in [ConfigUtil](apps/labs/common/ConfigUtil.py)
7. Set up environment variables, to look up default configuration values in [ConfigConst](apps/labs/common/ConfigConst.py)
8. Update and diplay data processing conditions and alert message for email in [ActuatorData](apps/labs/common/ActuatorData.py)

#### Sample output:
###### 1. Data processing updates:
![alt text](https://github.com/Adhira-Deogade/cd-github-python/blob/master/apps/labs/module02/Picture2.png)

###### 2. Email alert:
![alt text](https://github.com/Adhira-Deogade/cd-github-python/blob/master/apps/labs/module02/Picture3.png)
