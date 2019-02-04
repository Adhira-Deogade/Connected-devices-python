



# Import libraries
from labs.common import ConfigUtil
import labs.common.ConfigConst as configconst
import smtplib
from email.mime.text import MIMEText as mimeText
from email.mime.multipart import MIMEMultipart as mimeMultipart


#create a email address
#configure
class SmtpClientConnector():
    

    #Initialize the object of ConfigUtil with the directory of the configuration file.
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
        
        # From getProperty, passing section and key parameters, obtain host and port values
        host= self.config.getProperty(configconst.SMTP_CLOUD_SECTION, configconst.HOST_KEY)
        port= self.config.getProperty(configconst.SMTP_CLOUD_SECTION, configconst.PORT_KEY)
        
        # Obtain Email addresses of "For and to" and authentication code of sending email 
        fromAddr= self.config.getProperty(configconst.SMTP_CLOUD_SECTION, configconst.FROM_ADDRESS_KEY)
        toAddr= self.config.getProperty(configconst.SMTP_CLOUD_SECTION, configconst.TO_ADDRESS_KEY)
        authToken= self.config.getProperty(configconst.SMTP_CLOUD_SECTION, configconst.USER_AUTH_TOKEN_KEY)
        
        # Initialize message   
        msg= mimeMultipart()
        
        # Define message attributes
        msg['From']= fromAddr
        msg['To']= toAddr        
        msg['Subject'] = topic
        
        # Obtain temperature information to publish in message
        msgBody = str(data)
        
        # Attach the information to email
        msg.attach(mimeText(msgBody)) 
        
        # Convert information to string for email to display
        msgText = msg.as_string()
        
        ''' Send e-mail notification '''
        # Create server with host address and port values
        smtpServer = smtplib.SMTP_SSL(host, port) 
        smtpServer.ehlo()
        smtpServer.login(fromAddr, authToken) 
        smtpServer.sendmail(fromAddr, toAddr, msgText) 
        smtpServer.close()
