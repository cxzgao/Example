import json

class ReadJson(object):
    # 使用构造函数，传入参数filename,打开data数据文件
    def __init__(self,filename):
        self.filepath = "./data/"+filename
    # 打开data数据文件并将文件读取到f文件中
    def read_json(self):
        with open(self.filepath,"r",encoding="utf-8") as f:
            # 使用方法load() 加载文件f
            return json.load(f)

if __name__ == '__main__':
    #使用ReadJson方法读取data文件内容，并把内容写入空数据中
    datas = ReadJson("admin_list.json").read_json()
    arrs = []
    for data in datas.values():
        arrs.append((data.get("url"),
                     data.get("headers"),
                     data.get("page"),
                     data.get("limit"),
                     data.get("key"),
                     data.get("status_code")))
    print(arrs)