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
import unittest
from selenium import webdriver
from report import make_report
import time
import requests
import pytest
import json
import oprate


class test_warninfo(unittest.TestCase):
    global number
    def setUp(cls):
        try:
            logger.debug("Chrome浏览器打开")
            options = webdriver.ChromeOptions()
            # 无头模式
            options.add_argument("--window-size=1920,1080")
            options.add_argument("--start-maximized")
            options.add_argument('--headless')
            path = download_dir  # 读取配置文件中下载路径
            prefs = {'download.default_directory': r'%s' % path}
            options.add_experimental_option('prefs', prefs)
            cls.driver = webdriver.Chrome(options=options)  # chrome下载设置
            cls.driver.get(conf.get("web", "url"))
            cls.driver.implicitly_wait(5)
            cls.driver.find_element_by_id('username').send_keys('system')
            cls.driver.find_element_by_id('password').send_keys('12345678')
            time.sleep(1)
            cls.driver.find_element_by_id('login-Button').click()
            #进入布控抓捕页面
            cls.driver.find_element_by_xpath('/html/body/div/nav/div/div[2]/ul[1]/li[4]/a').click()
        except:
            logger.exception("网络错误")
        else:
            logger.debug("登陆成功")
            time.sleep(3)

    # @pytest.mark.run(order=1) #用例执行顺序
    @pytest.mark.data
    @pytest.mark.smt
    def test_1warninfopush(self):
        '''预警信息接口推送'''
        for i in range(10):
            oprate.Add_suspect((("浙A0000%d") % i), 'ill_suspected_vehicle_record', 4)
            print(("浙A0000%d") % i)
            try:
                url = 'http://192.168.90.163:9303/illegal-rest/api/vehicle/warn'
                headers = {
                    'Content-Type': 'application/json'
                }  # 数据头
                body = {
                    "enStationId": "18ced6ee-daad-11ea-b55a-0242ac180002",
                    "enStationName": "桐乡西",
                    "gantryId": "3237",
                    "gantryName": "高速卡口",
                    "imgUrl": "",
                    "passTime": str(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))),
                    "plateColor": 2,
                    "plateNumber": (("浙A0000%d") % i),
                    "sid": "G001533010001200102020120318101100",
                    "type": "",
                    "vehicleType": "4",
                }
                response = requests.post(url, data=json.dumps(body), headers=headers)
                assert response.status_code == 200
            except AssertionError:
                logger.exception("接口推送预警失败：%s",response.status_code)
                raise
            else:
                logger.info("预警信息推送成功：%s,%s", response.status_code, (("浙A0000%d") % i))

    @pytest.mark.flaky(reruns=3, reruns_delay=2)
    @pytest.mark.data
    @pytest.mark.smt
    def test_check2(self):
        '''检查实时预警总数'''
        driver = self.driver
        driver.find_element_by_xpath('/html/body/div/div/div[1]/div[2]/ul/li[3]/div/a/span[2]').click()
        frame = driver.find_element_by_name('ssyj')
        driver.switch_to.frame(frame)
        expinfo = '10'
        time.sleep(3)
        acuinfo = driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/h4/a/span[2]').text
        try:
            self.assertEqual(expinfo, acuinfo)
        except AssertionError:
            logger.exception("期望预警总数：10，实际预警总数：%s",acuinfo)
            raise
        else:
            logger.info("断言成功, acuinfo: %s", acuinfo)
        driver.quit()

    @pytest.mark.flaky(reruns=3, reruns_delay=2)
    @pytest.mark.data
    @pytest.mark.smt
    def test_check3(self):
        '''检查预警信息排序'''
        driver = self.driver
        driver.find_element_by_xpath('/html/body/div/div/div[1]/div[2]/ul/li[3]/div/a/span[2]').click()
        frame = driver.find_element_by_name('ssyj')
        driver.switch_to.frame(frame)
        expinfo = '浙A00009'
        time.sleep(3)
        acuinfo = driver.find_element_by_xpath(
            '/html/body/div[2]/div/div[2]/div/div[1]/div/ul/li[1]/div/div[1]/h4').text
        try:
            self.assertEqual(expinfo, acuinfo)
        except AssertionError:
            logger.exception("期望预警车辆：10，实际：%s", acuinfo)
            raise
        else:
            logger.info("断言成功, acuinfo: %s", acuinfo)
        driver.quit()

    @pytest.mark.smt
    def test_check4(self):
        '''桐乡西卡口预警地市：嘉兴市'''
        driver = self.driver
        frame = driver.find_element_by_name('yjrw')
        driver.switch_to.frame(frame)
        expinfo = '嘉兴市'
        acuinfo = driver.find_element_by_xpath(
            '/html/body/div[1]/div[1]/div[2]/div[2]/table/tbody/tr[1]/td[7]/span').text
        try:
            self.assertEqual(expinfo, acuinfo)
        except AssertionError:
            logger.exception("桐乡西卡口预警地市期望：'嘉兴市'，实际：%s", acuinfo)
            raise
        else:
            logger.info("断言成功, acuinfo: %s", acuinfo)
        driver.quit()

    @pytest.mark.smt
    def test_check5(self):
        '''预警任务操作'''
        driver = self.driver
        frame = driver.find_element_by_name('yjrw')
        driver.switch_to.frame(frame)
        try:
            try:
                acuinfo1 = driver.find_element_by_xpath(
                    '/html/body/div[1]/div[1]/div[2]/div[2]/table/tbody/tr[2]/td[11]/button[1]').text
            except:
                acuinfo1 = ''
            try:
                acuinfo2 =  driver.find_element_by_xpath(
                '/html/body/div[1]/div[1]/div[2]/div[2]/table/tbody/tr[2]/td[11]/button[2]').text
            except:
                 acuinfo2 = ''
            try:
                acuinfo3 = driver.find_element_by_xpath(
                    '/html/body/div[1]/div[1]/div[2]/div[2]/table/tbody/tr[2]/td[11]/button[3]').text
            except:
                acuinfo3 = ''
            try:
                acuinfo4 = driver.find_element_by_xpath(
                    '/html/body/div[1]/div[1]/div[2]/div[2]/table/tbody/tr[2]/td[11]/button[4]').text
            except:
                acuinfo4 = ''
            try:
                acuinfo5 = driver.find_element_by_xpath(
                    '/html/body/div[1]/div[1]/div[2]/div[2]/table/tbody/tr[2]/td[11]/button[5]').text
            except:
                acuinfo5 = ''
            list1 = [acuinfo1,acuinfo2,acuinfo3,acuinfo4,acuinfo5]
            list2 = ["认领","布控","处理","布控推荐","详情"]
        except:
            logger.exception("元素定位失败")
        else:
            try:
                self.assertEqual((list2), (list1))
            except AssertionError:
                logger.exception("期望：5，实际：%s", list1)
                raise
            else:
                logger.info("断言成功, acuinfo: %s", list1)
            driver.quit()

    @pytest.mark.smt
    def test_check6(self):
        '''预警任务布控——认领成功操作'''
        driver = self.driver
        frame = driver.find_element_by_name('yjrw')
        driver.switch_to.frame(frame)
        no = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div[2]/table/tbody/tr[2]/td[2]').text
        driver.find_element_by_xpath(
            '/html/body/div[1]/div[1]/div[2]/div[2]/table/tbody/tr[2]/td[11]/button[1]').click()

        time.sleep(1)
        try:
            try:
                acuinfo1 = driver.find_element_by_xpath(
                    '/html/body/div[1]/div[1]/div[2]/div[2]/table/tbody/tr[1]/td[11]/button[1]').text
            except:
                acuinfo1 = ''
            try:
                acuinfo2 = driver.find_element_by_xpath(
                    '/html/body/div[1]/div[1]/div[2]/div[2]/table/tbody/tr[1]/td[11]/button[2]').text
            except:
                acuinfo2 = ''
            try:
                acuinfo3 = driver.find_element_by_xpath(
                    '/html/body/div[1]/div[1]/div[2]/div[2]/table/tbody/tr[1]/td[11]/button[3]').text
            except:
                acuinfo3 = ''
            try:
                acuinfo4 = driver.find_element_by_xpath(
                    '/html/body/div[1]/div[1]/div[2]/div[2]/table/tbody/tr[1]/td[11]/button[4]').text
            except:
                acuinfo4 = ''
            try:
                acuinfo5 = driver.find_element_by_xpath(
                    '/html/body/div[1]/div[1]/div[2]/div[2]/table/tbody/tr[1]/td[11]/button[5]').text
            except:
                acuinfo5 = ''
            try:
                no2 = driver.find_element_by_xpath(
                    '/html/body/div[1]/div[1]/div[2]/div[2]/table/tbody/tr[1]/td[2]').text
            except:
                no2 = ''

            list1 = [acuinfo1, acuinfo2, acuinfo3, acuinfo4, acuinfo5,no2]
            list2 = ["布控" ,"处理", "布控推荐", "详情","",no]
        except:
            logger.exception("元素定位失败")
        else:
            try:
                self.assertEqual((list2), (list1))
            except AssertionError:
                logger.exception("期望：5，实际：%s", list1)
                raise
            else:
                logger.info("断言成功, acuinfo: %s", list1)
            driver.quit()

    @pytest.mark.smt
    def test_check7(self):
        '''预警任务布控——布控成功操作'''
        driver = self.driver
        frame = driver.find_element_by_name('yjrw')
        driver.switch_to.frame(frame)
        no = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div[2]/table/tbody/tr[2]/td[2]').text
        driver.find_element_by_xpath(
            '/html/body/div[1]/div[1]/div[2]/div[2]/table/tbody/tr[2]/td[11]/button[2]').click()
        driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/form/div/div/span/span[1]/span/ul').click()
        driver.find_element_by_xpath('/html/body/span/span/span/ul/li[1]').click()
        driver.find_element_by_xpath('/html/body/span/span/span/ul/li[513]').click()
        driver.find_element_by_xpath('/html/body/div[4]').click()
        driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[1]').click()
        time.sleep(5)
        try:
            try:
                acuinfo1 = driver.find_element_by_xpath(
                    '/html/body/div[1]/div[1]/div[2]/div[2]/table/tbody/tr[1]/td[11]/button[1]').text
            except:
                acuinfo1 = ''
            try:
                acuinfo2 = driver.find_element_by_xpath(
                    '/html/body/div[1]/div[1]/div[2]/div[2]/table/tbody/tr[1]/td[11]/button[2]').text
            except:
                acuinfo2 = ''
            try:
                acuinfo3 = driver.find_element_by_xpath(
                    '/html/body/div[1]/div[1]/div[2]/div[2]/table/tbody/tr[1]/td[11]/button[3]').text
            except:
                acuinfo3 = ''
            try:
                acuinfo4 = driver.find_element_by_xpath(
                    '/html/body/div[1]/div[1]/div[2]/div[2]/table/tbody/tr[1]/td[11]/button[4]').text
            except:
                acuinfo4 = ''
            try:
                acuinfo5 = driver.find_element_by_xpath(
                    '/html/body/div[1]/div[1]/div[2]/div[2]/table/tbody/tr[1]/td[11]/button[5]').text
            except:
                acuinfo5 = ''
            try:
                no2 = driver.find_element_by_xpath(
                    '/html/body/div[1]/div[1]/div[2]/div[2]/table/tbody/tr[1]/td[2]').text
            except:
                no2 = ''

            list1 = [acuinfo1, acuinfo2, acuinfo3, acuinfo4, acuinfo5, no2]
            list2 = [ "处理", "布控推荐", "详情", "", "",no]
        except:
            logger.exception("元素定位失败")
            raise
        else:
            try:
                self.assertEqual((list2), (list1))
            except AssertionError:
                logger.exception("期望：5，实际：%s，该用例失败会导致测试类后续用例失败", list1)
                raise
            else:
                logger.info("断言成功, acuinfo: %s", list1)

            driver.quit()

    def test_check8(self):
        '''预警任务布控——布控/认领失效'''

        pass

    @pytest.mark.smt
    def test_check9(self):
        '''预警任务布控——车辆扭转黑名单页面显示'''
        driver = self.driver
        frame = driver.find_element_by_name('yjrw')
        driver.switch_to.frame(frame)
        expno = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div[2]/table/tbody/tr[4]/td[2]').text
        driver.find_element_by_xpath(
            '/html/body/div[1]/div[1]/div[2]/div[2]/table/tbody/tr[4]/td[11]/button[3]').click()
        driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/form/div[3]/div/span/span[1]/span/span[1]').click()
        driver.find_element_by_xpath('/html/body/span/span/span/ul/li[10]').click()
        driver.find_element_by_xpath('/html/body/div[5]').click()
        driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/form/div[4]/div/textarea').send_keys('自动化测试脚本添加1228238973qjbdkjbqwdhb')
        #上传附件
        #######
        driver.find_element_by_xpath('/html/body/div[5]/div/div/div[3]/button[1]').click()
        time.sleep(5)
        acuno = driver.find_element_by_xpath(
                    '/html/body/div[1]/div[1]/div[2]/div[2]/table/tbody/tr[1]/td[2]').text
        status = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div[2]/table/tbody/tr[1]/td[6]/span').text
        try:
            self.assertEqual((expno), (acuno))
        except AssertionError:
            logger.exception("期望：%s，实际：%s，该用例失败会导致测试类后续用例失败",expno, acuno)
            raise
        else:
            logger.info("断言成功, acuinfo: %s,%s", acuno,status)
        driver.quit()

    @pytest.mark.smt
    def test_check91(self):
        '''预警任务布控——前置条件check8，检查黑名单页面数据'''
        driver = self.driver
        frame = driver.find_element_by_name('yjrw')
        driver.switch_to.frame(frame)
        number = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div[2]/table/tbody/tr[1]/td[3]').text
        #跳出当前框架
        driver.switch_to.default_content()
        driver.find_element_by_xpath('/html/body/div/nav/div/div[2]/ul[1]/li[2]/a').click()
        frame = driver.find_element_by_name('yccclgl')
        driver.switch_to.frame(frame)
        driver.find_element_by_xpath('/html/body/form/div[1]/div/input').send_keys(number)
        driver.find_element_by_xpath('/html/body/form/div[8]/div/button[1]').click()
        try:
            acu = driver.find_element_by_xpath(
                '/html/body/div[1]/div[1]/div[2]/div[2]/table/tbody/tr/td[2]').text
        except:
            logger.exception('获取黑名单搜索结果元素失败，查询车辆：%s',number)
            raise
        else:
            logger.info('黑名单实际数据：%s，期望数据：%s',acu,number)
        driver.quit()

    @pytest.mark.smt
    @pytest.mark.reset
    def test_reset(self):
        ''' 重置测试数据'''
        try:
            for i in range(10):
                oprate.Delete((("浙A0000%d") % i), 'ill_suspected_vehicle_record')
                oprate.Delete((("浙A0000%d") % i), 'ill_warn_record')
                oprate.Delete((("浙A0000%d") % i), 'ill_vehicle_warn_info')
                oprate.Delete((("浙A0000%d") % i), 'ill_warn_task')
                print(("浙A0000%d") % i)
        except:
            logger.exception('reset faliur！！！')
            raise
        else:
            logger.info('reset success')



if __name__=='__main__':
    make_report('test_zj_datatest.py')












