# -*- coding: utf-8 -*-
# @Time : 2025/12/6 12:02
# @Author : nanji
# @Site : 
# @File : test_03_40_b.py
# @Software: PyCharm
# @Comment :
# JsonOutputParser 和 PydanticOutputParser (xml解析器,
# 都是通过在提示词中增加get_format_introduce 对大模型进行说明,前提是要大模型支持Json格式
# 使用的时候 prompt  | llm | parser 联合使用
from langchain_core.output_parsers import PydanticOutputParser, StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel, Field


class ZhouZhou(BaseModel):
    """JoJo的奇妙冒险的对象"""  # """doc string"""
    name: str = Field(description="姓名")
    age: int = Field(description="年龄")


class ZhouZhouList(BaseModel):
    list1: list[ZhouZhou] = Field(description="ZhouZhou对象的List列表")


parser = PydanticOutputParser(pydantic_object=ZhouZhouList)
print('parser.get_format_instructions():', parser.get_format_instructions())
prompt = (ChatPromptTemplate.from_template('给我2个名字要中文{format}')
          .partial(format=parser.get_format_instructions()))

# print("1" * 100)
# print(prompt)
# print("2" * 100)
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
ai_msg = chain.stream({})  # 返回json解构的字典
print('ai_msg=', ai_msg)
print("3" * 100)
print('type(ai_msg):=', type(ai_msg))
for chunk in ai_msg:
    print('chunk=', chunk)
    print('type(chunk)=', type(chunk))
    print('chunk=',chunk.model_dump_json())

print("4"*100)