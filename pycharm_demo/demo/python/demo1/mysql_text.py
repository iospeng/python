# -*- coding: utf-8 -*-
# !usr/bin/python
import pymysql

# 打开数据库连接
conn = pymysql.connect('localhost', 'root', '123456', 'forever', use_unicode=True, charset="utf8")
# 使用cursor（）方法创建一个数据库对象cursor
cursor = conn.cursor()
names = input()
p = input()
# li = (names, p)
# 使用execute()方法执行sql查询
sql = '''INSERT INTO one(name,pass)VALUES('%s','%d')''' % (names, int(p))

s = cursor.execute(sql)
# s = cursor.executemany(sql)
# 将数据提交到数据库
conn.commit()
#数据库查询后依次读出数据
for i in range(s):
    data = cursor.fetchone()
    print(data)
conn.close()
