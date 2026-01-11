# -*- coding: utf-8 -*-
# @Time : 2026/1/11 23:37
# @Author : nanji
# @Site : 
# @File : test_06_15.py
# @Software: PyCharm
# @Comment :
import sqlite3

# 连接到 SQLite 数据库
conn = sqlite3.connect("langgraph.db",check_same_thread=False)#创建链接,关闭检查相同线程,langgraph是多线程,默认sqlite是单线程
conn.row_factory = sqlite3.Row
# 打开游标
cursor = conn.cursor()
cursor.execute("select * from writes")
result = cursor.fetchall()
for row in result:
    print(f"thread_id: {row["thread_id"]}")
    print(f"checkpoint_ns: {row["checkpoint_ns"]}")
    print(f"checkpoint_id: {row["checkpoint_id"]}")
    print(f"task_id: {row["task_id"]}")
    print(f"idx: {row["idx"]}")
    print(f"channel: {row["channel"]}")
    print(f"type: {row["type"]}")
    print(f"value: {row["value"]}")

# 先关闭游标,再关闭连接

cursor.close()
conn.close()
