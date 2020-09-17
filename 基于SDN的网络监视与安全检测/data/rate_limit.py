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
      "cmd": "show hardware rate-limit module 1",
      "version": 1
    },
    "id": 1
  }
]
requests.packages.urllib3.disable_warnings()
response = requests.post(url,data=json.dumps(payload), headers=myheaders,auth=(switchuser,switchpassword),verify=False).json()['result']['body']['TABLE_hardware_rate_limiter']['ROW_hardware_rate_limiter']
print("{0:38}{1:15}{2:15}{3:10}{4:14}".
    format("Class-descr","Config","Allowed","Dropped","Total"))
for device in response:
    print("{0:38}{1:15}{2:15}{3:10}{4:14}".
    format(device['class-descr'],
          device['rate-limit-configured'],
          device['rate-limit-allowed'],
          device['rate-limit-dropped'],
          device['rate-limit-total']))

