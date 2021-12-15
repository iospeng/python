# -*- coding: utf-8 -*-
# @Project : Compliance
# @File    : test_register_from.py
# @Software: PyCharm
# @Author  : Lizhipeng
# @Email   : 1907878011@qq.com
# @Time    : 2021/10/26 16:08
from po.seat_register import SeatRegister


class TestRegisterFrom:
    cookie = [{'domain': '192.168.90.162', 'httpOnly': True, 'name': 'JSESSIONID', 'path': '/ims-pro', 'secure': False, 'value': 'D499AD806EECB04AA871AAAA627B7B24'}]

    """判断数据是否与账号对应"""
    def test_register_from(self):
        """判断数据是否与账号对应"""
        reg = SeatRegister(drivers=None, cookie=self.cookie)
        assert "郑州市" in reg.seat_register()

    """检查文件是否上传"""
    def test_file(self):
        """检查文件是否上传"""
        file = SeatRegister(drivers=None, cookie=self.cookie)
        assert "项目部署.pdf" in file.test_file_yesorno()

    """上传附件"""
    def test_file_replace(self):
        """上传附件"""
        file = SeatRegister(drivers=None, cookie=self.cookie)
        file.test_file_replace()
        assert "项目部署.pdf" in file.test_file_yesorno()
