import unittest
from api.api_user_token import Api_User_Login

class Test_UserLogin(unittest.TestCase):
    def test_userlogin(self):
        url = "http://t-chat-api.zaomeijia.cn/app/user/login"
        mobile = "131"
        password = "131"
        res = Api_User_Login().api_userlogin(url,mobile,password)
        #print(res.json())
        return res.json()['result']['login_token']

if __name__ == '__main__':
    unittest.main()