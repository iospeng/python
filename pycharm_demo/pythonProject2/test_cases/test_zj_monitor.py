#!/usr/bin/env python
#-*-coding:utf-8-*-
import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
from utils.my_logger import logger
from utils.read_config import conf
from utils.get_path import *
sys.path.append(oprate_dir)
import pytest
import unittest
from report import make_report
from selenium import webdriver
import time
import oprate
class test_monitor(unittest.TestCase):
        def setUp(cls):
            try:
                # driver = webdriver.Chrome()
                logger.debug("Chrome浏览器打开")
                options = webdriver.ChromeOptions()
                # 无头模式
                options.add_argument("--window-size=1920,1080")
                options.add_argument("--start-maximized")
                options.add_argument('--headless')
                path = download_dir                                #读取配置文件中下载路径
                prefs = {'download.default_directory': r'%s' %path }
                options.add_experimental_option('prefs', prefs)
                cls.driver = webdriver.Chrome(options=options)     #chrome下载设置
                cls.driver.get(conf.get("web", "url"))
                cls.driver.implicitly_wait(5)
                cls.driver.find_element_by_id('username').send_keys('system')
                cls.driver.find_element_by_id('password').send_keys('12345678')
                time.sleep(1)
                cls.driver.find_element_by_id('login-Button').click()
            except :
                logger.error("网络错误")
            else :
                logger.debug("登陆成功")
                time.sleep(3)

        def test_monitorupload(self):
            '''监控车辆模板上传'''
            driver = self.driver
            time.sleep(2)
            # oprate.Delete('浙A00001', 'ill_suspected_vehicle_record')
            driver.find_element_by_xpath('/html/body/div/div/div[1]/div[2]/ul/li[2]/div/a/span[2]').click()
            frame = driver.find_element_by_name('jkclgl')
            driver.switch_to.frame(frame)
            path = os.path.join('%s' % upload_dir, '车辆导入模板.xlsx')
            driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[1]/div/div/form/input[1]').send_keys(path)
            logger.debug("选择上传文件")
            expinfo = "导入成功！"
            time.sleep(1)
            acuinfo = driver.find_element_by_xpath(
                '/html/body/div[4]').find_element_by_xpath('/html/body/div[6]/div[2]').text
            if expinfo == acuinfo:
                info = oprate.Serch('浙ATE001', 'ill_suspected_vehicle_record')
                assert info != None
                logger.info("断言成功,导入数据，库查询成功")
            else:
                try:
                    self.assertEqual(expinfo, acuinfo)
                except AssertionError:
                    logger.exception("失败")
                    raise
                else:
                    logger.info("断言成功, acuinfo: %s", acuinfo)
            oprate.Delete('浙ATE001', 'ill_suspected_vehicle_record')
            # 状态复位
            driver.quit()

        @pytest.mark.test
        def test_case(self):
            '''test only'''

            assert  1==1

if __name__=='__main__':
    make_report('test_zj_monitor.py')


