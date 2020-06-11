import unittest
from api.api_product_add import Api_Product

class Test_Product(unittest.TestCase):
    def test_product(self):
        url = "http://t-chat-api.zaomeijia.cn/manage/product/add"
        product_id = 6
        title = "title"
        image = ""
        describe = "describe"
        price = 1000
        res = Api_Product().api_product(url,product_id,title,image,describe,price)
        print(res.json())

if __name__ == '__main__':
    unittest.main()