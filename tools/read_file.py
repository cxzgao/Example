import json

class ReadJson(object):
    # ʹ�ù��캯�����������filename,��data�����ļ�
    def __init__(self,filename):
        self.filepath = "../data/"+filename
    # ��data�����ļ������ļ���ȡ��file�ļ���
    def read_json(self):
        with open(self.filepath, "r",encoding="utf-8") as file:
            # ʹ�÷���load() �����ļ�file
            return json.load(file)