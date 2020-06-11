# -*- coding:utf-8 -*-
"""
   在unittest框架中使用数据库工具类
"""
# 导包 unittest、tools.read_db
# 新建类
# 新建方法
    # 定义sql语句
    # 调用get_sq_one方法
    # 断言
import unittest
from tools.read_db import ReadDB

class Test_db(unittest.TestCase):
    def test_db(self):
        sql = "select admin_status from admin where admin_id=23"
        result = ReadDB().get_sql_one(sql)
        self.assertEquals(0,result[0])
        try:
            0 == result[0]
            print("修改成功")
        except:
            print(result)

if __name__ == '__main__':
    unittest.main()