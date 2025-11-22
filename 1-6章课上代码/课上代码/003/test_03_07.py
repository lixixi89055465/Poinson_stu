# -*- coding: utf-8 -*-
# @Time : 2025/11/22 17:41
# @Author : nanji
# @Site : 
# @File : test_03_07.py
# @Software: PyCharm
# @Comment :
import asyncio


async def gasGuan1():
    print('1蛋清气体重力加速系统冲天瞄准!')
    await asyncio.sleep(1)
    print("1重力加速,深蹲的时候,变成倒立,变成肩膀中束锻炼↑")


async def gasGuan2():
    print("2蛋清气体重力加速系统冲地面瞄准↓")
    await asyncio.sleep(0)
    print("2平时蹲100,力量举130,人间大炮一级准备:蹲200↓")


async def fun3():
    pass


async def main():
    # f:asyncio.Future=asyncio.gather(gasGuan1(),gasGuan2())
    f = asyncio.gather(gasGuan1(), gasGuan2())
    await f

asyncio.run(main())
