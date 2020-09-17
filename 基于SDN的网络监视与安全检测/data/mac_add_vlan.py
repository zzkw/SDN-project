import requests
import json

"""
Modify these please
"""
switchuser='admin'
switchpassword='admin.123'

url='https://10.101.112.129/ins'
myheaders={'content-type':'application/json-rpc'}
payload=[
  {
    "jsonrpc": "2.0",
    "method": "cli",
    "params": {
      "cmd": "show mac address-table vlan 1",
      "version": 1
    },
    "id": 1
  }
]
requests.packages.urllib3.disable_warnings()
response = requests.post(url,data=json.dumps(payload), headers=myheaders,auth=(switchuser,switchpassword),verify=False).json()
#print(json.dumps(response['result'],sort_keys=True,indent=4))
print("MAC address: ",response['result'])
