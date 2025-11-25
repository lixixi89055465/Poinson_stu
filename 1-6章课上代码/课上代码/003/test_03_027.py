# -*- coding: utf-8 -*-
# @Time : 2025/11/25 22:44
# @Author : nanji
# @Site : 
# @File : test_03_027.py
# @Software: PyCharm
# @Comment :
# LangChain表达式 LangChain表达式 (LCEL)
# 一般顺序, 提示词 | llm | 解析器
# 前一个可运行对象的 .invoke() 调用的输出作为输入传递给下一个可运行对象。
from langchain_classic.chains.llm import LLMChain
from langchain_core.output_parsers import StrOutputParser
import os

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableSequence
from langchain_deepseek import ChatDeepSeek
from dotenv import load_dotenv
import os
from langchain_deepseek import ChatDeepSeek
from dotenv import load_dotenv

load_dotenv('../assets/.env')
prompt = ChatPromptTemplate.from_template(
    '你好，我是{city} {name}'
)

llm = ChatDeepSeek(
    stop='好',
    model=os.getenv('MODEL_NAME'),
    temperature=0.8
)
# Serializable 可串行化的
# 按顺序,做个提示词+ llm的链
# msg = prompt.invoke({"city": "广东佛山", "name": "吴彦祖"})
# print('msg:', msg)
chain = prompt | llm
# msg = chain.invoke({})
# print(msg)
ai_msg = llm.invoke(prompt.invoke({"city": "广东佛山", "name": "吴彦祖"}))
parser = StrOutputParser()
chain = prompt | llm | parser
text = chain.invoke({"city": "广东佛山", "name": "吴彦祖"})
print('text:', text)

