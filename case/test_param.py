"""
    parameterized参数化组件应用
    使用：@parameterized.expant(参数)
    单个参数：parameterized.expand(["yinhaha","yin111"])
    多个参数：parameterized.expand([("yinhaha","123456"),("yinhaha","1234")])
"""
# 导包
import unittest
import os
from parameterized import parameterized

# 新建测试类
class TestPara(unittest.TestCase):
    # 新建测试方法
    @parameterized.expand([("yinhaha","123456"),("yinhaha","1234")])
    def test_para(self,username,password):
        print("用户名：",username)
        print("密码：",password)
        print(os.path.abspath('.'))
        print(os.path.abspath('..'))
