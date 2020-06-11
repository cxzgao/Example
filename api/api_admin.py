"""登录接口对象封装"""
# 导入requests包
# 新建类—用户列表
# 新建方法—用户列表方法
     # headers定义
     # data定义
     # 调用post并返回响应对象

import requests
from case.test_token import TestLogin

class Api_Admin(object):
    # 新建新增管理员方法
    def api_admin(self,url,admin_id,username,admin_name,password,admin_status,status_code):
        headers = {"Content-Type": "application/json",
                   "Authorization": TestLogin().test_testlogin()}
        data = {"admin_id":admin_id,
                "username":username,
                "admin_name":admin_name,
                "password":password,
                "admin_status":admin_status,
                "status_code": status_code}
        # 返回响应信息
        return requests.post(url,headers=headers,json=data)
