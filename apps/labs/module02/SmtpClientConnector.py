from labs.common import ConfigUtil
import labs.common.ConfigConst as configconst
import smtplib
from email.mime.text import MIMEText as mimeText
from email.mime.multipart import MIMEMultipart as mimeMultipart


#create a email address
#configure

class SmtpClientConnector():
    
    """
    Initialize the object of ConfigUtil with the directory of the configuration file.
    """
    
    def __init__(self):
        self.config = ConfigUtil.ConfigUtil('../../../config/ConnectedDevicesConfig.props')
        self.config.loadConfig()
        print('Configuration data...\n' + str(self.config))
        
    """
    Use the defined object to have access the method in ConfigUtil, assign them to attribute in 
    the configuration file.
    Then complete the process of send E-mail.
    """    
        
    def publishMessage(self, topic, data):
        host= self.config.getProperty(configconst.SMTP_CLOUD_SECTION, configconst.HOST_KEY)
        port= self.config.getProperty(configconst.SMTP_CLOUD_SECTION, configconst.PORT_KEY)
        
        fromAddr= self.config.getProperty(configconst.SMTP_CLOUD_SECTION, configconst.FROM_ADDRESS_KEY)
        
        toAddr= self.config.getProperty(configconst.SMTP_CLOUD_SECTION, configconst.TO_ADDRESS_KEY)
        
        authToken= self.config.getProperty(configconst.SMTP_CLOUD_SECTION, configconst.USER_AUTH_TOKEN_KEY)
        
    
        msg= mimeMultipart()
        
        msg['From']= fromAddr
        
        msg['To']= toAddr
        
        msg['Subject'] = topic 
        msgBody = str(data)
        msg.attach(mimeText(msgBody)) 
        msgText = msg.as_string()
        # send e-mail notification
        smtpServer = smtplib.SMTP_SSL(host, port) 
        smtpServer.ehlo()
        smtpServer.login(fromAddr, authToken) 
        smtpServer.sendmail(fromAddr, toAddr, msgText) 
        smtpServer.close()
