#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import os

from selenium.webdriver.common.by import By

from utils.times import dt_strftime


class ConfigManager(object):
    # 项目目录
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # 页面元素目录
    ELEMENT_PATH = os.path.join(BASE_DIR, 'yaml')

    # 报告文件
    REPORT_FILE = os.path.join(BASE_DIR, 'reports.html')

    # 元素定位的类型
    LOCATE_MODE = {
        'css': By.CSS_SELECTOR,
        'xpath': By.XPATH,
        'name': By.NAME,
        'id': By.ID,
        'class': By.CLASS_NAME,
        'link_text': By.PARTIAL_LINK_TEXT,
        'tag_name': By.TAG_NAME
    }

    # 邮件信息
    EMAIL_INFO = {
        'username': '',  # 切换成你自己的地址
        'password': '',
        'smtp_host': '测试',
        'smtp_port': 465
    }

    # 收件人
    ADDRESSEE = [
        '2222224647@qq.com',
    ]

    @property
    def log_file(self):
        """日志目录"""
        log_dir = os.path.join(self.BASE_DIR, 'logs')
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)
        return os.path.join(log_dir, '{}.log'.format(dt_strftime()))

    @property
    def ini_file(self):
        """配置文件"""
        ini_file = os.path.join(self.BASE_DIR, 'config', 'config.ini')
        if not os.path.exists(ini_file):
            raise FileNotFoundError("配置文件%s不存在！" % ini_file)
        return ini_file


cm = ConfigManager()
if __name__ == '__main__':
    print(cm.BASE_DIR)
