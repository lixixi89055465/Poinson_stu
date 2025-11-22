# -*- coding: utf-8 -*-
# @Time : 2025/11/22 8:46
# @Author : nanji
# @Site : 
# @File : test_002_037.py
# @Software: PyCharm
# @Comment :
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_community.callbacks.manager import get_openai_callback
msg='你好'
load_dotenv('../assets/.env')
llm=ChatOpenAI(model=os.getenv('MODEL_NAME'),temperature=0.8)
with get_openai_callback() as cb:
    res=llm.invoke(msg)
    print(cb.prompt)
    print(cb.completion_tokens)
    print(cb.total_tokens)
    print(f'res.response_metadata={res.response_metadata}')
print(res.content)
print(cb.total_tokens)


