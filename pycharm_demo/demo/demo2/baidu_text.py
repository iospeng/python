
from selenium import webdriver
import time

driver = webdriver.Chrome()
# 浏览器最大化
driver.maximize_window()
driver.get('http://hz.topws.cn/flow.php')
# driver.find_element_by_class_name('known-btn j-known-btn').click()
# driver.find_element_by_xpath("//div[@class='known-btn j-known-btn]").click()
# driver.find_element_by_css_selector("a.app-list-name").click()
driver.find_element_by_css_selector('a.style-red').click()
driver.find_element_by_name('formLogin').find_element_by_id('loginname').send_keys('15671278825')
driver.find_element_by_name('formLogin').find_element_by_id('nloginpwd').send_keys('sjq123456')
driver.find_element_by_name('formLogin').find_element_by_id('loginSubmit').click()
# driver.switch_to.frame('formCart')
# 获得当前窗口
nowhandle = driver.current_window_handle

driver.switch_to.window(nowhandle)

try:
    se = driver.find_element_by_name('goPay')
    se.click()
except:
    print('错误截图')
    driver.get_screenshot_as_file("D:\\python\python\\demo2\\errorImg\\j.jpg")
# se.text
# se.click()
