# -*- coding: utf-8 -*-
# @Time : 2025/12/6 11:06
# @Author : nanji
# @Site : 
# @File : test_03_39.py
# @Software: PyCharm
# @Comment :
# JsonOutputParser 和 PydanticOutputParser (xml解析器,
# 都是通过在提示词中增加get_format_introduce 对大模型进行说明,前提是要大模型支持Json格式
# 使用的时候 prompt  | llm | parser 联合使用
from langchain_core.output_parsers import JsonOutputParser, StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel, Field
import json


class ZhouZhou(BaseModel):
    """JoJo的奇妙冒险的对象"""  # """doc string"""
    name: str = Field(description="姓名")
    age: int = Field(description="姓名")


class ZhouZhouList(BaseModel):
    list1: list[ZhouZhou] = Field(description='ZhouZhou对象的List列表')


parser = JsonOutputParser(pydantic_object=ZhouZhouList)
# print(parser.get_format_instructions())
prompt = (ChatPromptTemplate.from_template('给我2个名字要中文{format}')
          .partial(format=parser.get_format_instructions()))
print("1" * 100)
print(prompt)
print("2" * 100)
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
# result = prompt.stream({})
# for item in result:
#     print('item=', item)
# print("3" * 100)
# ai_msg = chain.stream({})  ##返回json解构的字典
# for chunk in ai_msg:
#     print(chunk, end='')

chain = prompt | llm | JsonOutputParser()
ai_msg = chain.stream({})  # 返回json解构的字典
print("4" * 100)
for chunk in ai_msg:
    jsonStr = json.dumps(chunk, ensure_ascii=False, indent=2)
    print('jsonStr:', jsonStr, end='')

print("5" * 100)
