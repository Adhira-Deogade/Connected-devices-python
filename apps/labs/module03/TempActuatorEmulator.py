

'''
    Created on 09-Feb-2019
    @author: Adhira
'''
from labs.common import ActuatorData
from labs.module03.SenseHatLedActivator import SenseHatLedActivator

'''
    Construct objects
'''
actuator = ActuatorData.ActuatorData()
senseHatActivator = SenseHatLedActivator()

'''
    Emulator to generate temperature data
'''
class TempActuatorEmulator():
    def __init__(self):
        senseHatActivator.setEnableLedFlag(True)
        
    ''' 
        Implement method to accept and store actuator data 
        @param actuator: All data from actuator object
        @summary: 
        1. Turn SenseHat ON
        2. Start the thread
        3. Update actuator data file
        4. Set condition for displaying message
        5. Call display message method from LedActivator
    '''
    def processMessage(self, actuator):
        senseHatActivator.setEnableLedFlag(True)
        senseHatActivator.run()
        print('Can be run here?')
        actuator.updateData(actuator)                                                       # Update actuator data file
        
        ''' Obtain information for adaptor to display - condition for displaying message''' 
        if actuator.getCommand() == 1:
            show_mesg = 'Temperature higher than normal: ' + str(abs(actuator.getValue()))  # Obtain values from actuator data file
        else:
            show_mesg = 'Temperature lower than normal: ' + str(abs(actuator.getValue()))
        
        ''' Send the message to SenseHat '''
        self.senseHatActivator.setDisplayMessage(show_mesg)
     
