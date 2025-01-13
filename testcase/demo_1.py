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
from config.allParams import TEST_OPERA_URL

getToken = Element('Token')
setting = '24'
log = Log()


class TestInterface:
    def test_interface(self):
        pass


if __name__ == '__main__':
    pytest.main(['test_interface.py', '-s'])
