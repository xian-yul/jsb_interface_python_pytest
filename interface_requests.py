# @Time         : 2024/02/21 上午 10:26
# @Author       : ljx
# @File         : interface_requests.py
# @Software     : PyCharm
import json

import requests
import util

cases = util.read_data('test_case_api.xlsx', 'interface')
for case in cases:
    time = util.timestamp()
    case_id = case.get('case_id')
    url = case.get('url')
    url = url + '?timestamp=' + str(time)
    method = case.get('method')
    data = eval(case.get('data'))
    expect = eval(case.get('expect'))
    expect_msg = expect.get('message')
    if method == 'post':
        body_var = str(data).replace("'", '"')
        var = util.generate_var(body_var)
        sk = util.generate_sk()
        sign_data = "sk=" + str(sk) + "&timestamp=" + str(time) + "&var=" + str(var)
        sign = util.MD5(sign_data)
        header = {
            "Sign": sign,
            "Content-Type": "application/json"
        }
        data = {
            "phone": "13500135000",
            "sk": str(sk),
            "var": str(var),
        }
        print(data)
        # 将数据转换成JSON格式字符串
        json_data = json.dumps(data)
        # 使用requests发送post请求
        r = requests.post(url=url, headers=header, data=json_data)
        print("请求url ： " + r.url)
        # 以text格式打印出参
        print("请求结果 : " + r.text)
    else:
        str_data = util.dict_key_value(data, '=')
        sign_data = str_data + 'timestamp=' + str(time)
        sign = util.MD5(sign_data)
        # header信息
        header = {
            "Sign": sign,
            "Content-Type": "application/json"
        }
        r = requests.get(url=url, headers=header, params=data)
        print("请求url ： " + r.url)
        # 以text格式打印出参
        print("请求结果 : " + r.text)
    response = r.json()
    real_msg = response.get('message')
    print('预期结果的msg:{}'.format(expect_msg))
    print('实际结果的msg:{}'.format(real_msg))
    if real_msg == expect_msg:
        print('第{}条用例测试通过'.format(case_id))
        final_re = "passed"
    else:
        print('第{}条用例测试不通过'.format(case_id))
        final_re = "failed"
    util.write_result("test_case_api.xlsx", "interface", case_id + 1, 8, final_re)
