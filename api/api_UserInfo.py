import requests
from case.test_token import TestLogin

class Api_UserInfo(object):
    def api_userinfo(self,url,user_id):
        headers = {"Content-Type":"application/json",
                   "Authorization":TestLogin().test_testlogin()}
        data = {"user_id":user_id}
        return requests.post(url,headers=headers,json=data)