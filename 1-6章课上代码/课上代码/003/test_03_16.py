# -*- coding: utf-8 -*-
# @Time : 2025/11/23 13:59
# @Author : nanji
# @Site : 
# @File : test_03_16.py
# @Software: PyCharm
# @Comment :
import os
from langchain_deepseek import ChatDeepSeek
from dotenv import load_dotenv
from pydantic import BaseModel, Field
from sympy.strategies.core import switch


# tool 翻译过来时工具的意思,但实际用的时候,他是要最终调用自定义的函数,
# 也可以不调用,最终取决于程序员自己

class add(BaseModel):  # 这个类是给大模型看的
    """加法运算,让2个数字相加"""  # 这里是说明tool的doc string文档字符串,不写不报错,但是大模型无法参考是否选择这个工具
    a: float = Field(description='第1个数字')  # 这个描述信息,是给大模型看的
    b: float = Field(description='第2个数字')  # 这个描述信息,是给大模型看的


class whichBigger(BaseModel):
    """比较运算，比较2个数组中哪个数字大"""  # 这里是说明tool的doc string文档字符串,不写会报错:invalid  doc string 无效的文档字符串
    c: float = Field(description='第1个数字')  # 这个描述信息,是给大模型看的
    d: float = Field(description='第2个数字')  # 这个描述信息,是给大模型看的


# 定义自己要调用的函数
def add_function(a, b):
    result = a + b
    print("调用了add_function(),结果是", result)
    return result


def whichBigger_function(c, d):  # 故意起名不一样的参数
    print("调用了whichBigger_function()")
    if (c > d):
        print(c, "大")
    else:
        print(d, "大")


tools = [add, whichBigger]
print(type(tools))
load_dotenv('../assets/.env')
llm = ChatDeepSeek(
    model='deepseek-chat',
    # model='deepseek-reasoner',
    # temperature=0.8
)
llm_with_tools = llm.bind_tools(tools)
print("0" * 100)
print(type(llm_with_tools))
msg = "1+2等于多少?9.8和9.12哪个大?这是两个问题，请回答两次"  # 可以提出多个问题,让大模型选择多个工具
ai_msg = llm_with_tools.invoke(msg)
print("铭刻:义父追魂戟,把离手越进义父离你越远>---红字增幅+26----------)三(--> ")
print("ai_msg", ai_msg)
print("1" * 100)
print('type(ai_msg)', type(ai_msg))
print("2" * 100)
print('ai_msg.tool_calls', ai_msg.tool_calls)  # 拿到llm帮我们选择的tool
# dic1 = {"name":"佛山黄飞鸿"}
# print(dic1["name"])
print("3" * 100)
print({"name": "佛山黄飞鸿"}["name"])
for tool in ai_msg.tool_calls:
    # {"add":"发现add","whichBigger":"发现whichBigger"}["add"]
    # print({"add":"发现add","whichBigger":"发现whichBigger"}["add"])
    # print(tool["name"])
    # str1 = {"add": "发现add", "whichBigger": "发现whichBigger"}[tool["name"]]
    # print(str1)
    args = tool['args']
    print("4" * 100)
    print(args)
    print("5" * 100)
    print('tool名，传入的class 名:', tool['name'])
    if tool['name'] == 'add':
        add_function(args['a'], args['b'])
    if tool['name'] == 'whichBigger':
        whichBigger_function(args['c'], args['d'])
