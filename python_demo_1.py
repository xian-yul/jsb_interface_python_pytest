# get_yaml.py

import requests

import yaml
import urllib3
import json

urllib3.disable_warnings()


class SignTest():

    def __init__(self, file):
        self.file = file

    def test_sign(self):
        with open(self.file, encoding='utf-8') as fobj:
            content = fobj.read()  # 使用 yaml.load()将yaml数据转换为list或dict
            data = yaml.load(content, Loader=yaml.FullLoader)  # 使用for循环，依次读取测试用例
            for i in range(len(data)):
                # 从yaml中提取接口的参数　　　　　　      # 由于读取到的数据类型为list列表，所以只能用下标访问
                title = data[i]['title']
                method = data[i]['method']
                port = data[i]['port']
                url = data[i]['url']
                datas = data[i]['data']
                header = data[i]['header']
                expected = data[i]['expected']
                self.sign_test(title, method, port, url, datas, header, expected)

    def sign_test(self, title, method, port, url, datas, header, expected):
        print("用例标题：", title)
        print("请求方式：", method)
        print("端口：", port)
        print("url：", url)
        print("返回值：", datas)
        print("请求头：", header)
        print("预计结果：", expected)
        response = requests.request(url=url, method=method, data=datas, headers=header)
        response = json.loads(response.text)
        print(response)
        try:
            # 通过断言，判断实际结果是否与预期结果一致
            assert expected['code'] == response['code']
            print("测试通过\n")
        except Exception:
            print("测试失败\n")


if __name__ == "__main__":
    signtest = SignTest("yaml/test_case.yaml")
    signtest.test_sign()
