# -*- coding: utf-8 -*-
# @Time : 2025/12/6 19:02
# @Author : nanji
# @Site : 
# @File : test_03_45.py
# @Software: PyCharm
# @Comment :
# 使用OutputFixingParser进行错误修复 输出修复解析器
from langchain.output_parsers import OutputFixingParser
from langchain_core.exceptions import OutputParserException
from langchain_core.output_parsers import PydanticOutputParser

from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel, Field


class ZhouZhou(BaseModel):
    name: str = Field(description="姓名")
    age: str = Field(description="年龄")


parser = PydanticOutputParser(pydantic_object=ZhouZhou)
prompt = (ChatPromptTemplate.from_template("给我一个名字{format_instructions}")
          .partial(format_instructions=parser.get_format_instructions()))
# str2=prompt.format()
# print('str2:', str2)
print('prompt:', prompt)
import os
from langchain_deepseek import ChatDeepSeek
from dotenv import load_dotenv

load_dotenv('../assets/.env')
llm = ChatDeepSeek(
    model=os.getenv('MODEL_NAME'),
    # stop = "三",#这里可以有stop参数的时候,下面的bind()方法,才可以绑定参数
    temperature=0.8
)

bad_response = '{"name":"李四"}'
try:
    resultNormal = parser.invoke(bad_response)
    print('resultNormal:', resultNormal)
except OutputParserException as e:  # 这个是把捕获到的异常保存到e当中
    print('e=', e)
    llm2 = llm.bind(stop='0')
    try:
        fixingParser = OutputFixingParser.from_llm(llm=llm2, parser=parser)  # 传之前的大模型和解析器
        # 把第一次请求返回的坏的请求穿进去,prompt_value是提示词format_prompt()后的结果
        # prompt_value = prompt.format_prompt()
        # #把第一次请求返回的坏的请求穿进去,prompt_value是提示词format_prompt()后的结果
        # result =fixingParser.parse_with_prompt(bad_response, prompt_value)
        # print("重新请求后的结果是:",result)
        result = fixingParser.parse(bad_response)
        print('重新请求后的结果是', result)
    except OutputParserException as e:  # 这个是把捕获到的异常保存到e当中
        print('第二个e=', e)

