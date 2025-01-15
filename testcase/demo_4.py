# @Time         : 2024/02/21 上午 10:26
# @Author       : ljx
# @File         : test_interface.py
# @Software     : PyCharm
import json
import os
import sys

sys.path.append(os.path.split(os.path.abspath(os.path.dirname(__file__)))[0])
import pytest
import requests
import allure
from utils import util
from utils.log import Log
from utils.util import post_request_encryption, get_request_encryption, setting_select, read_yaml
from config.allParams import EXCEL_OUTSIDE, TEST_USER_URL

log = Log()
SETTING = '24'
PORT = TEST_USER_URL


class TestInterface:
    @pytest.mark.parametrize("case", read_yaml(r"../testdata/test_user_case.yaml"))
    def test_interface(self, case):
        method = case["method"]
        interface = case["interface"]
        print(method, interface)


if __name__ == '__main__':
    # pytest.main(["--html=./report/report.html", "test_interface.py"], '-s')
    pytest.main(['--alluredir', 'report/1', 'test_interface.py'])
    split = 'allure' + 'generate' + './report/1' + '-0' + './report/html' + '--clean'
    os.system(split)
# pytest ./testcase/test_interface.py -s -q --alluredir=../report/1
#  allure generate --clean ./report -0 ./report
