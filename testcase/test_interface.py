# @Time         : 2024/02/21 上午 10:26
# @Author       : ljx
# @File         : test_interface.py
# @Software     : PyCharm
import json

import pytest
import requests
import allure
from common import util, log
from common.log import Log
from common.readelement import Element
from common.util import post_request_encryption, get_request_encryption, setting_select
from config.allParams import EXCEL_OUTSIDE

getToken = Element('Token')
setting = '24'
log = Log()


# class TestInterface:
def test_interface():
    path_dict = setting_select()
    cases = util.read_data(path_dict['excel'], EXCEL_OUTSIDE)
    for case in cases:
        time = util.timestamp()
        case_id = case.get('case_id')
        method = case.get('method')
        case_port = case.get('case_port')
        case_interface = case.get('case_interface')
        url = path_dict.get('url')
        url = url + case_interface + '?timestamp=' + str(time)
        case_title = case.get('case_title')
        data = eval(case.get('data'))
        header = eval(case.get('header'))
        expect = eval(case.get('expect'))
        expect_msg = expect.get('message')
        # 动态获取参数生成标题
        allure.dynamic.title(case_title)
        with allure.step('判断请求方式: {}'.format(case_port)):
            if method == 'post':
                data_dict = post_request_encryption(data, header)
                # 将数据转换成JSON格式字符串
                json_data = json.dumps(data_dict.get('data'))
                # 使用requests发送post请求
                r = requests.post(url=url, headers=data_dict.get('headers'), data=json_data)
            else:
                # str_data = util.dict_key_value(data, '=')
                # sign_data = str_data + 'timestamp=' + str(time)
                # if 'sign' in header and header['sign'] is None:
                #     sign = util.MD5(sign_data)
                #     header['sign'] = sign
                header = get_request_encryption(data, header)
                r = requests.get(url=url, headers=header, params=data)
        with allure.step('响应结果：'):
            # 以text格式打印出参
            response = r.json()
            real_msg = response.get('message')
        with allure.step('接口返回信息打印：'):
            log.info(
                "\n用例ID:{}\n请求方式:{}\n请求标题:{}\n请求端口:{}\n请求url:{}\n请求结果:{}\n预期结果:{}\n实际结果:{} ".format(
                    case_id, method,
                    case_title,
                    case_port,
                    r.url,
                    r.text,
                    expect_msg,
                    real_msg))
        with allure.step('接口实际返回接口与预期接口对比'):
            if real_msg == expect_msg:
                log.info('\n第{}条用例测试通过'.format(case_id))
                final_re = "passed"
            else:
                log.info('\n第{}条用例测试不通过'.format(case_id))
                final_re = "failed"
        log.info('-------------------------------------')
        util.write_result(path_dict.get('excel'), EXCEL_OUTSIDE, case_id + 1, 9, final_re)


if __name__ == '__main__':
    pytest.main(['test_interface.py', '-s'])
