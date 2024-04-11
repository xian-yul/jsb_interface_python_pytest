# @Time         : 2024/02/05 上午 11:23
# @Author       : ljx
# @File         : requests_post.py
# @Software     : PyCharm
import json

import requests
from common import util

# 值需放入sign进行md5加密 定义变量存储时间 保证时间一致
time = util.timestamp()
url = "http://192.168.101.24:8070/api/sendSms?timestamp=" + str(time)
# 请求参数 放入body 传入var加密
body_var = '{"phone":"13500135000"}'
var = util.generate_var(body_var)
sk = util.generate_sk()

#  按排序加密sk>timestamp>var 参数不用进行加密 例如 phone
sign_data = "sk=" + str(sk) + "&timestamp=" + str(time) + "&var=" + str(var)
sign = util.MD5(sign_data)

# header信息
header = {
    "Sign": sign,
    "Content-Type": "application/json"
}

# 请求入参
data = {
    "phone": "13500135000",
    "sk": str(sk),
    "var": str(var),
    "smsType": 2
}
# 将数据转换成JSON格式字符串
json_data = json.dumps(data)
print(json_data)
# 使用requests发送post请求
r = requests.post(url=url, headers=header, data=json_data)
print("请求url ： " + r.url)
# 以text格式打印出参
print("请求结果 : " + r.text)

# 以json格式打印出参
# print(r.content)
