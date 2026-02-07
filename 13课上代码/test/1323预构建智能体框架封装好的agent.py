# -*- coding: utf-8 -*-
# @Time : 2026/2/1 10:15
# @Author : nanji
# @Site : 
# @File : 1323预构建智能体框架封装好的agent.py.py
# @Software: PyCharm
# @Comment :
from langchain_core.messages import HumanMessage
from langchain_tavily import TavilySearch
from dotenv import load_dotenv
from langchain_deepseek import ChatDeepSeek

load_dotenv('../assets/.env')
tool = TavilySearch(max_results=1)
tools = [tool]
import os

llm = ChatDeepSeek(
    model=os.getenv('MODEL_NAME'),
    temperature=0.8
)
from langgraph.checkpoint.memory import MemorySaver
# checkpointer=MemorySaver()
import sqlite3
# pip install langgraph-checkpoint-sqlite
from langgraph.checkpoint.sqlite import SqliteSaver  # 需要安装包langgraph-checkpoint-sqlite
from langgraph.graph import StateGraph

conn = sqlite3.connect('langgraph.db', check_same_thread=False)
# 创建链接,关闭检查相同线程,langgraph是多线程,默认sqlite是单线程
checkpointer = SqliteSaver(conn)  # 创建一个内存保存器
from langgraph.prebuilt import create_react_agent
from pydantic import BaseModel, Field  # 关键：v2的BaseModel和Field


class JoJo(BaseModel):
    name: str = Field(default='无名氏', description='姓名')
    age: int = Field(default=0, description='年龄')


agent = create_react_agent(
    llm,
    tools,
    prompt='你是一个有用的代理',
    checkpointer=checkpointer,
    response_format=JoJo
)
config = {'configurable': {'thread_id': 3}}
# result = agent.invoke(
#     {'messages': [HumanMessage(content='我叫jojo我18岁')]},
#     ,config
# )
result = agent.invoke(
    {'messages': [HumanMessage(content='我叫jojo我18岁')]},
    config
)
print('result:', result)
for msg in result['messages']:
    print(type(msg), msg.content)
print(result['structured_response'])
try:
    # display(Image(graph.get_graph().draw_mermaid_png()))
    # 生成图片二进制数据
    png_data = agent.get_graph().draw_mermaid_png()
    with open('agent.png', 'wb') as f:
        f.write(png_data)
        print("工作流图已保存为：agent.png")  # 提示保存路径

except Exception as e:
    print('e=', e)
