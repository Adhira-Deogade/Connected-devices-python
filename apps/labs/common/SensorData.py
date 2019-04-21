


import os
import json
from datetime import datetime

class SensorData():
    timeStamp = None
    name = 'This is new temperature report!'
    tempValue = 0
    pressureValue = 0
    humidityValue = 0
    avgValue = 10
    minValue = 0
    maxValue = 30
    totValue = 0
    sampleCount = 0
#     string_data = ''
#     json_obj_str = ''
#     dummy_str = ''
#     string_data_new = ''
    

    """
    Define a time-stamp to record the time.
    """
    

    def __init__(self):
        self.timeStamp = str(datetime.now())
       

    """
    record and update the current temperature, max and min temperature.
    count the average of the temperature so far.
    """    
        

    def addValue(self, temp, press, humid):
        self.sampleCount += 1
        self.timeStamp = str(datetime.now())
        self.tempValue = temp
        self.pressureValue = press
        self.humidityValue = humid
        self.totValue += temp
        if(self.tempValue < self.minValue):
            self.minValue = self.tempValue
        if(self.tempValue > self.maxValue):
            self.maxValue = self.tempValue
        if(self.totValue != 0 and self.sampleCount > 0):
            self.avgValue = self.totValue / self.sampleCount
      

    """
    Get average temperature.
    """        
            

    def getAvgValue(self):
        return self.avgValue
    

    """
    Get maximum temperature.
    """
    

    def getMaxValue(self):
        return self.maxValue
    

    """
    Get the minimum temperature
    """
    

    def getMinValue(self):
        return self.minValue
    

    """
    Get the current temperature
    """
    

    def getValue(self):
        return self.curValue
    

    """
    name of every round
    """
    

    def setName(self, name):
        self.name = name
        
    
    '''
    To JSon
    '''
    def toJSon(self):
#      
        dummy_str = {
            "name" : self.name,
            "Current" : self.curValue,
            "Time" : self.timeStamp,
            "Average" : self.avgValue,
            "Sample" : self.sampleCount,
            "Min" : self.minValue,
            "Max" : self.maxValue
            }
        json_obj_str = dummy_str
        www = json.dumps(json_obj_str)
        print("WWW: ",www)
#         with open('SensorData.txt', 'w') as outfile:
#             json.dump(json_obj_str, outfile)
        return www

    
    '''
    From JSon
    '''
    def fromJSon(self, string_data):
        my_str = json.loads(string_data)
        self.curValue = my_str['Current']
        self.name = my_str['name']
        self.timeStamp = my_str['Time']
        self.avgValue = my_str['Average']
        self.sampleCount = my_str['Sample']
        self.maxValue = my_str['Max']
        self.minValue = my_str['Min']
        print("Current value = ",self.curValue)
        print("Time = ",self.timeStamp)
        
        
    """
    print out all of the information in a format.
    """
    

    def __str__(self):
        customStr = \
            str(self.name + ":" + \
                os.linesep + '\tTime:    ' + self.timeStamp +  os.linesep + '\tCurrentTemp: ' + str(self.tempValue) + \
                os.linesep + '\tCurrent pressure: ' + str(self.pressureValue) + \
                os.linesep + '\tCurrent humidity: ' + str(self.humidityValue) + \
                os.linesep + '\tAverage: ' + str(self.avgValue) + os.linesep + '\tSample: ' + str(self.sampleCount))
        return customStr
    
    
#     def printFromJSon(self):
#         customStr = \
#             str(self.name + ":" + os.linesep + '\tTime:    ' + self.timeStamp +  os.linesep + '\tCurrent: ' + str(self.curValue) + \
#             os.linesep + '\tAverage: ' + str(self.avgValue) + os.linesep + '\tSample: ' + str(self.sampleCount) +  os.linesep + '\tMin:     ' + str(self.minValue) + os.linesep + '\tMax:    ' + str(self.maxValue))
#         return customStr