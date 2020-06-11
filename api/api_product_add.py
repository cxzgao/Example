import requests
from case.test_token import TestLogin

class Api_Product(object):
    def api_product(self,url,product_id,title,image,describe,price):
        headers = {"Content-Type": "application/json",
                   "Authorization": TestLogin().test_testlogin()
                   }
        data = {"product_id": product_id,
                "title": title,
                "image": "",
                "describe": describe,
                "price": price
                }
        return requests.post(url,headers=headers,json=data)