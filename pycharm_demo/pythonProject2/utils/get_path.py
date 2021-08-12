#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import os
#此脚本路径
base_dir = os.path.split(os.path.split(os.path.abspath(__file__))[0])[0]
# print(base_dir,2)
utils_dir = os.path.join(base_dir, 'utils')
# print(utils_dir)

# 用例的路径
case_dir = os.path.join(base_dir, 'test_cases')
# print(case_dir)


oprate_dir = os.path.join(base_dir, 'utils')
# print(oprate_dir)
# 测试数据的路径
# data_dir = os.path.join(base_dir, 'test_data', 'data.xlsx')
# print(data_dir)

# 日志文件路径
logger_dir = os.path.join(base_dir, 'logs', 'auto_test_logger.log')
# print(logger_dir)

#配置文件路径
ini_file = os.path.join(base_dir, 'config', 'pytest.ini')
# print(ini_file)

#测试下载时使用的临时文件夹
download_dir = os.path.join(base_dir, 'download')
# print(download_dir)

upload_dir = os.path.join(base_dir, 'upload')
# print(upload_dir)
report_dir = os.path.join(base_dir, 'test_report')
# for files in os.walk(case_dir):
#  print(files,"\n")
print ('*'*80,'\n')

