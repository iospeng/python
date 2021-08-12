# coding utf-8

import time
import unittest
import logging
from selenium import webdriver
from Feifa_pacage.LY_Login import Logins
from Feifa_pacage.loggers import Log

driver_obj = Logins()
obj_log = Log()


class ShouYe(unittest.TestCase):

    def test_Control(self):
        """布控核查"""
        time.sleep(3)
        try:
            driver_obj.driver.find_element_by_xpath('/html/body/div/div[1]/div[1]/div/ul/li[2]/div/a/span[2]').click()
            time.sleep(1)
            '定位待核查列表'
            time.sleep(3)
            driver_obj.driver.find_element_by_xpath('/html/body/div/div[1]/div[1]/div/ul/li[2]/ul/li[1]/div').click()
            '定位输入框'
            time.sleep(3)
            iframe = driver_obj.driver.find_element_by_xpath("//iframe[@name='dzblb']")
            driver_obj.driver.switch_to.frame(iframe)
            print( '定位iframe')
            # driver_obj.driver.switch_to_frame()
            numbers = driver_obj.driver.find_element_by_xpath('//*[@id="defaultForm"]/div/div[1]/div/div/div[1]/input')
            print(numbers.text + '定位输入框')
            if numbers.text == '':
                numbers.send_keys('1060')
            else:
                numbers.clear()
                time.sleep(1)
                numbers.send_keys('1060')
            driver_obj.driver.find_element_by_xpath('//*[@id="select2-plateColor-container"]').click()
            time.sleep(1)
            driver_obj.driver.find_element_by_xpath('//*[@id="select2-plateColor-results"]/li[2]').click()
            time.sleep(1)
            driver_obj.driver.find_element_by_xpath('//*[@id="select2-vehicleType-container"]').click()
            time.sleep(1)
            driver_obj.driver.find_element_by_xpath('//*[@id="select2-vehicleType-results"]/li[3]').click()
            time.sleep(1)
            city = driver_obj.driver.find_element_by_xpath('//*[@id="defaultForm"]/div[5]/div/input')
            if city == '':
                city.send_keys('郑州')
            else:
                city.clear()
                time.sleep(1)
                city.send_keys('郑州')
            owner = driver_obj.driver.find_element_by_xpath('//*[@id="defaultForm"]/div[6]/div/input')
            if owner == '':
                owner.send_keys('无')
            else:
                owner.clear()
                time.sleep(1)
                owner.send_keys('无')
            driver_obj.driver.find_element_by_xpath('//*[@id="updatedDateS"]').click()
            time.sleep(1)
            driver_obj.driver.find_element_by_xpath('/html/body/div[3]/div[3]/table/tbody/tr[2]/td[4]').click()
            time.sleep(1)
            driver_obj.driver.find_element_by_xpath('//*[@id="updatedDateE"]').click()
            time.sleep(1)
            driver_obj.driver.find_element_by_name('/html/body/div[4]/div[3]/table/tbody/tr[2]/td[7]').click()
            time.sleep(1)
            driver_obj.driver.find_element_by_xpath('//*[@id="defaultForm"]/div[9]/div/button[1]').click()


        except:
            obj_log.write_error('定位布控核查按钮失败')
