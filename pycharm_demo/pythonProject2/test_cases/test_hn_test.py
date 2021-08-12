#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
from utils.my_logger import logger
from utils.read_config import conf
from utils.get_path import *
sys.path.append(oprate_dir)
import unittest
import subprocess
from selenium import webdriver
import hn
import time
import pytest
@pytest.mark.hn
class test_hn_suspect(unittest.TestCase):
    def setUp(cls):
        try:
            options = webdriver.ChromeOptions()
            options.add_argument("--window-size=1920,1080")
            options.add_argument("--start-maximized")
            # 无头模式
            options.add_argument('--headless')
            path = download_dir  # 读取配置文件中下载路径
            prefs = {'download.default_directory': r'%s' % path}
            options.add_experimental_option('prefs', prefs)
            cls.driver = webdriver.Chrome(options=options)  # chrome下载设置
            cls.driver.get(conf.get("web", "url-hn"))
            cls.driver.implicitly_wait(5)
            cls.driver.find_element_by_id('username').send_keys('system')
            cls.driver.find_element_by_id('password').send_keys('12345678')
            time.sleep(1)
            cls.driver.find_element_by_id('login-Button').click()
        except:
            logger.error("网络错误")
        else:
            logger.debug("河南非法营运登陆成功")
            time.sleep(3)

    def test_01(self):
        '''河南高度疑似车辆模板下载'''
        driver = self.driver
        time.sleep(2)
        driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[1]/div[2]/div/ul/li[1]/div').click()
        driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[1]/div[2]/div/ul/li[1]/ul/li[1]/div').click()
        frame = driver.find_element_by_name('zdjkclgl')
        driver.switch_to.frame(frame)
        driver.find_element_by_xpath('//*[@id="toolbar"]/button[1]').click()
        time.sleep(3)
        try:
            path = download_dir
            self.assertTrue(os.path.join('%s' % path, 'download.xlw'))
        except AssertionError:
            logger.exception("与预期不符，用例执行不通过")
            raise
        else:
            logger.info("断言成功,文件下载成功")
            os.remove(os.path.join('%s' % path, 'download.xlw'))
            logger.debug("状态复位，删除下载文件")
        driver.quit()

    def test_02(self):
        '''MQ推送预警 '''
        #会导致主线程中断，另起进程。
        # hn.add('豫A00001', 'ill_suspected_vehicle_record')
        for i in range(10):
            hn.add((("豫A0000%d") % i), 'ill_suspected_vehicle_record', 4)
            print(("豫A0000%d") % i)
        logger.info('增加MQ推送的车辆到疑似车辆库')
        cmd = 'python3 mqpush.py'
        p = subprocess.Popen(cmd, shell=True)
        return_code = p.wait()
        print (return_code)
        logger.warning("MQpush。sendOK，返回码：%s" % return_code)

    def test_03(self):
        '''检查预警信息是否存在此条预警'''
        driver = self.driver
        driver.find_element_by_xpath('/html/body/div/div[1]/div[1]/div/ul/li[2]/div').click()
        driver.find_element_by_xpath('/html/body/div/div[1]/div[1]/div/ul/li[2]/ul/li[3]/div/a/span[2]').click()
        frame = driver.find_element_by_name('yjxxcx')
        driver.switch_to.frame(frame)
        expinfo = '豫A00001'
        time.sleep(3)
        acuinfo = driver.find_element_by_xpath('//*[@id="tblResult"]/tbody/tr[1]/td[2]/span').text
        try:
            self.assertEqual(expinfo, acuinfo)
        except AssertionError:
            logger.exception("失败。期望预警总数：豫A00001，实际预警总数：%s", acuinfo)
            raise
        logger.info("断言成功, acuinfo: %s", acuinfo)
        driver.quit()

    @pytest.mark.hnreset
    def test_reset(self):
        '''重置测试数据'''
        try:
            hn.Delete('豫A00001','ill_suspected_vehicle_record')
            hn.Delete('豫A00001', 'ill_warn_record')
            hn.Delete('豫A00001', 'ill_vehicle_warn_info')
            hn.Delete('豫A00001', 'ill_warn_task')
        except:
            logger.exception("重置异常")
            raise
        logger.exception("重置成功！！！")




