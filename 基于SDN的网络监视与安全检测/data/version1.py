import requests
import json
from SDN.switch_login_info import SwitchLoginInfo

class Item:
    sw=SwitchLoginInfo()
    def __init__(self,ip=None,user=None,password=None,response=None):
        self.response=response
        
        if(self.sw.ifSuccess==1):
            self.switchuser=self.sw.userName
            self.switchpassword=self.sw.password
            self.url='https://'+self.sw.ipAddress+'/ins'
        else:
            self.switchuser=user
            self.switchpassword=password
            self.url='https://'+ip+'/ins'
#         self.switchuser='admin'
#         self.switchpassword='admin.123'
# 
#         self.url='https://10.101.112.129/ins'
        
        self.myheaders={'content-type':'application/json'}
        self.payload={
          "ins_api": {
            "version": "1.0",
            "type": "cli_show",
            "chunk": "0",
            "sid": "1",
            "input": "show version",
            "output_format": "json"
          }
        }
        requests.packages.urllib3.disable_warnings()
       
    def print_version(self):
        
        self.response = requests.post(self.url,data=json.dumps(self.payload), headers=self.myheaders,auth=(self.switchuser,self.switchpassword),verify=False).json()["ins_api"]["outputs"]["output"]
        return self.response




#print("version:",response["version"])
#print("status:",response["outputs"]["output"]["code"])
#print("msg:",response["outputs"]["output"]["msg"])
#print("name:",response["outputs"]["output"]["body"]["host_name"])


