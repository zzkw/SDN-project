from telnetlib import IP


class SwitchLoginInfo:
    ipAddress='10.101.112.129'
    userName='admin'
    password='admin.123'
    ifSuccess=1
    def changeUserInfo(self,ip,user,password):
        self.ipAddress=ip
        self.userName=user
        self.password=password
        self.ifSuccess=2
        
        
    
