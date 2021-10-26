# -*- coding: utf-8 -*-
# @Project : Compliance
# @File    : test_logins.py
# @Software: PyCharm
# @Author  : Lizhipeng
# @Email   : 1907878011@qq.com
# @Time    : 2021/10/26 15:17
from po.logins import Logins
from po.seat_register import SeatRegister


class TestLogins:
    def test_logins(self):
        log = Logins()
        assert "郑州市监管" in log.logins()
