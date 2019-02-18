import os
import json
from datetime import datetime
COMMAND_OFF = 0
COMMAND_ON = 1
COMMAND_SET = 2
COMMAND_RESET = 3
STATUS_IDLE   = 0
STATUS_ACTIVE = 1
ERROR_OK =0 
ERROR_COMMAND_FAILED = 1 
ERROR_NON_RESPONSIBLE = -1
class ActuatorData():
    timeStamp = None    
    name = 'Not set'
    hasError = False
    command = 0
    errCode = 0
    statusCode = 0
    stateData = None
    val = 0.0
    def __init__(self):
        self.updateTimeStamp()
    def getCommand(self):
        return self.command
    def getName(self):
        return self.name
    def getStateData(self):
        return self.stateData
    def getStatusCode(self):
        return self.status_code
    def getErrorCode(self):
        return self.errcode
    def getValue(self):
        return self.val
    def hasError(self):
        return self.hasError
    def setCommand(self, command):
        self.command = command
    def setName(self, name):
        self.name = name
    def setStateData(self, stateData):
        self.stateData = stateData
    def setStatusCode(self, statusCode):
        self.statusCode = statusCode
    def setErrorCode(self, errCode):
        self.errCode = errCode
        if (self.errCode != 0):
            self.hasError = True
        else:
            self.hasError = False
            
#     def toJSon(self):
#         return self.string_data
#     
#     def fromJSon(self, string_data):
#         self.string_data = string_data
#         
        
    def tojson(self):
#      
        dummy_str = {
            "Command" : self.command,
            "Value" : self.val
            }
        json_obj_str = dummy_str
        www = json.dumps(json_obj_str)
        print("WWW-actuator: ",www)
        return www
    
    '''
    From JSon
    '''
    def fromjson(self, string_data):
        my_str = json.loads(string_data)
        self.val = my_str['Value']
        self.command = my_str['Command']
       
        print("Value = ",self.val)
        print("Command = ",self.command)
   

    def setValue(self, val):
        self.val = val
        
    def updateData(self, data):
        self.command = data.getCommand()
        self.statusCode = data.getStatusCode()
        self.errCode = data.getErrorCode()
        self.stateData = data.getStateData()
        self.val = data.getValue()
            
    def updateTimeStamp(self):
        self.timeStamp = str(datetime.now())
    def __str__(self):
        customStr = \
            str(self.name + ':' + \
            os.linesep + '\tTime:        ' + self.timeStamp + \
            os.linesep + '\tCommand:     ' + str(self.command) +  \
            os.linesep + '\tStatus Code: ' + str(self.statusCode) + \
            os.linesep + '\tError Code:  ' + str(self.errCode) + \
            os.linesep + '\tState Data:  ' + str(self.stateData) + \
            os.linesep + '\tValue:       ' + str(self.val))
        return customStr
            
