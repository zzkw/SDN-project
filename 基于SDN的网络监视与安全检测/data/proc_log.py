import requests
import json
from SDN.switch_login_info import SwitchLoginInfo
        
        
"""
Modify these please
"""
class ProcLog:
    sw=SwitchLoginInfo()
    def get_ProLog_response(self,response=None):
        if(self.sw.ifSuccess==0):
            return
        switchuser=self.sw.userName
        switchpassword=self.sw.password
        
        url='https://'+self.sw.ipAddress+'/ins'
        myheaders={'content-type':'application/json-rpc'}
        payload=[
          {
            "jsonrpc": "2.0",
            "method": "cli",
            "params": {
              "cmd": "show processes log",
              "version": 1
            },
            "id": 1
          }
        ]
        requests.packages.urllib3.disable_warnings()
        response = requests.post(url,data=json.dumps(payload), headers=myheaders,auth=(switchuser,switchpassword),verify=False).json()
        #print(json.dumps(response['result'],sort_keys=True,indent=4))

        return response

