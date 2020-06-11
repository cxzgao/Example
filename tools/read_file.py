import json

class ReadJson(object):
    # 使用构造函数，传入参数filename,打开data数据文件
    def __init__(self,filename):
        self.filepath = "../data/"+filename
    # 打开data数据文件并将文件读取到file文件中
    def read_json(self):
        with open(self.filepath, "r",encoding="utf-8") as file:
            # 使用方法load() 加载文件file
            return json.load(file)