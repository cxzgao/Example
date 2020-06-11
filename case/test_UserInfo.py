import unittest
from api.api_UserInfo import Api_UserInfo

class TestUserInfo(unittest.TestCase):
    def test_UserInfo(self):
        url = 'http://t-chat-api.zaomeijia.cn/manage/user/info'
        user_id = 64
        # 调用登陆方法
        res = Api_UserInfo().api_userinfo(url,user_id)
        print(res.json()['result'])

if __name__ == '__main__':
    unittest.main()