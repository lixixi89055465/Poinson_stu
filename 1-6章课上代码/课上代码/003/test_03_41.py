# -*- coding: utf-8 -*-
# @Time : 2025/12/6 12:19
# @Author : nanji
# @Site : 
# @File : test_03_41.py
# @Software: PyCharm
# @Comment :
from langchain_core.output_parsers import XMLOutputParser, StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

# 西格玛男人之机智的小军
# parser = XMLOutputParser(tags=[
#     "小军来尝尝李阿姨新摘的樱桃时候,的回复",
#                       "小军阿姨心情不太好来陪问姨上去聊聊天,如何回答"
#                       ])#带标签的,就是让大模型,返回自己输入的标签
parser = XMLOutputParser()
query = '给我生成一个<西格玛男人之机智的小军的语言操作手册>'
print("0" * 100)
print(parser.get_format_instructions())
prompt = ChatPromptTemplate.from_template(
    "{query}{format_introduce}tags标签<>里不要有任何符号只有中文"
).partial(query=query, format_introduce=parser.get_format_instructions())

print(prompt.format())
import os
from langchain_deepseek import ChatDeepSeek
from dotenv import load_dotenv

load_dotenv('../assets/.env')
llm = ChatDeepSeek(
    model=os.getenv('MODEL_NAME'),
    temperature=0.8
)
# chain = prompt | llm | StrOutputParser()
# ai_msg = chain.invoke({})
# print("1" * 100)
# print('ai_msg:', ai_msg)
# 用解析器转成字典

chain = prompt | llm | XMLOutputParser()
ai_msg = chain.invoke({})
print('ai_msg;', ai_msg)
print(type(ai_msg), type(ai_msg))

import json

jsonStr = json.dumps(ai_msg, ensure_ascii=False, indent=2)
print('jsonStr:', jsonStr)
