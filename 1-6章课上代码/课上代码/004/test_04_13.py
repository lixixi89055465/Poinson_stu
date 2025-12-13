# -*- coding: utf-8 -*-
# @Time : 2025/12/12 23:16
# @Author : nanji
# @Site : 
# @File : test_04_13.py
# @Software: PyCharm
# @Comment :
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableLambda, chain


@chain
def add_one(a):
    result = a + 1
    print('add_one调用 result=', result)
    return result


print(add_one)
print("0" * 100)
print(id(add_one))


@chain
def run1(_):
    print('run1')


print("1" * 100)
print(run1)


@chain
def run2(a):
    print('run2 a=', a)


# 管道操作符,会强制转换函数类型为RunnableLamda
chain1 = add_one | (lambda x: x + 1) | (lambda x: x + 1) | {'run2': run2, 'run1': run1}
# print("type(chain1)=",type(chain1)) #管道操作符,返回RunnableSequence对象,

print("铭刻:义父追魂戟,把离手越进义父离你越远>---红字增幅+26----------)三(--> ")
print("1" * 100)
a = chain1.invoke(3)
print("2" * 100)
print(a)
chain1 = ChatPromptTemplate.from_template('')
dic1 = chain1.to_json()
print("3" * 100)
print('dic1:', dic1)

import json

jsonStr = json.dumps(dic1, ensure_ascii=False, indent=2)

