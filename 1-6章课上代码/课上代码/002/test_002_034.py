# -*- coding: utf-8 -*-
# @Time : 2025/11/20 22:52
# @Author : nanji
# @Site : 
# @File : test_002_034.py
# @Software: PyCharm
# @Comment :
import os
from dotenv import load_dotenv
from langchain_openai import OpenAI, ChatOpenAI
# from openai import OpenAI
msg = '你好'
load_dotenv('../assets/.env')
# llm = OpenAI(model=os.getenv('MODEL_NAME'), temperature=0.8)
llm = ChatOpenAI(model=os.getenv('MODEL_NAME'), temperature=0.8)
res = llm.invoke(msg)
print(res.content)
