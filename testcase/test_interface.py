# @Time         : 2024/02/21 上午 10:26
# @Author       : ljx
# @File         : test_interface.py
# @Software     : PyCharm
import json
import os
import sys

from config.allParams import USER_YAML

sys.path.append(os.path.split(os.path.abspath(os.path.dirname(__file__)))[0])
import pytest
import requests
import allure
from utils import util
from utils.log import Log
from utils.util import post_request_encryption, get_request_encryption, setting_select, read_yaml

log = Log()
SETTING = '24'
PORT = '买家'


class TestInterface:
    # class TestInterface:
    @pytest.mark.parametrize("cases", read_yaml(USER_YAML))
    def test_interface(self, cases):
        path_dict = setting_select(SETTING, PORT)
        time = util.timestamp()
        url = path_dict.get('url')
        url = url + cases['interface'] + '?timestamp=' + str(time)
        # 动态获取参数生成标题
        allure.dynamic.title(cases['title'])
        with allure.step('判断请求方式'):
            if cases["method"] == 'post':
                # 把sign加密到请求头,把sk var 加密传参到data
                data_dict = post_request_encryption(cases['data'], cases['header'], time)
                # 将数据转换成JSON格式字符串
                json_data = json.dumps(data_dict.get('data'))
                # 使用requests发送post请求
                r = requests.post(url=url, headers=data_dict.get('headers'), data=json_data)
            else:
                header = get_request_encryption(cases['data'], cases['header'], time)
                r = requests.get(url=url, headers=header, params=cases['data'])
        with allure.step('响应结果：'):
            # 以text格式打印出参
            response = r.json()
            real_msg = response.get('message')
        with allure.step('接口返回信息打印：'):
            log.info(
                "\n请求方式:{}\n请求标题:{}\n\n请求url:{}\n请求结果:{}\n预期结果:{}\n实际结果:{} ".format(
                    cases["method"],
                    cases['title'],
                    r.url,
                    r.text,
                    cases['message'],
                    real_msg))
        with allure.step('接口实际返回接口与预期接口对比'):
            if real_msg == cases['message']:
                log.info('\n标题为 {} 用例测试通过'.format(cases['title']))
                # final_re = "passed"
            else:
                log.info('\n标题为 {} 用例测试不通过'.format(cases['title']))
                # final_re = "failed"
        log.info('-------------------------------------')
        # util.write_result(path_dict.get('excel'), EXCEL_OUTSIDE, case_id + 1, 9, final_re)


if __name__ == '__main__':
    # pytest.main(["--html=./report/report.html", "test_interface.py"], '-s')
    pytest.main(['--alluredir', 'report/1', 'test_interface.py'])
    split = 'allure' + 'generate' + './report/1' + '-0' + './report/html' + '--clean'
    os.system(split)
# pytest ./testcase/test_interface.py -s -q --alluredir=./report/1
#  allure generate --clean ./report -0 ./report
