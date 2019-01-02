'''
 Copyright (c) 2018-2019. Andrew D. King. All Rights Reserved.
 
 Permission is hereby granted, free of charge, to any person obtaining a copy
 of this software and associated documentation files (the "Software"), to deal
 in the Software without restriction, including without limitation the rights
 to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 copies of the Software, and to permit persons to whom the Software is
 furnished to do so, subject to the following conditions:
 
 The above copyright notice and this permission notice shall be included in all
 copies or substantial portions of the Software.

 THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
 SOFTWARE.
'''

import configparser
import os

'''
A simple utility wrapper around the built-in Python
configuration infrastructure.
 
@author: aking
'''
class ConfigUtil:
    configPath = '/mnt/e/aking/Documents/workspace/iot-device/data'
    configFile = configPath + '/' + 'ConnectedDevicesConfig.props'
    configData = configparser.ConfigParser()
    isLoaded   = False
    
    '''
    Constructor for ConfigUtil.
    
    @param configFile The name of the configuration file to load.
    '''
    def __init__(self, configFile = None):
        if (configFile != None):
            self.configFile = configFile
    
    '''
    Attempts to load the config file using the name passed into
    the constructor.
     
    '''
    def loadConfig(self):
        print(str(os.listdir(self.configPath)))
        
        if (os.path.exists(self.configPath)):
            print("Loading config: " + self.configFile)
            self.configData.read(self.configFile)
            self.isLoaded = True
        else:
            print("Failed to OS-check config. Will try to load: " + self.configFile)
            self.configData.read(self.configFile)
            self.isLoaded = True
        
        print("Config: " + str(self.configData.sections()))

    '''
    Returns the entire configuration object. If the config file hasn't
    yet been loaded, it will be loaded.
    
    @param forceReload Defaults to false; if true, will reload the config.
    @return: The entire configuration file.
     
    '''
    def getConfig(self, forceReload = False):
        if (self.isLoaded == False or forceReload):
            self.loadConfig()
        
        return self.configData
    
    '''
    Returns the name of the configuration file.
    
    @return: The name of the config file.
    '''
    def getConfigFile(self):
        return self.configFile

    '''
    Attempts to retrieve the value of 'key' from the config.
    
    @param: section The name of the section to parse.
    @param: key The name of the key to lookup in 'section'.
    @param: forceReload Defaults to false; if true will reload the config.
    @return: The property associated with 'key' in 'section'.
    '''
    def getProperty(self, section, key, forceReload = False):
        return self.getConfig(forceReload).get(section, key)
    
    '''
    Simple boolean check if the config data is loaded or not.
    
    @return: boolean True on success; false otherwise.
    '''
    def isConfigDataLoaded(self):
        return self.isLoaded
    