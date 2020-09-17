import requests
import json
from SDN.switch_login_info import SwitchLoginInfo
"""
Modify these please
"""

class Redundancy:
    sw=SwitchLoginInfo()
    def get_redundancy_response(self,response=None):
        if(self.sw.ifSuccess==0):
            return
        self.response=response
        
        switchuser=self.sw.userName
        switchpassword=self.sw.password
        
        url='https://'+self.sw.ipAddress+'/ins'
        myheaders={'content-type':'application/json-rpc'}
        payload=[
          {
            "jsonrpc": "2.0",
            "method": "cli",
            "params": {
              "cmd": "show system redundancy status",
              "version": 1
            },
            "id": 1
          }
        ]
        requests.packages.urllib3.disable_warnings()
        self.response = requests.post(url,data=json.dumps(payload), headers=myheaders,auth=(switchuser,switchpassword),verify=False).json()['result']['body']
        return self.response
