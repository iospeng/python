# -*- coding: utf-8 -*-
# @Project : Compliance
# @File    : seat_register.py
# @Software: PyCharm
# @Author  : Lizhipeng
# @Email   : 1907878011@qq.com
# @Time    : 2021/10/26 15:58
import time
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from loggers.loggers import Loggers
from po.drivers import Drivers


class SeatRegister(Drivers):
    base_url = 'http://192.168.90.162:8090/ims-pro/'
    logs = Loggers()

    # 通过行政区划，判断展示数据是否是郑州
    def seat_register(self):
        """
        定位第一条数据，看第一条数据是否是登录账号的新政区划
        拿到第一条数据的新政区划
        :return:
        """
        sleep(2)
        self.frame_switch('iframe', 0)

        # 显示等待
        def wait(x):
            return len(self.driver.find_elements(By.XPATH, '//*[@id="table"]/tbody/tr/td[2]')) >= 1
        WebDriverWait(self.driver, 50).until(wait)
        try:
            ele = self.findtext(By.XPATH, '//*[@id="table"]/tbody/tr/td[2]').text
        except:
            self.logs.write_error('座位排查对比登记表，获取第一条数据新政区划失败')
        else:
            self.driver.switch_to.default_content()
            return ele

    # 通过附件名称，判断附件是否上传
    def test_file_yesorno(self):
        sleep(2)
        # 切换frame
        self.frame_switch('iframe', 0)
        sleep(2)

        # 显示等待
        def wait(x):
            return len(self.driver.find_elements(By.XPATH, '//*[@id="table"]/tbody/tr/td[6]/span[1]')) >= 1

        try:
            WebDriverWait(self.driver, 5).until(wait)
        except:
            print('附件未上传')
            # 返回原frame
            self.driver.switch_to.default_content()
        else:
            print('附件已上传')
            try:
                ele = self.findtext(By.XPATH, '//*[@id="table"]/tbody/tr/td[6]/span[1]').text
            except:
                self.logs.write_error('座位排查对比登记表，定位附件名称失败')
            else:
                # 返回原frame
                self.driver.switch_to.default_content()
                return ele

    # 图片已上传，点击替换附件
    def test_file_replace(self):
        sleep(2)
        # 切换frame
        self.frame_switch('iframe', 0)
        sleep(2)
        try:
            self.findtext(By.XPATH, '//*[@id="table"]/tbody/tr/td[6]/span[2]').click()
            sleep(1)
            self.findtext(By.XPATH, '//*[@id="fileUploadAde"]').send_keys(
                r'E:\Download\git\project\python\pycharm_demo\Compliance\files\项目部署.pdf')
            sleep(5)
            self.findtext(By.XPATH, '//*[@id="attachmentModal"]/div/div/div[3]/button[2]').click()
            sleep(2)
            # self.findtext(By.XPATH, '//*[@id="layui-layer2"]/div[3]/a[1]').click()
            self.findtext(By.XPATH, '//*[@id="layui-layer2"]/div[3]/a[2]').click()
        except:
            self.logs.write_error('座位排查对比登记表，定位上传附件失败')
        else:
            sleep(5)
            # 返回原frame
            self.driver.switch_to.default_content()
