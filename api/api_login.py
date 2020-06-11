"""登录接口对象封装"""
# 导入requests包
# 新建类—登陆
# 新建方法—登陆方法
     # headers定义
     # data定义
     # 调用post并返回响应对象

import requests

class ApiLogin(object):
    def api_login(self,url,username,password):
        headers = {"Content-Type":"application/json"}
        data = {"username":username,
                "password":password}
        # 返回响应信息
        return requests.post(url,headers=headers,json=data)

# url、data：需要从data数据文件中读取出来，做参数使用，
# 所以api_post_login方法使用动态传参
