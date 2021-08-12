import oprate
# import string
# import random
# # !/usr/bin/env python
# # -*- coding: utf-8 -*-
from rocketmq.client import Producer,Message
# import requests
from selenium import webdriver
# import json
import hn
import threading
import time
import re
import  os
# for i in range(2,100):
#     for j in range(2,i):
#         if i%j ==0:
#             break
#         else:
#             print(i, '\n')
#             break
# # from sympy import *
# x = symbols("x")
#
# result = solve('x-x/2-1-x/4-1/2-x/8-1/4-x/16-1/8-x/32-1/16-1',x)
# print(result)
# tt = re.findall('^\d{13}',str(time.time()).replace('.',''))[0]
# print(tt)
# producer = Producer('PID-001')
# producer.set_namesrv_addr('192.168.90.131:9876')
# producer.start()
# msg = Message('linkcld_tdmp_gantry')
# msg.set_keys('key')
# msg.set_tags('bayonet')
# body = ("[{'enn':'河南惠济站'," \
#        "'gid':'G003041003005620010'," \
#        "'ipnc':'豫NL7007_1'," \
#        "'ln':'201'," \
#        "'marked':true," \
#        "'mid':'020000410101620060354820210315072344'," \
#        "'mt':3," \
#        "'pnc':'豫NL7007_1'," \
#        "'pt':%s," \
#        "'rt':1615767977000," \
#        "'vt':'3'}]"%tt)
# print(body)
# msg.set_body(body)
# ret = producer.send_sync(msg)
# print(ret.status, ret.msg_id, ret.offset)
# producer.shutdown()
# print (str(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))))
# # 这里定义了类和方法，如果只要功能，直接取方法里的内容即可
# oprate.Add_suspect('浙A00001','ill_suspected_vehicle_record')
# print(oprate.Serch('浙A00001', 'ill_suspected_vehicle_record'))
#
# print(oprate.Serch('浙B0T756','ill_vehicle_freq'))
# i = 2
# for i in range(10):
# hn.push('豫A0000%d_1'% i)
# hn.Delete('豫A00001', 'ill_suspected_vehicle_record')
# hn.Delete('豫A00001', 'ill_warn_record')
# hn.Delete('豫A00001', 'ill_vehicle_warn_info')
# tt = re.findall('^\d{13}', str(time.time()).replace('.', ''))[0]
# print(tt)
# producer = Producer('PID-001')
# producer.set_namesrv_addr('192.168.90.131:9876')
# producer.start()
# msg = Message('linkcld_tdmp_gantry')
# msg.set_keys('key')
# msg.set_tags('bayonet')
# body = ("[{'enn':'河南惠济站'," \
#         "'gid':'G003041003005620010'," \
#         "'ipnc':'%s'," \
#         "'ln':'201'," \
#         "'marked':true," \
#         "'mid':'020000410101620060354820210315072344'," \
#         "'mt':3," \
#         "'pnc':'%s'," \
#         "'pt':%s," \
#         "'rt':1615767977000," \
#         "'vt':'2'}]" % ('豫A00001_1', '豫A00001_1', tt))
# msg.set_body(body)
# ret = producer.send_sync(msg)
# print(ret.status, ret.msg_id, ret.offset)
# producer.shutdown()
# # def mq():
#     '''MQ推送预警 '''
#     hn.add('豫A00001', 'ill_suspected_vehicle_record')
#     try:
#         hn.push('豫A00001_1')
#         raise
#     except Exception:
#         raise
#     else:
#         assert 1 == 1
#         logger.info("预警信息推送成功")
# def main():
#     t1 = threading.Thread(target=mq())
#     t1.start()
#     t1.join()
#     print('ok')
#
# if __name__=='__main__':
#     main()
#  print (i)

#  time.sleep(2)
#  print ('ok')
#     oprate.Delete((("浙A0000%d")% i),'ill_suspected_vehicle_record',)
#     print(("浙A0000%d")% i)
# oprate.Delete(("浙ATE001"), 'ill_suspected_vehicle_record')

# hn.push('豫A00000_1')
# hn.push('豫A00001_1')
# hn.push('豫A00002_1')1234
# line = input("输入")
# print(len(line))
# if line == line[::-1]:
#     print("yes")
# else:
#     print("no")

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
options.add_argument('--headless')
driver = webdriver.Chrome(options=options)  # chrome下载设置
driver.get("https://www.mytokencap.com/currency/doge/821714640")
driver.implicitly_wait(3)
while True:
    driver.find_element_by_xpath(
        '//*[@id="__layout"]/div/div[1]/section/div[1]/div[2]/div/div[1]/div[2]')
    g =driver.find_element_j
    print(g)