import requests
from case.test_token import TestLogin

class Api_AdminList(object):
    def api_adminlist(self,url,page,limit,key,status_code):
        headers = {"Content-Type":"application/json",
                   "Authorization":TestLogin().test_testlogin()}
        data = {
            "page":page,
            "limit":limit,
            "key":key,
            "status_code":status_code
        }
        response = requests.post(url,headers=headers,json=data)
        return response