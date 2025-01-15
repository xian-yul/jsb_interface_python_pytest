import json

import requests

from utils import util

# 推送
# url = "http://192.168.101.24:9001/test/basis/push?timestamp=" + str(util.timestamp())
url = 'http://192.168.101.24:9001/test/basisContractAutoSwitch'

header = {
    "Content-Type": "application/json",
}
params = {
    "fromNumber": "l2409",
    "fromName": "塑料2409",
    "toNumber": "l2501",
    "toName": "塑料2501",
    "auto": 1
}

r = requests.post(url=url, headers=header, data=params)
print("请求url ： " + r.url)
print("请求结果 : " + r.text)
print("请求状态 : " + str(r.status_code))
