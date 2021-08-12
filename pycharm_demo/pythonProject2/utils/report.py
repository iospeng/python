#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import unittest
from BeautifulReport import BeautifulReport
from utils.my_logger import logger
from utils.get_path import *
from scp import SCPClient
import paramiko
import os
import time

def make_report(name):
    base_dir = os.path.split(os.path.split(os.path.abspath(__file__))[0])[0]
    report_dir = os.path.join(base_dir, 'test_report')
    logger.debug("报告输出模块：获取当前脚本路径")
    s = unittest.TestLoader().discover(start_dir=case_dir, pattern=name)
    logger.debug("testsuit填充用例，%s", s)
    print('*'*25,'测试开始','*'*25)
    br = BeautifulReport(s)
    filename = time.strftime("%Y-%m-%d_%H:%M:%S") + r".html"
    logger.debug("报告输出模块：设置报告格式")
    br.report(filename=filename, description='回归用例自动化测试报告', report_dir=report_dir)
    try:
        file = os.path.join('%s' % report_dir, filename)
        ssh = paramiko.SSHClient()
        ssh.load_system_host_keys()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname='192.168.90.162', port=22, username='deploy', password='linkcld123456')
        scpclient = SCPClient(ssh.get_transport(), socket_timeout=15.0)
        scp = SCPClient(ssh.get_transport())
        scp.put(file, recursive=True, remote_path='/linkcld/uploadfile/report.html')
        scp.close()
    except:
        logger.exception("上传报告失败")
    else:
        logger.info("报告已上传192.168.90.162/linkcld/uploadfile/report.html")