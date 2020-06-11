import requests

class Api_L(object):
    def api_l(self,url,username,password):
        headers = {"Content-Type":"application/json"}
        data = {"username":username,
                "password":password}
        return requests.post(url,headers=headers,json=data)