# -*- coding: utf-8 -*-
# @Project : RequestsDemo
# @File    : test_festival_yaml.py.py
# @Software: PyCharm
# @Author  : Lizhipeng
# @Email   : 1907878011@qq.com
# @Time    : 2022/1/6 13:55
import yaml


def test_festival_yaml():
    env = {
        "method": "post",
        "url": "http://192.168.90.162:8090/ims-pro/holiday/save",
        "header": {
            "Host": "192.168.90.162:8090",
            "Content-Length": "549",
            "Accept": "*/*",
            "X-Requested-With": "XMLHttpRequest",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36",
            "Content-Type": "application/json",
            "Origin": "http://192.168.90.162:8090",
            "Referer": "http://192.168.90.162:8090/ims-pro/app/registrationForm/holidayReport/registerPage.html?id=undefined&state=1",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Cookie": "JSESSIONID=109E05B89D1608AC24585135B98CF9F1",
            "Connection": "keep-alive",
        },
        "params": {
            "allSeat": "1",
            "areaCode": "410173",
            "areaName": "郑州航空港经济综合实验区",
            "censusDate": "2022-01-06",
            "charterVehicleCount": "0",
            "customiseLineCount": "0",
            "customisePersonCount": "0",
            "customiseVehicleCount": "0",
            "holidayName": "元旦",
            "holidayType": "1",
            "networkTicketCount": "0",
            "networkTicketPersonCount": "0",
            "nextPersonCount": "0",
            "nextShuttleForecastCount": "0",
            "nextVehicleForecastCount": "0",
            "runVehicleCount": "0",
            "saveType": "1",
            "shuttleVehicleCount": "0",
            "todayPersonCount": "0",
            "todayShuttleCount": "0",
        }
    }

    with open("festival.yaml", "w", encoding='utf-8') as f:
        yaml.safe_dump(data=env, stream=f, allow_unicode=True, sort_keys=False)
