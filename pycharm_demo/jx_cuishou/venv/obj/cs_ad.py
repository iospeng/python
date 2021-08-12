# -*- coding:utf-8 -*-

from selenium import webdriver
import unittest
import HTMLTestRunner
import time
from obj.one import Login
import os
from obj.Image import Images
from selenium.webdriver.support.ui import Select
# from obj.ErrorC import Error_Class


login_obj = Login()
img = Images()


class cs_admin(unittest.TestCase):

    # 网页对象操作：
    #  click()  点击对象
    #  send_keys("xxx") 在对象上模拟按键输入
    #  clear() 用于清除输入框的内容，比如百度输入框里默认有个“请输入关键字”的信息，
    #            再比如我们的登陆框一般默认会有“账号”“密码”这样的默认信息。
    #            clear 可以帮助我们清除这些信息。
    #  submit() 提交表单
    #  text  获取该元素的文本
    #  get_attribute("属性名，如name")   获得属性值


    def test_b_query(self):
        u"""催收管理模块(查询)"""
        # 借款编号查询
        time.sleep(5)
        login_obj.driver.find_element_by_xpath('//*[@id="navMenu"]/ul/li[2]/a/span').click()  # 定位‘催收管理’
        time.sleep(5)
        login_obj.driver.find_element_by_xpath('//*[@id="sidebar"]/div/div[2]/ul/li[1]/div/a').click()  # 定位‘我的催收订单’
        time.sleep(1)
        login_obj.driver.find_element_by_xpath('//*[@id="loanId"]').send_keys('1213263')  # 定位‘借款编号’输入框，并输入值
        time.sleep(1)
        login_obj.driver.find_element_by_xpath('//*[@id="pagerForm"]/div[1]/div/table/tbody/tr[4]/td[3]/div/div/button').click() # 定位查询按钮
        time.sleep(1)
        order_test = login_obj.driver.find_element_by_xpath('//*[@id="cs_list_box"]/tr/td[2]').text  # 获取查询结果第一条中的借款编号
        # 验证截图
        img.get_img('借款单号查询查询成功,借款编号为：', '借款订单号查询失败，借款编号为：', order_test, '1213263')

        # 借款人姓名查询
        time.sleep(5)
        login_obj.driver.find_element_by_xpath('//*[@id="loanId"]').clear() # 清空‘借款编号’
        time.sleep(1)
        login_obj.driver.find_element_by_xpath('//*[@id="loanRealName"]').send_keys('李志鹏') # 定位‘借款人姓名’输入框，并输入值
        time.sleep(1)
        login_obj.driver.find_element_by_xpath('//*[@id="pagerForm"]/div[1]/div/table/tbody/tr[4]/td[3]/div/div/button').click() # 定位查询按钮
        time.sleep(1)
        name_test = login_obj.driver.find_element_by_xpath('//*[@id="cs_list_box"]/tr/td[3]').text # #获取查询结果第一条中的借款人姓名
        # 验证截图
        img.get_img('借款人姓名查询查询成功，姓名为：', '借款人姓名查询失败，姓名为：', name_test, '李志鹏')

        #手机号查询
        # login_obj.driver.find_element_by_xpath('//*[@id="loanId"]').clear()
        # time.sleep(1)
        login_obj.driver.find_element_by_xpath('//*[@id="loanRealName"]').clear()  # 清空‘借款人姓名’
        time.sleep(1)
        login_obj.driver.find_element_by_xpath('//*[@id="pagerForm"]/div[1]/div/table/tbody/tr[1]/td[3]/input').send_keys('15671278825') # 定位‘借款人手机号’输入框，并输入值
        time.sleep(1)
        login_obj.driver.find_element_by_xpath('//*[@id="pagerForm"]/div[1]/div/table/tbody/tr[4]/td[3]/div/div/button').click() # 定位查询按钮
        time.sleep(1)
        num_test = login_obj.driver.find_element_by_xpath('//*[@id="cs_list_box"]/tr/td[4]').text[0:11] # 获取查询结果第一条中的手机号（截取前11位）
        # 验证截图
        img.get_img('手机号查询成功，手机号为：','手机号查询失败，手机号为：',num_test,'15671278825')

        # 催收时间查询
        # 开始时间
        login_obj.driver.find_element_by_xpath('//*[@id="pagerForm"]/div[1]/div/table/tbody/tr[1]/td[3]/input').clear() # 清空手机号
        time.sleep(1)
        login_obj.driver.find_element_by_xpath('//*[@id="collectionBeginTime"]').click() # 定位催收时间‘开始时间’选择框
        time.sleep(1)
        login_obj.driver.find_element_by_xpath('//*[@id="calendar"]/div/div[1]/table/tbody/tr/td[1]/select').click() # 定位时间框中的‘年份’下拉框
        time.sleep(1)
        login_obj.driver.find_element_by_xpath('//*[@id="calendar"]/div/div[1]/table/tbody/tr/td[1]/select/option[118]').click() # 定位 ‘年份’下拉框中的‘2017’年
        time.sleep(1)
        login_obj.driver.find_element_by_xpath('//*[@id="calendar"]/div/div[1]/table/tbody/tr/td[2]/select').click() # 定位时间框中的‘月份’下拉框
        time.sleep(1)
        login_obj.driver.find_element_by_xpath('//*[@id="calendar"]/div/div[1]/table/tbody/tr/td[2]/select/option[1]').click() # 定位‘月份’下拉框中的‘1’月
        time.sleep(1)
        login_obj.driver.find_element_by_xpath('//*[@id="calendar"]/div/div[2]/dl[2]/dd[6]').click() # 定位时间框中的1号
        time.sleep(1)
        # 结束时间
        login_obj.driver.find_element_by_xpath('//*[@id="collectionEndTime"]').click() # 定位催收时间‘结束时间’选择框
        time.sleep(1)
        login_obj.driver.find_element_by_xpath('//*[@id="calendar"]/div/div[1]/table/tbody/tr/td[1]/select').click() # 定位时间框中的‘年份’下拉框
        time.sleep(1)
        login_obj.driver.find_element_by_xpath('//*[@id="calendar"]/div/div[1]/table/tbody/tr/td[1]/select/option[119]').click() #定位 ‘年份’下拉框中的‘2018’年
        time.sleep(1)
        login_obj.driver.find_element_by_xpath('//*[@id="calendar"]/div/div[1]/table/tbody/tr/td[2]/select').click() # 定位时间框中的‘月份’下拉框
        time.sleep(1)
        login_obj.driver.find_element_by_xpath('//*[@id="calendar"]/div/div[1]/table/tbody/tr/td[2]/select/option[11]').click() # 定位‘月份’下拉框中的‘11’月
        time.sleep(1)
        login_obj.driver.find_element_by_xpath('//*[@id="calendar"]/div/div[2]/dl[2]/dd[33]').click() # 定位时间框中的31号
        time.sleep(1)
        login_obj.driver.find_element_by_xpath('//*[@id="pagerForm"]/div[1]/div/table/tbody/tr[4]/td[3]/div/div/button').click() # 定位查询按钮
        time.sleep(1)

        #派单时间查询
        # 清空上一步
        login_obj.driver.find_element_by_xpath('//*[@id="collectionBeginTime"]').click() # 定位催收时间‘开始时间’选择框
        time.sleep(1)
        login_obj.driver.find_element_by_xpath('//*[@id="calendar"]/div/div[3]/button[1]').click() # 定位催收时间查询，开始时间的时间框中的清空按钮
        time.sleep(1)
        login_obj.driver.find_element_by_xpath('//*[@id="collectionEndTime"]').click() # 定位催收时间‘结束时间’选择框
        time.sleep(1)
        login_obj.driver.find_element_by_xpath('//*[@id="calendar"]/div/div[3]/button[1]').click() # 定位催收时间查询，结束时间的时间框中的清空按钮
        time.sleep(1)
        #开始时间
        login_obj.driver.find_element_by_xpath('//*[@id="dispatchBeginTime"]').click() # 定位派单时间‘开始时间’选择框
        time.sleep(1)
        login_obj.driver.find_element_by_xpath('//*[@id="calendar"]/div/div[1]/table/tbody/tr/td[1]/select').click() # 定位时间框中的‘年份’下拉框
        time.sleep(1)
        login_obj.driver.find_element_by_xpath('//*[@id="calendar"]/div/div[1]/table/tbody/tr/td[1]/select/option[118]').click() # 定位 ‘年份’下拉框中的‘2017’年
        time.sleep(1)
        login_obj.driver.find_element_by_xpath('//*[@id="calendar"]/div/div[1]/table/tbody/tr/td[2]/select').click() # 定位时间框中的‘月份’下拉框
        time.sleep(1)
        login_obj.driver.find_element_by_xpath('//*[@id="calendar"]/div/div[1]/table/tbody/tr/td[2]/select/option[11]').click()  # 定位‘月份’下拉框中的‘1’月
        time.sleep(1)
        login_obj.driver.find_element_by_xpath('//*[@id="calendar"]/div/div[2]/dl[2]/dd[4]').click() # 定位时间框中的1号
        # 结束时间
        login_obj.driver.find_element_by_xpath('//*[@id="dispatchEndTime"]').click() # 定位派单时间‘结束时间’选择框
        time.sleep(1)
        login_obj.driver.find_element_by_xpath('//*[@id="calendar"]/div/div[1]/table/tbody/tr/td[1]/select').click() # 定位时间框中的‘年份’下拉框
        time.sleep(1)
        login_obj.driver.find_element_by_xpath('//*[@id="calendar"]/div/div[1]/table/tbody/tr/td[1]/select/option[119]').click() #定位 ‘年份’下拉框中的‘2018’年
        time.sleep(1)
        login_obj.driver.find_element_by_xpath('//*[@id="calendar"]/div/div[1]/table/tbody/tr/td[2]/select').click() # 定位时间框中的‘月份’下拉框
        time.sleep(1)
        login_obj.driver.find_element_by_xpath('//*[@id="calendar"]/div/div[1]/table/tbody/tr/td[2]/select/option[11]').click()  # 定位‘月份’下拉框中的‘11’月
        time.sleep(1)
        login_obj.driver.find_element_by_xpath('//*[@id="calendar"]/div/div[2]/dl[2]/dd[7]').click() # 定位时间框中的31号
        time.sleep(1)
        login_obj.driver.find_element_by_xpath('//*[@id="pagerForm"]/div[1]/div/table/tbody/tr[4]/td[3]/div/div/button').click() # 定位查询按钮
        time.sleep(1)

        # 逾期天数查询
        # 清空上一次的查询条件
        login_obj.driver.find_element_by_xpath('//*[@id="dispatchBeginTime"]').click() # 定位派单时间‘开始时间’选择框
        time.sleep(1)
        login_obj.driver.find_element_by_xpath('//*[@id="calendar"]/div/div[3]/button[1]').click()  # 定位派单时间查询，开始时间的时间框中的清空按钮
        time.sleep(1)
        login_obj.driver.find_element_by_xpath('//*[@id="dispatchEndTime"]').click() # 定位派单时间‘结束时间’选择框
        time.sleep(1)
        login_obj.driver.find_element_by_xpath('//*[@id="calendar"]/div/div[3]/button[1]').click() # 定位派单时间查询，结束时间的时间框中的清空按钮
        time.sleep(1)

        login_obj.driver.find_element_by_xpath('//*[@id="overDueDaysBegin"]').send_keys(1) # 定位逾期天数‘最小天数’输入框，并输入值
        time.sleep(1)
        login_obj.driver.find_element_by_xpath('//*[@id="overDueDaysEnd"]').send_keys(1) # 定位逾期天数‘最大天数’输入框，并输入值
        time.sleep(1)
        login_obj.driver.find_element_by_xpath('//*[@id="pagerForm"]/div[1]/div/table/tbody/tr[4]/td[3]/div/div/button').click() # 定位查询按钮
        time.sleep(1)
        late_text = login_obj.driver.find_element_by_xpath('//*[@id="cs_list_box"]/tr[1]/td[10]').text # 获取查询结果第一条数据中的逾期天数
        img.get_img('逾期天数查询成功，逾期天数为：','逾期天数查询失败，逾期天数为：',late_text,'1')

        # 催收公司搜索
        # 清空上一次的搜索条件
        login_obj.driver.find_element_by_xpath('//*[@id="overDueDaysBegin"]').clear() # 定位清空逾期天数‘最小天数’输入框
        time.sleep(1)
        login_obj.driver.find_element_by_xpath('//*[@id="overDueDaysEnd"]').clear() # 定位清空逾期天数‘最大天数’输入框
        time.sleep(1)

        login_obj.driver.find_element_by_xpath('//*[@id="companyId"]').click() # 定位催收公司下拉选择框
        time.sleep(1)
        login_obj.driver.find_element_by_xpath('//*[@id="companyId"]/option[2]').click() # 定位下拉列表中的值
        time.sleep(1)
        login_obj.driver.find_element_by_xpath('//*[@id="pagerForm"]/div[1]/div/table/tbody/tr[4]/td[3]/div/div/button').click() # 定位查询按钮
        time.sleep(5)

        # 催收组查询
        # 清空上一次的搜索条件
        login_obj.driver.find_element_by_xpath('//*[@id="companyId"]').click() # 定位催收公司下拉选择框
        time.sleep(1)
        login_obj.driver.find_element_by_xpath('//*[@id="companyId"]/option[1]').click()# 定位下拉列表中的默认值
        time.sleep(1)

        login_obj.driver.find_element_by_xpath('//*[@id="collectionGroup"]').click() # 定位催收组下拉选择框
        time.sleep(1)
        login_obj.driver.find_element_by_xpath('//*[@id="collectionGroup"]/option[4]').click() # 定位下拉列表中的默认值
        login_obj.driver.find_element_by_xpath('//*[@id="pagerForm"]/div[1]/div/table/tbody/tr[4]/td[3]/div/div/button').click()  # 定位查询按钮
        time.sleep(5)


