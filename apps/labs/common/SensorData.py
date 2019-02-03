import os
from datetime import datetime
class SensorData():
    timeStamp = None
    name = 'This is new temperature report!'
    curValue = 0
    avgValue = 0
    minValue = 0
    maxValue = 30
    totValue = 0
    sampleCount = 0
    

    """
    Define a timestamp to record the time.
    """
    

    def __init__(self):
        self.timeStamp = str(datetime.now())
       

    """
    record and update the current temperature, max and min temperature.
    count the average of the temperature so far.
    """    
        

    def addValue(self, newVal):
        self.sampleCount += 1
        self.timeStamp = str(datetime.now())
        self.curValue = newVal
        self.totValue += newVal
        if(self.curValue < self.minValue):
            self.minValue = self.curValue
        if(self.curValue > self.maxValue):
            self.maxValue = self.curValue
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
        

    """
    print out all of the information in a format.
    """
    

    def __str__(self):
        customStr = \
            str(self.name + ":" + os.linesep + '\tTime:    ' + self.timeStamp +  os.linesep + '\tCurrent: ' + str(self.curValue) + \
            os.linesep + '\tAverage: ' + str(self.avgValue) + os.linesep + '\tSample: ' + str(self.sampleCount) +  os.linesep + '\tMin:     ' + str(self.minValue) + os.linesep + '\tMax:    ' + str(self.maxValue))
        return customStr