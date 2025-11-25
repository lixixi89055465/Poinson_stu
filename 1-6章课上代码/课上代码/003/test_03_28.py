# -*- coding: utf-8 -*-
# @Time : 2025/11/25 23:03
# @Author : nanji
# @Site : 
# @File : test_03_28.py
# @Software: PyCharm
# @Comment :
from langchain_core.output_parsers import PydanticOutputParser, StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel, Field, field_validator


class ZhouZhou(BaseModel):
    name: str = Field(description='JoJo的奇妙冒险里的任务名字')
    age: int = Field(default=18)


@field_validator('age')
def validate_age(value):
    if value < 18:
        print("未满十八岁")
        raise ValueError("西格玛男人,从不落入女人陷阱")
    if value > 65:
        print("退休了,可以回家打游戏,到大街上,抽嘎了")


parser = PydanticOutputParser(pydantic_object=ZhouZhou)
# print("0"*100)

# print(parser.get_format_instructions())
t1 = ChatPromptTemplate.from_template("给我{count}个名字{get_format_instructions}")
prompt = t1.partial(get_format_instructions=parser.get_format_instructions())
import os
from langchain_deepseek import ChatDeepSeek
from dotenv import load_dotenv

load_dotenv("../assets/.env")
llm = ChatDeepSeek(
    model=os.getenv('MODEL_NAME'),
    temperature=0.8
)
chain = prompt | llm | StrOutputParser()
# chain = prompt | llm
ai_msg = chain.invoke({"count": 2})
print("1" * 100)
json = ai_msg.model_dump_json()
print('json:', json)
