# -*- coding:utf-8 -*-
# 1、读取excel表
# 2、构建接口请求
# 3、测试结果写入excel
import json
import xlrd

# 1、读取excel表
excelDir = r"D:\testcase.xlsx"
workbook = xlrd.open_workbook(excelDir) #打开excel表
#print(workbook.sheet_names())#返回表中的页，list列表
sheet = workbook.sheet_by_name("login")
# 读取一行
# rows = sheet.row_values(1)
#print(rows)
# 读取一列
# cols = sheet.cell_value(1)
# print(cols)
# 读取指定单元格
cellUrl = sheet.cell_value(1,3)
cellData = sheet.cell_value(1,2)
cellHeaders = sheet.cell_value(1,6)
# print(cellUrl,cellData,cellHeaders)
# 返回单元格数据类型，0/1：字符串，2 3 4 5
# print(sheet.cell(1,2).ctype)


# print(sheet.nrows)
# print(sheet.ncols)
# print(sheet.cell(0,0).value)#第一行第一列的值
# print(sheet.row_values(0))#第一行的所有值
# print(dict(zip(sheet.row_values(0),sheet.row_values(1))))#将数据组装成字典形式
# 遍历excel,打印出所有的数据
for i in range(sheet.nrows):
    if i > 0:
        result = sheet.row_values(i)
        print(result)

# 2、构建接口请求
import requests
url = cellUrl
headers = json.loads(cellHeaders) #将str类型的cellHeaders转化为dict字典类型
data = json.loads(cellData)
# print(type(data))
res = requests.post(url,headers=headers,json=data)
# print(res.json())

# 3、测试结果写入excel




