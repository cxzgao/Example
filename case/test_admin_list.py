import unittest
from api.api_admin_list import Api_AdminList
from parameterized import parameterized
from tools.read_file import ReadJson

def get_data():
    # 使用ReadJson方法读取data文件内容，并把内容写入空数据中
    datas = ReadJson("admin_list.json").read_json()
    arrs = []
    for data in datas.values():
        arrs.append((data.get("url"),
                     data.get("page"),
                     data.get("limit"),
                     data.get("key"),
                     data.get("status_code")))
    #print(arrs)
    return arrs

class Test_AdminList(unittest.TestCase):
    @parameterized.expand(get_data())
    def test_admin_list(self,url,page,limit,key,status_code):
        response = Api_AdminList().api_adminlist(url,page,limit,key,status_code)

        if response.status_code==200:
            print("返回对应的列表数据：")
            print(response.json())

if __name__ == '__main__':
    unittest.main()