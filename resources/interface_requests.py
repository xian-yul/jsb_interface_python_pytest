# @Time         : 2024/02/21 上午 10:26
# @Author       : ljx
# @File         : interface_requests.py
# @Software     : PyCharm
import json
import requests

from common import util
from common.readelement import Element

getToken = Element('Token')

# 引入测试用例 excel地址
cases = util.read_data('../Testcase/test_case_api.xlsx', 'interface')
for case in cases:
    time = util.timestamp()
    case_id = case.get('case_id')
    url = case.get('url')
    url = url + '?timestamp=' + str(time)
    method = case.get('method')
    case_port = case.get('case_port')
    case_interface = case.get('case_interface')
    case_title = case.get('case_title')
    data = eval(case.get('data'))
    header = eval(case.get('header'))
    expect = eval(case.get('expect'))
    expect_msg = expect.get('message')
    if method == 'post':
        body_var = str(data).replace("'", '"')
        var = util.generate_var(body_var)
        sk = util.generate_sk()
        sign_data = "sk={}&timestamp={}&var={}".format(str(sk), str(time), str(var))
        if 'sign' in header and header['sign'] is None:
            sign = util.MD5(sign_data)
            header['sign'] = sign
        data.update({'sk': str(sk)})
        data.update({'var': str(var)})
        # 将数据转换成JSON格式字符串
        json_data = json.dumps(data)
        # 使用requests发送post请求
        r = requests.post(url=url, headers=header, data=json_data)
    else:
        str_data = util.dict_key_value(data, '=')
        sign_data = str_data + 'timestamp=' + str(time)
        if 'sign' in header and header['sign'] is None:
            sign = util.MD5(sign_data)
            header['sign'] = sign
        r = requests.get(url=url, headers=header, params=data)

    # 以text格式打印出参
    response = r.json()
    real_msg = response.get('message')
    print(
        "用例ID:{}\n请求方式:{}\n请求标题:{}\n请求端口:{}\n请求url:{}\n请求结果:{}\n预期结果:{}\n实际结果:{} ".format(
            case_id, method,
            case_title,
            case_port,
            r.url,
            r.text,
            expect_msg,
            real_msg))
    if real_msg == expect_msg:
        print('第{}条用例测试通过'.format(case_id))
        final_re = "passed"
    else:
        print('第{}条用例测试不通过'.format(case_id))
        final_re = "failed"
    print('-------------------------------------')
    util.write_result("../Testcase/test_case_api.xlsx", "interface", case_id + 1, 10, final_re)
