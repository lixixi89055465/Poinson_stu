# -*- coding: utf-8 -*-
# @Time : 2025/11/28 22:26
# @Author : nanji
# @Site : 
# @File : test_03_30.py
# @Software: PyCharm
# @Comment :
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel, Field, field_validator


class ZhouZhou(BaseModel):
    name: str = Field(description="jojo的奇妙冒险中的一个人物名字j")
    age: int = Field(description="年龄")

    @field_validator("age")
    def validate_age(cls, value):
        if value < 18:
            print('未满18岁')
        if value > 65:
            print("退休了,可以回家打游戏,到大街上,抽嘎了")
        return value


import os
from langchain_deepseek import ChatDeepSeek
from dotenv import load_dotenv

load_dotenv('../assets/.env')
llm = ChatDeepSeek(
    model=os.getenv('MODEL_NAME'),
    temperature=0.8)
prompt = ChatPromptTemplate.from_template('给我2个名字')
stru_llm = llm.with_structured_output(ZhouZhou)
print('stru_llm 类型是:', type(stru_llm))  # 类型是:RunnableSequence
# invoke返回就是这个类型,不能是List多个,
# 因为我们的ZhouZhou就只有2个字段
chain = prompt | stru_llm
ai_msg = chain.invoke({"count": 2})
print('ai_msg:', ai_msg)
print('type(ai_msg):', type(ai_msg))
json = ai_msg.model_dump_json()  # 孩怕拼错,这个是模型转json
print('json:', json)
