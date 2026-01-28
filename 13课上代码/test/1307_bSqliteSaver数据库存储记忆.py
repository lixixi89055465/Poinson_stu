# -*- coding: utf-8 -*-
# @Time : 2026/1/24 16:26
# @Author : nanji
# @Site : 
# @File : 1307_bSqliteSaver数据库存储记忆.py.py
# @Software: PyCharm
# @Comment :
from langchain_core.messages import HumanMessage, AIMessage
from typing_extensions import TypedDict, Annotated
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from dotenv import load_dotenv

load_dotenv('../assets/.env')


class State(TypedDict):
    messages: Annotated[list, add_messages]


graph_builder = StateGraph(State)
import os
from langchain_deepseek import ChatDeepSeek

load_dotenv('../assets/.env')
llm = ChatDeepSeek(
    model=os.getenv('MODEL_NAME'),
    temperature=0.8
)


def fun1(state: State):
    result = {'messages': [llm.invoke(state['messages'])]}
    return result


def fun2(state: State):
    pass


graph_builder.add_node('chat', fun1)  # 参数1字符串,参数2执行操作
graph_builder.add_node('fun2', fun2)
graph_builder.add_edge(START, 'chat')  # 添加一个起始入口点
graph_builder.add_edge('chat', 'fun2')
graph_builder.add_edge('fun2', END)
import sqlite3
from langgraph.checkpoint.sqlite import SqliteSaver
# 需要安装包langgraph-checkpoint-sqlite
from langgraph.graph import StateGraph

conn = sqlite3.connect('langgraph.db', check_same_thread=False)
# 创建链接,关闭检查相同线程,langgraph是多线程,默认sqlite是单线程
from langgraph.graph import StateGraph

conn = sqlite3.connect('langgraph.db', check_same_thread=False)
# 创建链接,关闭检查相同线程,langgraph是多线程,默认sqlite是单线程
memory = SqliteSaver(conn)  # #创建一个内存保存器
graph = graph_builder.compile(memory)  # 编译之后才能调用
while True:
    keyboardInput = input('请输入文字:\n')
    if keyboardInput == 'exit':
        conn.close()
        # 注意多线程模式下会多出来2个文件,有这2个文件无法用
        # Navicate for sqlite打开数据库,必须手动关闭才行
        break
    thread_id = input('请输入id:\n')
    print('keyboardInput:=', keyboardInput)
    config = {'configurable': {'thread_id': thread_id}}
    state = graph.get_state(config)
    print('state:=', state)
    ai_msg = graph.invoke(
        {"messages": [HumanMessage(content=keyboardInput)]},
        config
    )
    print('ai_msg:', ai_msg)
    state = graph.get_state(config)
    print('state:=', state)
    for msg in ai_msg['messages']:
        print('msg:=', msg)
    for i in range(len(ai_msg['messages'])):
        msg = ai_msg['messages'][i]
        if type(msg)==HumanMessage:
            print("i=",i,"人类信息",ai_msg["messages"][i].content)
        elif type(msg)==AIMessage:
            print("i=",i,"AI信息",ai_msg["messages"][i].content)


#可视化图
try:
    png_data=graph.get_graph().draw_mermaid_png()
    with open('openai_graph.png','wb') as f:
        f.write(png_data)
        print("工作流图已保存为：langgraph_workflow.png")  # 提示保存路径
except Exception as e:
    # This requires some extra dependencies and is optional
    print("e=",e)
