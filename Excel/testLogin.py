# -*- coding:utf-8 -*-
import requests
import unittest
import json
from Excel.readExcel import *

class TestLogin(unittest.TestCase):

    #每个测试类执行之前运行
    @classmethod
    def setUpClass(cls) -> None:
        cls.data_list = excel_list(r"D:\testcase.xlsx","login")

    def test_login(self):
        case_data = get_test_data(self.data_list,"登陆")
        if not case_data:
            print("用例为空")
        url = case_data.get('url')
        data = case_data.get('data')
        headers = case_data.get('headers')
        status = case_data.get('status')
        res = requests.post(url=url,data=json.loads(data))
        print(res.json())
        self.assertEqual(res.status_code,status)
if __name__ == '__main__':
    unittest.main()