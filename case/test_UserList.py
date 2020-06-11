import unittest
from api.api_UserList import Api_UserList
from parameterized import parameterized
from tools.read_file import ReadJson

def get_data():
    datas = ReadJson("user_list.json").read_json()
    arrs = []
    for data in datas.values():
        arrs.append((data.get("url"),
                     data.get("page"),
                     data.get("limit"),
                     data.get("is_realname"),
                     data.get("user_status"),
                     data.get("start_time"),
                     data.get("end_time"),
                     data.get("order_field"),
                     data.get("order_by"),
                     data.get("key")))
    print(arrs)
    return arrs

class Test_UserList(unittest.TestCase):

    @parameterized.expand(get_data())
    def test_userlist(self,url,page,limit,is_realname,user_status,start_time,end_time,order_field,order_by,key):
        # 日期转化为时间戳：
        # int(time.mktime(time.strftime("2020-04-30 23:40:00","%Y-%m-%d %H:%M:%S")))
        #start_time = "2020-03-10 10:00:00"

        res = Api_UserList().api_userlist(url,page,limit,is_realname,user_status,start_time,end_time,order_field,order_by,key)
        print(res.json())

if __name__ == '__main__':
    unittest.main()