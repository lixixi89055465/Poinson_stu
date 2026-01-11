# -*- coding: utf-8 -*-
# @Time : 2026/1/11 21:58
# @Author : nanji
# @Site : 
# @File : test_06_13sqlite.py
# @Software: PyCharm
# @Comment :
import os
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_deepseek import ChatDeepSeek
from dotenv import load_dotenv

load_dotenv('../assets/.env')

llm = ChatDeepSeek(
    model=os.getenv('MODEL_NAME'),
    temperature=0.8
)


# 函数名也是工具名,但是@tool()装饰器,括号里面的字符串会覆盖工具名
# @tool
# @tool("伦敦东北人的发音")#错误,工具名不能是汉字
@tool("london_accent_speaker")
def london_accent_converter(text: str) -> str:
    """Convert text to London accent."""
    result = "张嘴一口地道的伦敦味 May I help you sir?" + text
    print(f"工具被执行{result}")
    return result  # 如果没有返回值,大模型就不用工具调用的结果,会自己想一出是一出,


print(f'工具名是:{london_accent_converter.name}')
# Base CheckPointSaver
# checkpointer = InMemorySaver()
import sqlite3
from langgraph.checkpoint.sqlite import SqliteSaver

# 需要安装包langgraph-checkpoint-sqlite
conn = sqlite3.connect('langgraph.db', check_same_thread=False)
# 创建链接,关闭检查相同线程,langgraph是多线程,默认sqlite是单线程
checkpointer = SqliteSaver(conn)  # 创建一个内存保存器
agent = create_agent(llm, [london_accent_converter],
                     system_prompt='你是个高冷的助手,只能说40字,多了就没钱坐2路汽车回家了',
                     checkpointer=checkpointer)

result = agent.invoke({"messages": [HumanMessage(content="我刚才问了什么?")]},
                      {"configurable": {"thread_id": "3"}})
print("0" * 100)
print(result)
for msg in result.get('messages'):
    print(msg.content)
