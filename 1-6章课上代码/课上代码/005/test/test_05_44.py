# -*- coding: utf-8 -*-
# @Time : 2026/1/3 10:50
# @Author : nanji
# @Site : 
# @File : test_05_44.py
# @Software: PyCharm
# @Comment :
from langchain_core.messages import (SystemMessage,
                                     HumanMessage,
                                     AIMessage,
                                     trim_messages,
                                     BaseMessage)

msg = [
    SystemMessage("你是一个漂亮年轻的李阿姨,实际年龄比我小"),
    HumanMessage("我是一个钛合金钢铁直男,48k纯爷们,碳纤维的,但是我是软饭男"),
    AIMessage("我给你我的附属金卡"),
    HumanMessage("你在教我做事啊?"),
]


# msg1 = "你是一个漂亮年轻的李阿姨,实际年龄比我小"
# print(len(msg1))
# 自定义的一个token计数器
def azu_token_counter(messages):
    print("1" * 100)
    total = 0
    for msg in messages:
        print(f'msg.content=,{msg.content}')
        total += len(msg.content)
    print(f'total={total}')
    return total  # 返回总共的token数


trim_messages = trim_messages(
    msg,
    max_tokens=40,
    token_counter=azu_token_counter,
    # strategy="first",  # strategy="last",#last从后截取
    strategy="last",  # strategy="last",#last从后截取
    # allow_partial=False,  # first从前截取
)
print("0" * 100)
print('trim_messages=', trim_messages)
