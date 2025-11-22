# -*- coding: utf-8 -*-
# @Time : 2025/11/22 17:26
# @Author : nanji
# @Site : 
# @File : test_03_06.py
# @Software: PyCharm
# @Comment :
import asyncio


async def fun1():
    print('fun1 开始了')
    await asyncio.sleep(10)
    print('fun1 结束了')


async def fun2():
    print('fun2 开始了')
    print('fun2 结束了')


print("1 铭刻:义父追魂戟,把离手越进义父离你越远>---红字增幅+26----------)三(--> ")
asyncio.run(fun1())

print("0" * 100)
asyncio.run(fun2())
