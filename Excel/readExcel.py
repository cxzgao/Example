# -*- coding:utf-8 -*-
import xlrd

def excel_list(data_file,sheet):
    data_list = []
    wb = xlrd.open_workbook(data_file)
    sh = wb.sheet_by_name(sheet)
    header = sh.row_values(0)
    for i in range(1,sh.nrows):
        d = dict(zip(header,sh.row_values(i)))#将标题和数据组装成字典，返回
        data_list.append(d)
    #print(data_list)
    return data_list

def get_test_data(data_list,case_name):
    for case_data in data_list:
        # 如果字典中数据中的case_name与参数一致，返回
        if case_name == case_data['case_name']:
            return case_data#如果没有查询到对应的case_name，返回None

if __name__ == '__main__':
    data_list = excel_list(r"D:\testcase.xlsx","login")
    case_data = get_test_data(data_list,"ceshi")
    print(case_data)

