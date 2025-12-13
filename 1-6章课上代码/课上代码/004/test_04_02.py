# -*- coding: utf-8 -*-
# @Time : 2025/12/7 0:32
# @Author : nanji
# @Site : 
# @File : test_04_02.py
# @Software: PyCharm
# @Comment :
# RunnableLambda 可以把函数封装成Runnable
from langchain_core.runnables import RunnableLambda


def add_one(a):
    result = a + 1
    print('add_one=', result)


funx = lambda x: add_one(x)
a = funx(1)
print(a)
runnable1 = RunnableLambda(lambda x: add_one(x))  # 这2种写法效果一样
print("1" * 100)
print(runnable1)
print("2" * 100)
print(type(runnable1))
runnable1.invoke(1)  # invoke有输入有输出
print("3" * 100)
runnable1.invoke(2)
