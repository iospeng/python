
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common import action_chains
from selenium.webdriver.common.action_chains import ActionChains
import time
import HTMLTestRunner
import unittest

class webPy(object):
    def __init__(self):
        # 创建webdriver对象
        self.driver = webdriver.Chrome()
        # 浏览器最大化
        self.driver.maximize_window()
        op = self.open()
        hl, l, s, d, j, g = 0, 1, 2, 3, 4, 5
        if op:
            hl = self.test_HomeLogin()
        if hl:
            l = self.test_Login()
        if l:
            s = self.search()
        if s:
            d = self.details()
        if d:
            j = self.join()
        if j:
            self.go_pay()
    #打开浏览器
    def open(self):
        # global driver
        # 选择浏览器打开网页,前提是电脑上必须有这个浏览器，否者会报“找不到文件”的错
        '''
        Firefox     火狐浏览器
        Chrome      谷歌浏览器
        '''

        try:
            self.driver.get('http://hz.topws.cn')
            return True
        except BaseException as e:
            print('打开浏览器失败', e)
            return False

    # 定位控件位置
    '''
    find_element_by_id      通过控件ID定位
    send_keys               文本框输入方法
    click                   按钮点击方法
    '''
    # 定位到首页会员登录按钮
    def test_HomeLogin(self):
        # global driver
        try:
            xt = self.driver.find_element_by_id('ECS_MEMBERZONE').find_element_by_xpath('//a[1]')
            xt.click()
            # print('返回结果', y)
            return True
        except BaseException as e:
            print('点击首页登录按钮跳转失败', e)
            return False

    #登录页面登录
    def test_Login(self):
        # global driver
        # 点击会员登录按钮，跳转到登录页面，登录成功在次回到首页
        # 添加新窗口的句柄
        time.sleep(2)
        now_handle = self.driver.current_window_handle
        # print(now_handle, self.driver.title)
        try:
            self.driver.find_element_by_name('formLogin').find_element_by_id('loginname').send_keys('15671278825')
            self.driver.find_element_by_name('formLogin').find_element_by_id('nloginpwd').send_keys('sjq123456')
            self.driver.find_element_by_name('formLogin').find_element_by_id('loginSubmit').click()
            return True
        except BaseException as e:
            print('登录失败', e)
            return False

    #搜索商品，并进入商品详情页
    def search(self):
        # global driver
        # 添加新窗口的句柄
        time.sleep(2)
        now_handle1 = self.driver.current_window_handle
        # print("新窗口的句柄1", now_handle1, self.driver.title)
        try:
            text = self.driver.find_element_by_id('keyword')
            text.clear()
            text.send_keys('2017')
            self.driver.find_element_by_class_name('ecsc-search-button').click()
            return True
        except BaseException as e:
            print('搜索失败', e)
            return False

    #进入商品详情页
    def details(self):
        # global driver
        # 点击商品进入商品详情页
        try:
            ss = self.driver.find_elements_by_class_name('addcart')
            ss[0].click()
            return True
        except BaseException as e:
            print("进入商品详情页失败", e)
            return False
    def joinClick(self):
        try:
            # 点击“加入购物车”按钮
            # if te[0].text != 0:
            time.sleep(2)
            # 点击两次加入购物车按钮
            # self.driver.find_element_by_class_name('btn-append').click()
            time.sleep(2)
            ss = self.driver.find_element_by_class_name('btn-append').click()
            # add = 1
            # return True
        except BaseException as e:
            print('加入购物车失败', e)
            # return False

    #加入购物车
    def join(self):
        te = 0
        add = 0
        # 添加新窗口的句柄
        now_handle3 = self.driver.current_window_handle
        self.joinClick()
        # if te[0].text == None:
        try:
            time.sleep(2)
            #关闭对话框
            self.driver.find_element_by_class_name('pb-x').click()
        except BaseException as e:
            print('关闭对话框报错', e)

        try:
            time.sleep(2)
            # 输入购买数量
            te = self.driver.find_elements_by_name('quantity')
            te[0].clear()
            te[0].send_keys(2)
            # print('我勒个去', te[0].text)
        except BaseException as e:
            print('输入数量报错', e)

        # self.joinClick()
        #点击“立即订货”按钮
        try:
            # 因为是输入的数字，所以需要点击一下空白处刷新一下页面
            self.driver.find_element_by_id('p-box').click()
            self.driver.find_element_by_css_selector("a.btn-buynow").click()
            # print('adddd:', self.driver.title)
            return True
        except BaseException as e:
            print('立即订货按钮点击报错', e)
            return False

    def go_pay(self):
        # 获取新页面的句柄
        handle = self.driver.current_window_handle
        print('asd:',self.driver.title)
        try:
            self.driver.find_element_by_id('cart_goods_amount').click()
        except BaseException as e:
            print('去结算按钮编辑报错', e)
            self.driver.get_screenshot_as_file("D:\\python\\python\\demo2\\errorImg\\j.jpg")
    def all_case():
        discover = unittest.defaultTestLoader.discover('test_HomeLogin', pattern='test*.py',top_level_dir=None)
        print("dis:",discover)
        return discover

if __name__=='__main__':
    # test = unittest.TestSuite()
    # test.addTest(webPy())
    # test.addTest(webPy())
    # suite = unittest.makeSuite(webPy)
    # print('保存测试结果')
    # fileName = 'D:\\python\\python\\demo2\\errorImg\\file.html'
    # fp = open(fileName, 'wb')
    # runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='测试', description='ceshi')
    # runner.run(all_case())
    # # runner.run(suite)
    # fp.close()
    ho = webPy()

# driver.execute_script("window.scrollBy(0,200)","")  #向下滚动200px
# driver.execute_script("window.scrollBy(0,document.body.scrollHeight)","")  #向下滚动到页面底部