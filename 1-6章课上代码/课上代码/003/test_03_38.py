# -*- coding: utf-8 -*-
# @Time : 2025/12/6 10:05
# @Author : nanji
# @Site : 
# @File : test_03_38.py
# @Software: PyCharm
# @Comment :
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel, Field
import json


class ZhouZhou(BaseModel):
    """JoJo的奇妙冒险的对象"""  # """doc string"""
    name: str = Field(description="姓名")
    age: str = Field(description="姓名")


class ZhouZhouList(BaseModel):
    list1: list[ZhouZhou] = Field(description='ZhouZhou对象的List列表')


parser = JsonOutputParser(pydantic_object=ZhouZhouList)
# print("parser.get_format_instructions()=",parser.get_format_instructions())
prompt = (ChatPromptTemplate.from_template("给我2个名字要中文{format}")
          .partial(format=parser.get_format_instructions()))
print(prompt)
print("0" * 100)
# print(prompt.format())
import os
from langchain_deepseek import ChatDeepSeek
from dotenv import load_dotenv

load_dotenv('../assets/.env')
llm = ChatDeepSeek(
    model=os.getenv('MODEL_NAME'),
    temperature=0.8
)
chain = prompt | llm | parser
ai_msg = chain.invoke({})
print('ai_msg=', ai_msg)
print('type(ai_msg):', type(ai_msg))
print('铭刻:义父追魂戟,把离手越进义父离你越远>---红字增幅+28----------)三(--> ')
jsonStr = json.dumps(ai_msg, ensure_ascii=False, indent=2)
print('jsonStr:', jsonStr)
