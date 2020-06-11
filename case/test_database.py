# -*- coding:utf-8 -*-
"""
   操作项目数据库
   判断修改管理员信息后，是否修改成功，用户ID：23
   步骤：
   1、导包 pymysql
   2、获取连接对象
   3、获取游标对象
   4、执行方法 sql
   5、获取结果，并进行断言，修改"admin_status":0
   6、关闭游标对象
   7、关闭连接对象
"""

import pymysql
# 获取连接对象
conn = pymysql.connect(host="rm-uf6sw0zy3s2a732e6bo.mysql.rds.aliyuncs.com",
                       port=3306,
                       user="chat_test",
                       password="o649D83a6cyT7299",
                       database="chat_test",
                       charset="utf8")
# 获取游标对象
cursor = conn.cursor()
# 执行方法 sql
sql = "select admin_status from admin where admin_id=23"
cursor.execute(sql)
#print(cursor.fetchone())
# 获取结果，并进行断言
result = cursor.fetchone()[0]
print(result)
try:
    if 0 == result:
        print("修改成功")
except Exception as e:
    print("异常："+e)
finally:
    # 关闭游标对象
    cursor.close()
    # 关闭连接对象
    conn.close()