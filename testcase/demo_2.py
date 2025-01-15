import requests

from utils import util

url = 'http://v3.www.jinsubao.test/api/tradeFloor/statistics'
# url = "http://192.168.101.24:8090/api/couponCenter/coupon"
# url = "http://192.168.101.24:8050/api/auditBasisIndemnity"
# url = "http://192.168.101.24:9001/test/basis/contractValid/maturity"
# url = "https://demo.jinsubao.cn/api/test/basis/contractValid/maturity"
# params = {'contractNumber': 'l2405', 'contractValid': '1', 'time': '1716566399000'}
# header信息
header = {
    "Content-Type": "application/x-www-form-urlencoded",
}

# 使用requests发送get请求
r = requests.post(url=url, headers=header)
print("请求url ： " + r.url)
print("请求结果 : " + r.text)
print("请求状态 : " + str(r.status_code))
