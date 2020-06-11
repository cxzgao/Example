"""
    搜素组装测试套件
    运行测试套件并生成测试报告
"""
# 导包 unittest、HTMLTestReportCN
# 1、组装测试套件
# 2、指定报告存放路径及文件名称
# 3、运行测试套件并生成测试报告

import unittest
from HTMLTestReportCN import HTMLTestRunner

class TestRunner(object):
    fp = open('./report/' + '测试报告.html', 'wb')
    test = unittest.defaultTestLoader.discover('./case', pattern='test*.py')
    HTMLTestRunner(stream=fp).run(test)
    fp.close()