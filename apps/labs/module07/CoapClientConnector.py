'''
Created on 06-Apr-2019

@author: Adhira
'''
from coapthon.client.helperclient import HelperClient
from labs.common import ConfigUtil
from labs.common import ConfigConst
from labs.common import SensorData


client = None;
sensor = SensorData.SensorData();

class CoapClientConnector():
    
    config = None
    serverAddr = None
    host = "127.0.0.1"
    port = 5683
    
    
    def __init__(self):
        
        self.config = ConfigUtil.ConfigUtil("../../../config/ConnectedDevicesConfig.props");
        self.config.loadConfig();
        
        print("Configuration data: \n"+str(self.config));
        print('============= Setting Done! =============')
        
        
        self.host = self.config.getProperty(ConfigConst.COAP_GATEWAY_SECTION, ConfigConst.HOST_KEY);
        self.port = int(self.config.getProperty(ConfigConst.COAP_GATEWAY_SECTION,ConfigConst.PORT_KEY));
        try:
            self.client = HelperClient(server=(self.host, self.port));
            print("Created Coap client ref: " + str(self.client));
            print("coap://" + self.host + ":" + self.port);
        except Exception:
            print("Failed to create coap helper client reference using host: "+self.host);
            pass
        
        print("Host = "+self.host);
        print("Port = "+str(self.port));
        
        if not self.host or self.host.isspace():
            print("Using default host: "+self.host);
        if int(self.port) < 1024 or int(self.port) > 65535:
            print("Using default port: "+ self.port);
            
        self.serverAddr = (self.host, self.port);
        print("Server address is: "+ str(self.serverAddr));
        
        self.url = "coap://" + self.host + ":" + str(self.port) + "/Test" ;
    
#     def initClient(self):
#         try:
#             self.client = HelperClient(server=(self.host, self.port));
#             print("Created Coap client ref: " + str(self.client));
#             print("coap://" + self.host + ":" + self.port);
#         except Exception:
#             print("Failed to create coap helper client reference using host: "+self.host);
#             pass
    
    def HandleGETTest(self, resource):
        print("GET method");
        print("Testing GET for resources: " + str(resource));
        self.__init__();
        
        response = self.client.get(resource);
        if response:
            print("Response from GET is: " + response.pretty_print());
        else:
            print("No response received for GET using the resources: " + resource);
        self.client.stop();
        
    def HandlePOSTTest(self, resource, payload):
        print("Testing POST for resource: " + resource + " payload: " + payload);
        self.__init__();
        
        response = self.client.post(resource, payload);
        if response:
            print("Response from POST is: " + response.pretty_print());
        else:
            print("No response received for POST using the resources: " + resource);
        self.client.stop();
        
    def HandlePUTTest(self, resource, payload):
        print("Testing PUT for resource: " + resource + " payload: " + payload);
        self.__init__();
        
        response = self.client.put(resource, payload);
        if response:
            print("Response from PUT is: " + response.pretty_print());
        else:
            print("No response received for PUT using the resources: " + resource);
        self.client.stop();
    
    def HandleDELETETest(self, resource, payload):
        print("Testing DELETE for resource: " + resource + " payload: " + payload);
        self.__init__();
        
        response = self.client.delete(resource, payload);
        if response:
            print("Response from DELETE is: " + response.pretty_print());
        else:
            print("No response received for DELETE using the resources: " + resource);
        self.client.stop();
        
        
def main(self):
    
    CoapClientConnector().HandleGETTest("Test");
    CoapClientConnector().HandlePOSTTest("Test", "23");
    CoapClientConnector().HandlePUTTest("Test", "23");
    CoapClientConnector().HandleDELETETest("Test", "23");
        
    
if __name__ == '__main__':
        main()
#             
            
            
            
            