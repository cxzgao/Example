import requests
from case.test_user_token import Test_UserLogin

class Api_RedCreate(object):
    def api_redcreate(self,url,amount,number,pay_password,receiver_id,red_packet_type,title):
        headers = {"Content-Type": "application/json",
                   "Authorization": Test_UserLogin().test_userlogin()}
        data = {
            "amount": amount,
            "number": number,
            "pay_password": pay_password,
            "receiver_id":receiver_id,
            "red_packet_type": red_packet_type,
            "title":title
        }
        return requests.post(url,headers=headers,json=data)