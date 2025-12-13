# -*- coding: utf-8 -*-
# @Time : 2025/12/7 12:15
# @Author : nanji
# @Site : 
# @File : 04_03.py
# @Software: PyCharm
# @Comment :
import asyncio
from langchain_core.runnables import RunnableLambda


def add(a, b):
    result = a + b
    print('add()=', result)
    return (result, 1)


# print(add(1, 1))

async def sub(a, b):
    result = a - b
    print("异步方法执行sub()=", result)
    return (result, 1)  # 这里是为了返回元组,可以连续的invoke


# sub(1,1)#不能直接调用
# asyncio.run(sub(10, 1))

async def sub_run():
    await sub(10, 1)


# print("1" * 100)
# asyncio.run(sub_run())
# print("2" * 100)
runnable1 = RunnableLambda(lambda x: add(x[0], x[1]))
# a = runnable1.invoke((1, 1))
# print(a)
# b=runnable1.ainvoke((1,1))
# print("3"*100)
# print(b)
runable2 = RunnableLambda(lambda x: add(x[0], x[1]), afunc=lambda x: sub(x[0], x[1]))

chain = runnable1 | runable2


async def run2():
    await runable2.ainvoke((10, 9))


asyncio.run((runable2 | runable2).ainvoke((10, 9)))  # 连续调用2次ainvoke
# ainvoke的输入,是传入的参数,输出是 函数的return返回值
print("铭刻:义父追魂戟,把离手越进义父离你越远>---红字增幅+26----------)三(--> ")
a = runable2.invoke((3, 3))
print(a)
