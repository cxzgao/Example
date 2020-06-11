import requests
from case.test_token import TestLogin

class Api_UserList(object):
    def api_userlist(self,url,page,limit,is_realname,user_status,start_time,end_time,order_field,order_by,key):
        headers = {"Content-Type":"application/json",
                   "Authorization":TestLogin().test_testlogin()}
        data = {"page":page,
                "limit":limit,
                "is_realname":is_realname,
                "user_status":user_status,
                "start_time":start_time,
                "end_time":end_time,
                "order_field":order_field,
                "order_by":order_by,
                "key":key}
        return requests.post(url,headers=headers,json=data)