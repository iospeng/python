#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from rocketmq.client import Producer,Message
from utils.my_logger import logger
import time
import re

def push(num):
    tt = re.findall('^\d{13}', str(time.time()).replace('.', ''))[0]
    print(type(tt))
    producer = Producer('PID-001')
    producer.set_namesrv_addr('192.168.90.131:9876')
    producer.start()
    msg = Message('linkcld_tdmp_gantry')
    msg.set_keys('key')
    msg.set_tags('bayonet')
    body = ("[{'enn':'河南惠济站'," \
            "'gid':'G003041003005620010'," \
            "'ipnc':'%s'," \
            "'ln':'201'," \
            "'marked':true," \
            "'mid':'020000410101620060354820210315072344'," \
            "'mt':3," \
            "'pnc':'%s'," \
            "'pt':%s," \
            "'rt':1615767977000," \
            "'vt':'2'}]"% (num,num,tt))
    msg.set_body(body)
    ret = producer.send_sync(msg)
    print(ret.status, ret.msg_id, ret.offset)
    producer.shutdown()

def main():
    '''MQ推送预警 '''
    try:
        push('豫A00001_1')
        raise
    except Exception:
        logger.exception("RocketMQ推送预警失败")
        raise
    else:
        logger('MQ推送成功')
if __name__ == '__main__':
    logger.info('mqpush.py开始运行')
    main()