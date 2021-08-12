#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import unittest
import sys
from utils.get_path import *
sys.path.append(oprate_dir)
from report import make_report
import pytest

name =input('输入测试类，执行河南用例输入hn。省局用例输入zj\n\n执行单独文件输入文件名\n\n执行全量用例直接按enter：')
case = ("test_zj_%s.py" %name)
file = os.path.join(case_dir, case)
print( file)
if name == '':
     make_report("test*.py")
elif os.path.exists(file):
     make_report(case)
elif name == 'hn':
     make_report("test_hn*.py")
elif name == 'zj':
     make_report("test_zj*.py")
else:
     print('！'*10,'无此测试类','！'*10)


if __name__ == '__main__':
     print('*'*25,'测试结束','*'*25)
     # pytest.main(["-m","test"])
