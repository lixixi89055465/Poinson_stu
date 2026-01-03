# -*- coding: utf-8 -*-
# @Time : 2026/1/3 11:40
# @Author : nanji
# @Site : 
# @File : test_05_45.py
# @Software: PyCharm
# @Comment :
from langchain_core.messages import (SystemMessage,
                                     HumanMessage,
                                     AIMessage,
                                     trim_messages,
                                     BaseMessage)
from langchain_core.output_parsers import StrOutputParser

msg = [
    SystemMessage("你是一个漂亮年轻的李阿姨,实际年龄比我小"),
    HumanMessage("我是一个钛合金钢铁直男,48k纯爷们,碳纤维的,但是我是软饭男"),
    AIMessage("我给你我的附属金卡"),
    HumanMessage("你在教我做事啊?"),
]


def azu_token_counter(messages):
    total = 0
    for msg in messages:
        total += len(msg.content)
    return total


# 自定义的一个token计数器
trimmer = trim_messages(
    max_tokens=30,
    token_counter=azu_token_counter,
    strategy="last"
)
import os
from langchain_deepseek import ChatDeepSeek
from dotenv import load_dotenv

load_dotenv('../../assets/.env')
llm = ChatDeepSeek(
    model=os.environ.get("MODEL_NAME"),
    temperature=0.8
)
chain = trimmer | llm | StrOutputParser()
result = chain.invoke(msg)
print('result:', result)
