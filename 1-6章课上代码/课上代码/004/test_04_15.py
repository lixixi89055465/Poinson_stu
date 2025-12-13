# -*- coding: utf-8 -*-
# @Time : 2025/12/12 23:42
# @Author : nanji
# @Site : 
# @File : test_04_15.py
# @Software: PyCharm
# @Comment :
# passthrough 穿过的意思
from itertools import chain
from xml.dom.minidom import Document

from langchain_core.runnables import RunnablePassthrough


@chain
def add(a):
    print('add', a)


chain1 = RunnablePassthrough()
print(chain1.invoke(3))

dic = {'docs': [1, 2, 3]}
print("0" * 100)
print('type(dic):', type(dic))
result = RunnablePassthrough().invoke(
    {'docs': [1, 2, 3],
     'question': '我传入的文档中最大的数字是什么?'}
)
print("1"*100)
print(result)
list1 = result["docs"]
for doc in list1:
    print(doc)
