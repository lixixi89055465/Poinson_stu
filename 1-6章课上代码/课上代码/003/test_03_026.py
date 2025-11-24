# -*- coding: utf-8 -*-
# @Time : 2025/11/24 23:06
# @Author : nanji
# @Site : 
# @File : test_03_026.py
# @Software: PyCharm
# @Comment :
# LangChain表达式 LangChain表达式 (LCEL)
# 一般顺序, 提示词 | llm | 解析器
# 前一个可运行对象的 .invoke() 调用的输出作为输入传递给下一个可运行对象。
import os

from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_deepseek import ChatDeepSeek

load_dotenv('../assets/.env')
prompt = ChatPromptTemplate.from_template(
    "你好,我是{city}{name}"
)
llm = ChatDeepSeek(
    stop='好',
    model=os.getenv('MODEL_NAME'),
    temperature=0.8
)
# Serializable 可串行化的
# 按顺序,做个提示词+ llm的链
msg = prompt.invoke({
    "city": "广东佛山", "name": "吴彦祖"
})
print("0" * 100)
print("msg", msg)

# chain = prompt | llm
# a = chain.invoke({})
# print(a)
parser = StrOutputParser()
chain = prompt | llm | parser
text=chain.invoke({"city": "广东佛山", "name": "吴彦祖"})
print("text", text)

