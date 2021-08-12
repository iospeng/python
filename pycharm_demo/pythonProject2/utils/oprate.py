#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import sys
sys.path.append("..")
import pymysql.cursors
from utils.read_config import conf
from utils.my_logger import logger
import time
import random
# import os
# from utils.get_path import *
def function():
    '''生成随机字符串做主键'''
    list = [chr(i) for i in range(97,110)] + [str(i) for i in range(10)] + [str(i) for i in range(10)]  #小写字母+数字
    num = random.sample(list,20)  #输出10个固定长度的组合字符
    str1=''
    value = str1.join(num) #将取出的十个随机数进行重新合并
    logger.debug(("生成随机ID %s") % value)
    return (value)

def conn():
 #建立数据库连接
 global  cur,connect
 connect = pymysql.Connect(
  host=conf.get("mysql", "host"),
  port=conf.getint("mysql", "port"),
  user=conf.get("mysql", "username"),
  passwd=conf.get("mysql", "password"),
  database=conf.get("mysql", "database"),
  db='python',
  charset='utf8'
 )
 logger.debug("开始链接数据库")
 cur = connect.cursor()
 logger.debug("打开数据库游标")

def Serch(num,table):  # 传入车牌号与所查询库
  #查询数据库中师傅存在此数据
  global cur
  tab = table
  PLATE_NUMBER = (num)
  sql = "SELECT PLATE_NUMBER FROM %s WHERE  PLATE_NUMBER = '%s' "%(tab,PLATE_NUMBER)
  conn()
  cur.execute(sql)
  logger.debug("执行查询SQL语句")
  for row in cur.fetchall(): #查询全量数据
   print(row)
   logger.debug("返回数据库查询row")
   print('共查找出', cur.rowcount, '条数据')
   #关闭游标
   cur.close()
   logger.debug("数据库游标关闭")
   # 关闭连接
   if (cur.rowcount) == None:
       logger.debug("数据库返回为空")
       return False  #返回查询行数
   else:
       return (cur.rowcount)
   logger.debug("数据库返回行数")


def Add(num,table):
    global cur,connect
    pushtime = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    print(pushtime)
    PLATE_NUMBER = num
    sql = "INSERT INTO %s (ID, PLATE_NUMBER,PLATE_COLOR , START_DATE, END_DATE, VEHICLE_TYPE, PUSH_TIME) VALUES " \
          "( '%s','%s', 2,'2021-01-01','2021-02-04',4,'%s')"% (table,function(),PLATE_NUMBER,pushtime)
    conn()
    try:
        cur.execute(sql)
        connect.commit()
    except (pymysql.err.OperationalError) as e:
        logger.error(("数据库结构异常",repr(e)))
    except (pymysql.err.IntegrityError) as e:
        logger.error(("主键异常", repr(e)))
    print('成功插入', cur.rowcount, '条数据')
    logger.info(('成功插入', cur.rowcount, '条数据'))

def Add_suspect(num, table,level):
    global cur, connect
    pushtime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    print(pushtime)
    PLATE_NUMBER = num
    sql = "INSERT INTO %s (ID, PLATE_NUMBER,PLATE_COLOR , CREATED_TIME, LAST_MODIFIED_TIME, LEVEL) VALUES " \
          "( '%s','%s', 2,'2021-01-01','%s',%d)" % (table, function(), PLATE_NUMBER, pushtime,level)
    conn()
    try:
        cur.execute(sql)
        connect.commit()
    except (pymysql.err.OperationalError) as e:
        logger.error(("数据库结构异常", repr(e)))
    except (pymysql.err.IntegrityError) as e:
        logger.error(("主键异常", repr(e)))
    print('成功插入', cur.rowcount, '条数据')
    logger.info(('成功插入', cur.rowcount, '条数据,level:',level))

# def Add_warninfo(num,table):
#     global cur ,connect
#     pushtime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
#     PLATE_NUMBER = num
#     sql = "INSERT INTO %s (ID, PLATE_NUMBER,PLATE_COLOR , CREATED_TIME, LAST_MODIFIED_TIME, LEVEL) VALUES " \
#           "( '%s','%s', 2,'2021-01-01','%s',2)" % (table, function(), PLATE_NUMBER, pushtime)
#     conn()


def Delete(num,table):    #删除数据库中测试时增加的车辆
    global cur,connect
    tab = table
    PLATE_NUMBER = num
    if Serch(num,table) == None:
        logger.warning("数据库原不存在该车辆")
    else:
        limit = Serch(num,table)
        sql = "DELETE  FROM %s WHERE PLATE_NUMBER = '%s' LIMIT  %d" % (tab, PLATE_NUMBER,limit)
        logger.info(("删除", PLATE_NUMBER," 该车辆", limit ,"条数据"))
        conn()
        cur.execute(sql)
        connect.commit()
        logger.debug("执行删除SQL语句")
        result = Serch(num,table)
        if result == None:
            logger.debug("删除成功")
            return True
        else:
            logger.error("删除失败")
            return False
    return False











