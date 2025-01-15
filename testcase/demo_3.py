# @Time         : 2024/02/05 上午 11:23
# @Author       : ljx
# @File         : requests_post.py
# @Software     : PyCharm
import json
import time

import requests
from utils import util

# 值需放入sign进行md5加密 定义变量存储时间 保证时间一致

# 请求参数 放入body 传入var加密


#  按排序加密sk>timestamp>var 参数不用进行加密 例如 phone
# sign_data = "sk=" + str(sk) + "&timestamp=" + str(time) + "&var=" + str(var)


# # 请求入参
# data = {
#     "phone": "13500135000",
#     "sk": str(sk),
#     "var": str(var),
#     "smsType": 2
# }
# # 将数据转换成JSON格式字符串
# json_data = json.dumps(data)
# print(json_data)
# 使用requests发送post请求


# 以json格式打印出参
# print(r.content)

for num in range(0, 20):
    timestamp = util.timestamp()
    url = 'http://v3.www.jinsubao.test/api/tradeFloor/statistics?timestamp=' + str(timestamp)
    body_var = ''
    var = util.generate_var(body_var)
    sk = util.generate_sk()
    sign_data = 'timestamp=' + str(timestamp)
    sign = util.MD5(sign_data)
    # header信息
    header = {
        "Sign": sign,
        "Content-Type": "application/json"
    }
    r = requests.get(url=url, headers=header)
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    print("请求url ： " + r.url)
    # 以text格式打印出参
    print("请求结果 : " + r.text)
    num += 1
    time.sleep(1)
    print('---------')
    print()
