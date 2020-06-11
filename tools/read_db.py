# -*- coding:utf-8 -*-
"""
   完成数据库相关工具类封装
   主要方法：
       1、假设
   辅助方法：
       1、获取连接对象
       2、获取游标对象
       3、关闭游标对象方法
       4、关闭连接对象方法
"""
# 导包 pymysql
# 新建类 数据库

import pymysql

class ReadDB:
    conn = ""
    # 获取连接对象方法
    def get_conn(self):
        if self.conn == "":
            self.conn = pymysql.connect(host="rm-uf6sw0zy3s2a732e6bo.mysql.rds.aliyuncs.com",
                       port=3306,
                       user="chat_test",
                       password="o649D83a6cyT7299",
                       database="chat_test",
                       charset="utf8")
        # 返回连接对象
        return self.conn
    # 获取游标连接对象
    def get_cursor(self):
        # 获取游标对象
        cursor = self.get_conn().cursor()
        # 返回游标对象
        return cursor
    # 关闭游标对象
    def close_cursor(self,cursor):
        try:
            if cursor:
                cursor.close()
        except:
            print("异常退出")
    # 关闭连接对象
    def close_conn(self):
        try:
            if self.conn:
                self.conn.close()
                self.conn=""
        except:
            print("异常退出")

    # 主要执行方法
    def get_sql_one(self,sql):
        # 定义游标对象及数据变量
        sursor = ""
        data = ""
        try:
            # 获取游标对象
            sursor = self.get_cursor()
            # 调用执行方法
            sursor.execute(sql)
            # 获取结果
            data = sursor.fetchone()
        except Exception as e:
            print("get_sql_one error:",e)
        finally:
            # 关闭游标对象
            self.close_cursor(sursor)
            # 关闭连接对象
            self.close_conn()
            # 返回执行结果
            return data

    # 获取数据库所有结果集
    def get_sql_all(self, sql):
        # 定义游标对象及数据变量
        sursor = ""
        data = ""
        try:
            # 获取游标对象
            sursor = self.get_cursor()
            # 调用执行方法
            sursor.execute(sql)
            # 获取结果
            data = sursor.fetchall()
        except Exception as e:
            print("get_sql_all error:", e)
        finally:
            # 关闭游标对象
            self.close_cursor(sursor)
            # 关闭连接对象
            self.close_conn()
            # 返回执行结果
            return data

    # 修改/删除方法的封装
    def update_sql(self, sql):
        # 定义游标对象及数据变量
        sursor = ""
        data = ""
        try:
            # 获取游标对象
            sursor = self.get_cursor()
            # 调用执行方法
            sursor.execute(sql)
            # 事务提交
            self.conn.commit()
        except Exception as e:
            # 事务回滚
            self.conn.rollback()
            print("gupdate_sql error:", e)
        finally:
            # 关闭游标对象
            self.close_cursor(sursor)
            # 关闭连接对象
            self.close_conn()