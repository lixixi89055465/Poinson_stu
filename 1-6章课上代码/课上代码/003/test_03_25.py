# -*- coding: utf-8 -*-
# @Time : 2025/11/23 21:50
# @Author : nanji
# @Site : 
# @File : test_03_25.py
# @Software: PyCharm
# @Comment :
from langchain_core.output_parsers import BaseOutputParser
import os
from langchain_deepseek import ChatDeepSeek
from dotenv import load_dotenv


class PsParser(BaseOutputParser):
    # def parse(self, ai_msg):#这个是直接外面调用parse,需要自己获取content
    #     print("函数内部ai_msg=",ai_msg)
    #     print("函数内部 type(ai_msg)=", type(ai_msg))
    #     content = ai_msg.content
    #     print("content=", content)
    #     return content
    def parse(self, content):  # 这个是invoke调用的parse
        print("函数内部ai_msg=", ai_msg)
        print("函数内部 type(ai_msg)=", type(ai_msg))
        print("content=", content)
        return content


load_dotenv('../assets/.env')
llm = ChatDeepSeek(
    # stop='好',
    model=os.getenv('MODEL_NAME'),
    temperature=0.8
)
ai_msg = llm.invoke('你好')
print('ai_msg:=', ai_msg)
text = PsParser().invoke(ai_msg)
print("0" * 100)

print('text:=', text)
