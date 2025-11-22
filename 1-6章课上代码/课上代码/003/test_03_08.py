# -*- coding: utf-8 -*-
# @Time : 2025/11/22 18:28
# @Author : nanji
# @Site : 
# @File : test_03_08.py
# @Software: PyCharm
# @Comment :

import asyncio
import os
from langchain_deepseek import ChatDeepSeek
from dotenv import load_dotenv


async def invoke1(llm: ChatDeepSeek, msg: str) -> str:
    result: str=''
    async for item in llm.astream(msg):
        print(item.content, end='')
        result += item.content
    print('结果是:', result)
    return result
    # print("嘎斯罐1开始了↑")
    # res = await llm.ainvoke(msg)
    # print(res)
    # print("1的结果", res.content)
    # print("嘎斯罐1结束了了↑")
    # return res.content


async def invoke2(llm: ChatDeepSeek, msg: str) -> str:
    print("嘎斯罐2开始了↑")
    res = await llm.ainvoke(msg)
    print(res)
    print("2的结果", res.content)
    print("嘎斯罐2结束了了↑")
    return res.content


async def start():
    load_dotenv('../assets/.env')
    llm = ChatDeepSeek(model=os.getenv('MODEL_NAME'), temperature=0.8)
    (r1, r2) = await asyncio.gather(invoke1(llm, '嗯没问题'),
                                    invoke2(llm, '实在吃不下了!'))
    print(r1)
    print("2" * 100)
    print(r2)


asyncio.run(start())
