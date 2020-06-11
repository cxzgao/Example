"""完成登录业务层实现"""
# 导包 unittest api_login
# 新建测试类
# 新建测试方法
     # 暂时存放数据 url username  password
     # 调用登陆方法
     # 断言 响应信息 状态码

import unittest
from api.api_login import ApiLogin
from parameterized import parameterized
from tools.read_login import ReadJson

# 使用参数化 读取数据函数,通过方法 @parameterized.expand(get_data()) 传参给def test_login()
def get_data():
    datas = ReadJson("login_more.json").read_json()
    # 遍历获取login_more.json数据中的多组数据的value
    arrs = []
    for data in datas.values():
        arrs.append((data.get("url"),
                     data.get("username"),
                     data.get("password")))
    #print(arrs)
    return arrs

class TestLogin(unittest.TestCase):
    @parameterized.expand(get_data())
    def test_login_1(self,url,username,password):
        # 调用登陆方法,返回响应结果
        s = ApiLogin().api_login(url,username,password)
        print("查看响应结果",s.json())

if __name__ == '__main__':
    unittest.main()