import unittest
from api.api_red_create import Api_RedCreate
from tools.read_file import ReadJson
from parameterized import parameterized

def get_data():
    datas = ReadJson("red_create.json").read_json()
    arrs = []
    for data in datas.values():
        arrs.append((data.get("url"),
                     data.get("amount"),
                     data.get("number"),
                     data.get("pay_password"),
                     data.get("receiver_id"),
                     data.get("red_packet_type"),
                     data.get("title")))
    print(arrs)
    return arrs

class Test_RedCreate(unittest.TestCase):

    @parameterized.expand(get_data())
    def test_redcreate(self,url,amount,number,pay_password,receiver_id,red_packet_type,title):
        """
        url = "http://t-chat-api.zaomeijia.cn/app/red/packet/create"
        amount = 300000
        number = 1
        pay_password = "111111"
        receiver_id = "132"
        red_packet_type = 1
        title = "123456"
        """

        res = Api_RedCreate().api_redcreate(url,amount,number,pay_password,receiver_id,red_packet_type,title)
        # 判断返回结果的 errcode 是否等于0
        #self.assertEquals(0,res.json()['errcode'])
        # 判断返回结果的 状态码是否等于 200
        if 100 == res.status_code:
            print("true")
        else:
            print("false")
        print(res.json())

if __name__ == '__main__':
    unittest.main()