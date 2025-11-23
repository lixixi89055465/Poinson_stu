# -*- coding: utf-8 -*-
# @Time : 2025/11/23 21:26
# @Author : nanji
# @Site : 
# @File : test_03_24.py
# @Software: PyCharm
# @Comment :
import os
from langchain_core.output_parsers import StrOutputParser
from langchain_deepseek import ChatDeepSeek
from dotenv import load_dotenv

load_dotenv('../assets/.env')
llm = ChatDeepSeek(
    stop='好',
    model=os.getenv('MODEL_NAME'),
    temperature=0.8
)
ai_msg = llm.invoke('你好')
print('ai_msg:', ai_msg)

text2 = StrOutputParser().parse(ai_msg)
print('text2:', text2)
