import requests

from common import util

# url = "http://192.168.101.24:8090/api/couponCenter/coupon"
url = "http://192.168.101.24:8050/api/auditBasisIndemnity"
params = {'pageNum': 1, 'pageSize': 10, 'timestamp': util.timestamp()}
sign_data = 'pageNum=1&pageSize=10timestamp=' + str(util.timestamp())
print(sign_data)
sign = util.MD5(sign_data)
# header信息
header = {
    "Content-Type": "application/json",
    "Sign": sign,
}

# 使用requests发送get请求
r = requests.get(url=url, headers=header, params=params)
print("请求url ： " + r.url)
# 以text格式打印出参
print("请求结果 : " + r.text)

# 以json格式打印出参
# print(r.json())
