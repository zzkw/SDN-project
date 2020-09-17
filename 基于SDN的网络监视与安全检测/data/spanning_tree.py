import requests
import json
from SDN.switch_login_info import SwitchLoginInfo
        

"""
Modify these please
"""
class SpanningTree:
    sw=SwitchLoginInfo()
    def get_SpanningTree_response(self,response=None):
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
              "cmd": "show spanning-tree",
              "version": 1
            },
            "id": 1
          }
        ]
        requests.packages.urllib3.disable_warnings()
        response = requests.post(url,data=json.dumps(payload), headers=myheaders,auth=(switchuser,switchpassword),verify=False).json()['result']['body']['TABLE_tree']['ROW_tree']['TABLE_port']
        
        #print(json.dumps(response,sort_keys=True,indent=4))
#         print("{0:20}{1:15}{2:15}{3:10}{4:14}{5:12}{6:10}".
#             format("interface","role","state","path_cost",
#             "port_priority","port_number","oper_p2p"))
#         for device in response['ROW_port']:
#             print("{0:20}{1:15}{2:15}{3:10}{4:14}{5:12}{6:10}".
#             format(device['if_index'],
#                   device['role'],
#                    device['state'],
#                   device['path_cost'],
#                   device['port_priority'],
#                   device['port_number'],
#                   device['oper_p2p']))
#         
        return response

