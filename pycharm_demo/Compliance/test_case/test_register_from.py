# -*- coding: utf-8 -*-
# @Project : Compliance
# @File    : test_register_from.py
# @Software: PyCharm
# @Author  : Lizhipeng
# @Email   : 1907878011@qq.com
# @Time    : 2021/10/26 16:08
from po.seat_register import SeatRegister


class TestRegisterFrom:
    def test_register_from(self):
        cookie = [{'domain': '192.168.90.162', 'httpOnly': True, 'name': 'JSESSIONID', 'path': '/ims-pro', 'secure': False, 'value': 'D4036D4C383F86B58511258FAAD55F94'}]
        reg = SeatRegister(driver=None, cookies=cookie)
        assert "郑州市" in reg.seat_register()
