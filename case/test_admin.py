"""完成登录业务层实现"""
# 导包 unittest api_add_admin
# 新建测试类
# 新建测试方法
     # 暂时存放数据 url username  password
     # 调用登陆方法
     # 断言 响应信息 状态码

import unittest
from api.api_admin import Api_Admin
from parameterized import parameterized
from tools.read_file import ReadJson
from tools.read_db import ReadDB

# 使用参数化 读取数据函数,通过方法 @parameterized.expand(get_data()) 传参给def test_add_admin()


def get_data():
    datas = ReadJson("admin.json").read_json()
    # 新建空列表，添加读取json数据data
    arrs = []
    for data in datas.values():
        arrs.append((data.get("url"),
                     data.get("admin_id"),
                     data.get("username"),
                     data.get("admin_name"),
                     data.get("password"),
                     data.get("admin_status"),
                     data.get("status_code")))
    #print(arrs)
    return arrs

class TestAddadmin(unittest.TestCase):
    @parameterized.expand(get_data())
    def test_admin(self,url,admin_id,username,admin_name,password,admin_status,status_code):
        # 调用登陆方法
        response = Api_Admin().api_admin(url,admin_id,username,admin_name,password,admin_status,status_code)
        print("查看响应结果:",response.json())

        # 第三条数据为修改admin_id=23的数据返回的结果；admin_id=0表示新增管理员
        self.assertEqual(status_code,response.status_code)   # 检查返回的状态是否等于200
        print(response.status_code)

        # 数据库查询
        sql = "select admin_id from admin where admin_id=23 and admin_status=0"
        result = ReadDB().get_sql_one(sql)
        print(result)
        self.assertEquals(23, result[0])
        try:
            23 == result[0]
            print("修改成功:"+result)
        except:
            print(result)

if __name__ == '__main__':
    unittest.main()