import requests

class Api_User_Login(object):
    def api_userlogin(self,url,mobile,password):
        headers = {"Content-Type": "application/json"}
        data = {
            "mobile":mobile,
            "password":password
        }
        return requests.post(url,headers=headers,json=data)