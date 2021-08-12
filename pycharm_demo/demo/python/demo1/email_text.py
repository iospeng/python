# -*- coding: utf-8 -*-
# !usr/bin/python

import smtplib
from email.mime.text import MIMEText
from email.header import Header

# 邮箱地址
mail_host = 'smtp.163.com'
mail_user = 'iospeng'
mail_pass = '3999LAOdiDE'

name = 'iospeng@163.com'
toName = 'hziospeng@163.com'
message = MIMEText('aaa', 'plain', 'utf-8')
message['From'] = Header('iospeng@163.com', 'utf-8')
message['To'] = Header('hziospeng@163.com', 'utf-8')

subject = '测试邮件'
message['Subject'] = Header('hah', 'utf-8')

# 发送邮件
smtpObj = smtplib.SMTP(mail_host, 25)
# 链接邮箱
# smtpObj.connect(mail_host)
# smtpObj.set_debuglevel(1)
# 登录邮箱
log = smtpObj.login(mail_user, mail_pass)
print(log)
smtpObj.sendmail(name, toName, 'hhh')
# print ("邮件发送成功")