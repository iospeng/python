# -*- coding: utf-8 -*-
#!/usr/bin/python

from datetime import datetime,timedelta,timezone

# 获取当前系统时间
time = datetime.now()
print('获取当前系统时间：',time)
# 指定日期时间
AppointTime = datetime(2017,9,9,20,00)
print('指定时间：',AppointTime)

# 时间（datetime）转换为时间戳（timestamp）
timeTostamp = time.timestamp()
print('datetime转换为时间戳：',timeTostamp)
# 时间戳(timestamp)转换为时间（datetime）
stampTotime = datetime.fromtimestamp(timeTostamp)
print('时间戳转换为datetime:',stampTotime)

# 将时间转换为UTC标准时区的时间
standard = datetime.utcfromtimestamp(timeTostamp)
print('标准时区的时间(格林尼治时间)：',standard)

# 字符串时间转换为datetime
strdateTodate = datetime.strptime('2014.9.9 20:00:00','%Y.%m.%d %H:%M:%S')
print('字符串时间转换为datetime:',strdateTodate)

# datetime转换为字符串时间
dateTostr = strdateTodate.strftime('%Y-%m-%d %H:%M:%S')
print('date转换为字符串时间：',dateTostr)
print('dateTostr的数据类型是：',type(dateTostr))

# 时间计算
now = datetime.now()
print('当前系统时间：',now)
print('当前系统时间加1星期：',now+timedelta(weeks=1))
print('当前系统时间加1天：',now+timedelta(days=1))
print('当前系统时间加1小时：',now+timedelta(hours=1))
print('当前系统时间加1分钟：',now+timedelta(minutes=1))
print('当前系统时间加1秒：',now+timedelta(seconds=1))

# 本地时间转换为UTC时间
time_12 = timezone(timedelta(hours=12)) #创建时区UTC+12
print('创建时区UTC+12：',time_12)
utc_8_time= now.replace(tzinfo=time_12)
print('转换为UTC时间：',utc_8_time)

# 获取当前UTC时区的时间
nowUTCtime = datetime.utcnow().replace(tzinfo=timezone.utc)
print('当前UTC时区的时间：',nowUTCtime)
# 将UTC时间转换为东八区(北京)时间
bj_UTCtime = nowUTCtime.astimezone(timezone(timedelta(hours=8)))
print('东八区（北京）时间：',bj_UTCtime)
# 将UTC时间转换为东京时间
dj_UTCtime = nowUTCtime.astimezone(timezone(timedelta(hours=9)))
print('东京时间：',dj_UTCtime)
