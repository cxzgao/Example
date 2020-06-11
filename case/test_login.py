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
from tools.read_file import ReadJson

# 使用参数化 读取数据函数,通过方法 @parameterized.expand(get_data()) 传参给def test_login()
def get_data():
    data = ReadJson("login.json").read_json()
    # 新建空列表，添加读取json数据data
    arrs = []
    arrs.append((data.get("url"),
                 data.get("username"),
                 data.get("password"),
                 data.get("errcode"),
                 data.get("status_code")))
    print(arrs)
    return arrs

class TestLogin(unittest.TestCase):
    @parameterized.expand(get_data())
    def test_login(self,url,username,password,errcode,status_code):
        # 暂时存放数据
#        url = "http://t-chat-api.zaomeijia.cn/manage/admin/login"
#        username = "yinhaha"
#        password = "123456"
        # 调用登陆方法
        s = ApiLogin().api_login(url,username,password)
        print("查看响应结果:",s.json())
        # 断言 响应信息 状态码
#        self.assertEqual(0,s.json()['errcode']) # 判断返回的errcode是否等于0
        self.assertEqual(errcode, s.json()['errcode'])  # 判断返回的errcode是否等于0
        print(s.json()['errcode'])
#       self.assertEqual(200,s.status_code)   # 判断返回的status_code是否等于200
        self.assertEqual(status_code, s.status_code)  # 判断返回的status_code是否等于200
        print(s.status_code)

        # 提取登陆token
        print("token："+s.json()['result']['token'])

    def test_testlogin(self):
        pass


if __name__ == '__main__':
    unittest.main()
# token:8DmkwAlIHKtsvLytiEfmp9sAhwSvm7FqDXCcnH1/2ar5Gktuh0osshj/CnZ4Rlqf