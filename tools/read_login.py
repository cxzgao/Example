"""读取json数据"""
# 导包 json
# 打开json文件并获取文件流
# 调用load方法加载文件流

# import json
# 打开json文件并获取文件流, r=read, f 代表重命名的文件
#with open("../data/login.json","r",encoding="utf-8") as f:
    # 调用load方法加载文件流
#    data = json.load(f)
    # 读取到的data数据
#    print(data)

# 1、未经封装无法在其他模块直接调用使用;
# 2、数据存储文件太多，在读取文件时路径不能写死
# 3、预期格式为列表嵌套格式[(url,username...)],目前返回的时字典格式
# 4、预期格式为列表嵌套格式[(url,username...)],目前返回的时字典格式

# 1、解决方法：进行封装，使用函数进行封装;
# 2、使用参数替换静态写死的文件名
# 3、读取字典内容，并添加到新的列表中

# 使用参数替换静态写死的文件名
import json
#def read_json():
#    with open("../data/login.json", "r", encoding="utf-8") as f:
#        return json.load(f)

# 使用参数替换 静态文件名
import json

class ReadJson(object):
    def __init__(self,filename):
        self.filepath = "./data/"+filename

    def read_json(self):
        with open(self.filepath, "r",encoding="utf-8") as f:
            return json.load(f)


#if __name__ == '__main__':
    # 调用类方法 read.json()，传参 login.json
#    ReadJson("login.json").read_json()
    # print(ReadJson("login.json").read_json())  # 返回login.json文件中的数据

# 3、读取字典内容，并添加到新的列表中
if __name__ == '__main__':
    # 调用类方法 read.json()，传参 login.json
    data = ReadJson("login.json").read_json()
    # 新建空列表，添加读取json数据data
    arrs = []
    arrs.append((data.get("url"),
                 data.get("username"),
                 data.get("password"),
                 data.get("errcode"),
                 data.get("status_code")))
    print(arrs)
