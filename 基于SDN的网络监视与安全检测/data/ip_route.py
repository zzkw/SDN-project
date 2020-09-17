import requests
import json
from SDN.switch_login_info import SwitchLoginInfo
        

"""
Modify these please
"""
class IpRoute:
    sw=SwitchLoginInfo()
    def get_ip_response(self):
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
              "cmd": "show ip route summary",
              "version": 1
            },
            "id": 1
          }
        ]
        requests.packages.urllib3.disable_warnings()
        response = requests.post(url,data=json.dumps(payload), headers=myheaders,auth=(switchuser,switchpassword),verify=False).json()['result']['body']['TABLE_vrf']['ROW_vrf']['TABLE_addrf']['ROW_addrf']['TABLE_summary']['ROW_summary']
        #print(json.dumps(response['result'],sort_keys=True,indent=4))
#         print("Total number of routes: ",response['routes'])
#         print("Total number of paths: ",response['paths'])
#         print("mask_length        route_count")
#         for device in response['TABLE_route_count']['ROW_route_count']:
#             print("{0:5}{1:18}".
#             format(device['count'],
#                   device['mask_len']))
        return response
