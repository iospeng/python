#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
from utils.my_logger import logger
from report import make_report
from utils.read_config import conf
from utils.get_path import *
sys.path.append(oprate_dir)
import unittest
from selenium import webdriver
import pytest
import time
import oprate
@pytest.mark.parametrize('user',["刘一", "刘二"])
class test_mainpage(unittest.TestCase):
        def setUp(cls):
            try:
                options = webdriver.ChromeOptions()
                options.add_argument("--window-size=1920,1080")
                options.add_argument("--start-maximized")
                # 无头模式
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


        @pytest.mark.smt
        @pytest.mark.run(order=1)
        def test_loginsystem(self):
            '''浙江非法营运system角色登陆成功'''
            driver = self.driver
            expinfo = "欢迎，超级管理员"
            driver.implicitly_wait(3)
            acuinfo =  driver.find_element_by_xpath('/html/body/div/nav/div/div[2]/ul[2]/li[1]/a').text
            try:
                self.assertEqual(expinfo,acuinfo)
            except AssertionError:
                logger.exception("与预期不符，用例执行不通过")
                raise
            else:
                logger.info("断言成功")
                #状态复位
            driver.quit()


        @pytest.mark.test
        @pytest.mark.smt
        @pytest.mark.run(order=2)
        @pytest.mark.parametrize('user',["刘一", "刘二"])
        def test_login(self,user):
            '''浙江非法营运地市账号登陆'''
            driver = self.driver
            driver.find_element_by_xpath('/html/body/div/nav/div/div[2]/ul[2]/li[2]/a').click()
            driver.find_element_by_id('username').send_keys(user)
            driver.find_element_by_id('password').send_keys()
            driver.find_element_by_id('login-Button').click()
            driver.implicitly_wait(3)
            expinfo = "欢迎，刘一" or "欢迎，刘二"
            acuinfo = driver.find_element_by_xpath('/html/body/div/nav/div/div[2]/ul[2]/li[1]/a').text
            try:
                self.assertEqual(expinfo, acuinfo)
            except AssertionError:
                logger.exception("与预期不符，用例执行不通过")
                raise
            else:
                logger.info("断言成功")
                # 状态复位
            driver.quit()

        @pytest.mark.smt
        def test_suspectupload(self):
            '''疑似车辆模板上传'''
            driver = self.driver
            time.sleep(2)
            # oprate.Delete('浙A00001', 'ill_suspected_vehicle_record')
            frame = driver.find_element_by_name('ysclgl')
            driver.switch_to.frame(frame)
            path = os.path.join('%s' %upload_dir,'车辆导入模板.xlsx')
            driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[1]/div/div/form/input[1]').send_keys(path)
            logger.debug("选择上传文件")
            expinfo = "导入成功！"
            time.sleep(3)
            acuinfo = driver.find_element_by_xpath(
                '/html/body/div[4]').find_element_by_xpath('/html/body/div[6]/div[2]').text
            if expinfo == acuinfo:
                info = oprate.Serch('浙ATE001','ill_suspected_vehicle_record')
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

        def test_suspectserch(self):
            '''疑似车辆页面车牌筛选器'''
            oprate.Add_suspect('浙A00001','ill_suspected_vehicle_record',2)
            logger.info("插入车牌浙A00001，level=2")
            driver = self.driver
            frame = driver.find_element_by_name('ysclgl')
            driver.switch_to.frame(frame)
            driver.find_element_by_xpath('/html/body/form/div[1]/div/input').send_keys('浙A00001')
            driver.find_element_by_xpath('/html/body/form/div[9]/div/button[1]').click()
            expinfo = "浙A00001"
            acuinfo = driver.find_element_by_xpath(
                '/html/body/div[1]/div[1]/div[2]/div[2]/table/tbody/tr[1]/td[2]/span').text
            try:
                self.assertEqual(expinfo,acuinfo)
            except AssertionError:
                logger.exception("与预期不符，用例执行不通过")
                raise
            else:
                logger.info("断言成功, acuinfo: %s", acuinfo)
                oprate.Delete('浙A00001','ill_suspected_vehicle_record')
                #状态复位
            driver.quit()

        @pytest.mark.smt
        def test_suspectdownload(self):
            '''疑似车辆模板下载'''
            driver = self.driver
            time.sleep(2)
            frame = driver.find_element_by_name('ysclgl')
            driver.switch_to.frame(frame)
            driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[1]/div/div/button[1]').click()
            time.sleep(3)
            try:
                path = download_dir
                self.assertTrue(os.path.join('%s' %path,'车辆导入模板.xlsx'))
            except AssertionError:
                logger.exception("与预期不符，用例执行不通过")
                raise
            else:
                logger.info("断言成功,文件下载成功")
                os.remove(os.path.join('%s' %path,'车辆导入模板.xlsx'))
                logger.debug("状态复位，删除下载文件")
            driver.quit()

if __name__=='__main__':
    make_report('test_zj_suspect.py')



