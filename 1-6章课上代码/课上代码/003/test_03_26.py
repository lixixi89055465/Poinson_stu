# -*- coding: utf-8 -*-
# @Time : 2025/11/24 22:34
# @Author : nanji
# @Site : 
# @File : test_03_26.py
# @Software: PyCharm
# @Comment :
from langchain_classic.chains.llm import LLMChain
from langchain_core.output_parsers import StrOutputParser
import os
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableSequence

from langchain_deepseek import ChatDeepSeek
from dotenv import load_dotenv

load_dotenv('../assets/.env')
prompt = ChatPromptTemplate.from_template(
    '你好，我是{city}{name}'
)
prompt2 = prompt.partial(city='哈尔滨')
print("prompt2=", prompt2)
msg = prompt2.format(name='吴彦祖')
print("msg=", msg)
load_dotenv('../assets/.env')
llm = ChatDeepSeek(
    stop='好',
    model=os.getenv('MODEL_NAME'),
    temperature=0.8
)
chain = prompt | prompt2 | prompt2 | llm
print("1" * 100)
print('类型chain=', type(chain))
print("5" * 100)
print(chain)
# oldChain:LLMChain

json = chain.model_dump_json()
print("2" * 100)
print("json=", json)  # 通过json查看chain里面的顺序

ai_msg = chain.invoke({"name": "吴彦祖", "city": "上海"})
t = prompt2.invoke({"name": "吴彦祖"})  # 提示词模板的invoke要的input是一个字典,所以要用{}
print("4" * 100)
print(t)
print("3" * 100)
print("ai_msg=", ai_msg)
str1: str = "你好{name}"
msg2 = str1.format(name="彭于晏")  # 默认python的字符串str就有格式化

print("2" * 100)
print("msg2=", msg2)
