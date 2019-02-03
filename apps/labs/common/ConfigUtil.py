import configparser
import os
DEFAULT_CONFIG_FILE = "../../../config/ConnectedDevicesConfig.props"
class ConfigUtil:
    configFile = DEFAULT_CONFIG_FILE
    configData = configparser.ConfigParser()
    isLoaded   = False
    

    """
    Initialize the path of configuration 
    """
    

    def __init__(self, configFile = None):
        if (configFile != None):
            self.configFile = configFile
            

    """
    Open and read the file according to the path 
    using the configparser object
    """        
            

    def loadConfig(self):
        if (os.path.exists(self.configFile)):
            self.configData.read(self.configFile)
            self.isLoaded = True
            

    """
    check if the information of configuration file has be loaded, if not
    then return the object of configparser.
    """        
            

    def getConfig(self, forceReload = False):
        if (self.isLoaded == False or forceReload):
            self.loadConfig()
        return self.configData
    

    """
    To get configFile.
    """
    

    def getConfigFile(self):
        return self.configFile
    

    """
    define method which can pass the parameters defined in configuration file when sending message.
    """
    

    def getProperty(self, section, key, forceReload = False):
        return self.getConfig(forceReload).get(section, key)
    

    """
    check whether the file has been loaded
    """
    

    def isConfigDataLoaded(self):
        return self.isLoaded
