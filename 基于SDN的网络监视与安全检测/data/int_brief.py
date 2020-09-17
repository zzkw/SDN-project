import requests
import json
from SDN.switch_login_info import SwitchLoginInfo
        

"""
Modify these please
"""
class Brief:
    sw=SwitchLoginInfo()
    def get_brief_response(self):
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
              "cmd": "show interface brief",
              "version": 1
            },
            "id": 1
          }
        ]
        requests.packages.urllib3.disable_warnings()
        response = requests.post(url,data=json.dumps(payload), headers=myheaders,auth=(switchuser,switchpassword),verify=False).json()['result']['body']['TABLE_interface']
        #print(json.dumps(response,sort_keys=True,indent=4))
                
        return response
