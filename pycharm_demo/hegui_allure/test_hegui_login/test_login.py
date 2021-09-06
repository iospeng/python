import time
import pytest
import yaml
from selenium import webdriver
import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import web

driver = webdriver.Chrome()


def setup_module():
    # time.sleep(1)
    driver.maximize_window()
    # time.sleep(1)
    # driver.implicitly_wait(3)


def teardown_module():
    driver.quit()


@allure.feature('登录')
class TestLogin():
    driver.implicitly_wait(3)

    @allure.story('读取文件中的数据并返回')
    def test_yml(self):
        with open('data/datas.yml') as f:
            dates = yaml.safe_load(f)
        return dates

    @allure.story('输入账号密码，点击登录')
    def test_log(self):
        allure.attach(self.test_yml()['user'][0], '账号', attachment_type=allure.attachment_type.TEXT)
        allure.attach(self.test_yml()['ps'][0], '密码', attachment_type=allure.attachment_type.TEXT)
        with allure.step('打开网址'):
            driver.get("http://192.168.90.101/login/login.html?service=http://192.168.90.162:9800/illegal-pro/")
            # time.sleep(1)
        with allure.step('输入用户名'):
            webDriverWait
            webDriverWait(driver, 10).expected_conditions.visibility_of_element_located
            driver.find_element_by_xpath('//*[@id="username"]').send_keys(self.test_yml()['user'][0])
            # time.sleep(1)
        with allure.step('输入密码'):
            driver.find_element_by_xpath('//*[@id="password"]').send_keys(self.test_yml()['ps'][0])
            # time.sleep(1)
        with allure.step('点击登录'):
            driver.find_element_by_xpath('//*[@id="login-Button"]').click()
            # time.sleep(5)
        with allure.step('保存截图'):
            driver.save_screenshot('./img/2.jpg')
            allure.attach.file('./img/2.jpg', '截图', attachment_type=allure.attachment_type.JPG)


if __name__ == '__main__':
    pytest.main()
