import requests
from case.test_token import TestLogin

class Api_Red_List(object):
    def api_red_list(self,url,page,limit,create_time_start,create_time_end,red_packet_type,user_info,group_info,order_field,order_by):
        headers = {"Content-Type": "application/json",
                   "Authorization": TestLogin().test_testlogin()}
        data = {
            "page":page,
            "limit":limit,
            "create_time_start":create_time_start,
            "create_time_end":create_time_end,
            "red_packet_type":red_packet_type,
            "user_info":user_info,
            "group_info":group_info,
            "order_field":order_field,
            "order_by":order_by
        }
        return requests.post(url,headers=headers,json=data)