# -*- coding: utf-8 -*-
# @Time : 2026/1/10 15:45
# @Author : nanji
# @Site : 
# @File : test_06_07.py
# @Software: PyCharm
# @Comment :
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv('../assets/.env')
import os
from langchain_deepseek import ChatDeepSeek

llm = ChatDeepSeek(
    model=os.getenv('MODEL_NAME'),
    temperature=0.8
)
chain = llm | StrOutputParser()
ai_msg = chain.invoke('你好')
print(ai_msg)
