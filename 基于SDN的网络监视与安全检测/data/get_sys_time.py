import requests, urllib3
from SDN.switch_login_info import SwitchLoginInfo
    
class SysInfo:
    sw=SwitchLoginInfo()
    def running_time(self):
        if(self.sw.ifSuccess==0):
            return
        # Disable Self-Signed Cert warning for demo
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        
        # Assign requests.Session instance to session variable
        session = requests.Session()
        
        # Define URL and PAYLOAD variables
        URL = "https://"+self.sw.ipAddress+"/api/aaaLogin.json"
        PAYLOAD = {
                  "aaaUser": {
                    "attributes": {
                      "name": self.sw.userName,
                      "pwd": self.sw.password
                       }
                    }
                  }
        
        # Obtain an authentication cookie
        session.post(URL,json=PAYLOAD,verify=False)
        
        # Define SYS_URL variable
        SYS_URL = "https://"+self.sw.ipAddress+"/api/mo/sys.json"
        
        # Obtain system information by making session.get call
        # then convert it to JSON format then filter to system attributes
        sys_info = session.get(SYS_URL,verify=False).json()["imdata"][0]["topSystem"]["attributes"]
        #print(sys_info)
        # Print raw data
        
        #print("HOSTNAME:", sys_info["name"])
        #print("SERIAL NUMBER:", sys_info["serial"])
        return sys_info
