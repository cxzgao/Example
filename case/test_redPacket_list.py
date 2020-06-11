import unittest
from api.api_redPacket_list import Api_Red_List
from tools.read_file import ReadJson
from parameterized import parameterized

def get_data():
    datas = ReadJson("redpacket_list.json").read_json()
    arrs = []
    for data in datas.values():
        arrs.append((data.get("url"),
                     data.get("page"),
                     data.get("limit"),
                     data.get("create_time_start"),
                     data.get("create_time_end"),
                     data.get("red_packet_type"),
                     data.get("user_info"),
                     data.get("group_info"),
                     data.get("order_field"),
                     data.get("order_by")))
    return arrs

class Test_RedPacketList(unittest.TestCase):

    @parameterized.expand(get_data())
    def test_redpacketlist(self,url,page,limit,create_time_start,create_time_end,red_packet_type,user_info,group_info,order_field,order_by):
        res = Api_Red_List().api_red_list(url,page,limit,create_time_start,create_time_end,red_packet_type,user_info,group_info,order_field,order_by)
        print(res.json()['result'])
        print("\r\n")

if __name__ == '__main__':
    unittest.main()