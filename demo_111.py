import requests

# 基差合约更改
url = "http://192.168.101.24:9001/test/basis/contractValid/maturity"
# url = "https://demo.jinsubao.cn/api/test/basis/contractValid/maturity"
params = {'contractNumber': 'ru2501', 'contractValid': '2', 'time': '1721871923000', 'oldContractNumber': 'ru2409'}

header = {
    "Content-Type": "application/x-www-form-urlencoded",
}

r = requests.post(url=url, headers=header, params=params)
print("请求url ： " + r.url)
print("请求结果 : " + r.text)
print("请求状态 : " + str(r.status_code))
