"""读取json数据"""
# 导包 json
# 打开json文件并获取文件流
# 调用load方法加载文件流

# 使用参数替换 静态文件名
import json

class ReadJson(object):
    def __init__(self,filename):
        self.filepath = "./data/"+filename

    def read_json(self):
        with open(self.filepath, "r", encoding="utf-8") as f:
            return json.load(f)

# 读取字典内容，并添加到新的列表中
if __name__ == '__main__':
    # 调用类方法 read.json()，传参 login.json
    datas = ReadJson("admin.json").read_json()
    # 新建空列表，添加读取json数据data
    arrs = []
    for data in datas.values():
        arrs.append((data.get("url"),
                     data.get("admin_id"),
                     data.get("username"),
                     data.get("admin_name"),
                     data.get("password"),
                     data.get("admin_status"),
                     data.get("status_code")))
    print(arrs)
