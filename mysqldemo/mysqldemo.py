__author__ = 'xudazhou'

import pymysql

conn = pymysql.connect(host="127.0.0.1", port=3306, user="root", password="123456", db="test")
cur = conn.cursor()
cur.execute("SELECT version()")
rs = cur.fetchone()
print(rs)
print(rs[0])