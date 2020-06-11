import unittest
from api.api_token import Api_L

class TestLogin(unittest.TestCase):
    def test_testlogin(self):
        url = 'http://t-chat-api.zaomeijia.cn/manage/admin/login'
        username ='yinhaha'
        password = '123456'
        # 调用登陆方法
        res = Api_L().api_l(url, username, password)
        # print(res.json())
        # 获取token
        token = res.json()['result']['token']
        #print(token)
        return token

if __name__ == '__main__':
    unittest.main()