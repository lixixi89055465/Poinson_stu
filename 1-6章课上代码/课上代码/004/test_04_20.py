# -*- coding: utf-8 -*-
# @Time : 2025/12/13 10:29
# @Author : nanji
# @Site : 
# @File : test_04_20.py
# @Software: PyCharm
# @Comment :
# fall_back 意思是 备用 ,后退,作用,如果发现错误,就是用 [] List列表中的元素
from langchain_core.runnables import chain
from langsmith import expect


@chain
def normalFun(input: str):
    index = input.find("李阿姨")
    print("李阿姨index=", index)
    if index == -1:
        print("今天真开心啊,我要想干嘛干嘛了")
    else:
        print("警告:探测到在图的核聚变打击,位置index=", index)
        raise ValueError
    import os
    from langchain_deepseek import ChatDeepSeek
    from dotenv import load_dotenv
    load_dotenv('../assets/.env')
    llm = ChatDeepSeek(
        temperature=0.8
    )
    llm.invoke(input)


@chain
def errorFun1(input: str):
    print("1" * 100)
    index = input.find("做饭")
    print("做饭index=", index)
    if index == -1:
        print("不了,我要回家吃饭")
    else:
        raise ValueError("要来家里做饭了")
        # print("备用方法1执行")
        # print("我小军,今天就算饿死,也不会吃你做的饭")


@chain
def errorFun2(input: str):
    print("2" * 100)
    print("你在教我做事啊")


chain = normalFun.with_fallbacks([errorFun2, errorFun1])
# r1 = chain.invoke("来尝尝李阿姨新摘的樱桃")
# r1 = chain.invoke("小军啊,李阿姨今天要去你家做饭,小军啊,我给你我的附属金卡")
# chain.invoke("")print("0" * 100)
# print(r1)
try:
    raise ValueError('要来家里做饭了')
except Exception as error:
    print('e=', error)

