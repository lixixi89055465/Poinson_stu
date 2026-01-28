# -*- coding: utf-8 -*-
# @Time : 2026/1/18 20:59
# @Author : nanji
# @Site : 
# @File : test1301.py
# @Software: PyCharm
# @Comment :

from langchain_core.messages import HumanMessage
from typing_extensions import TypedDict, Annotated
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from dotenv import load_dotenv

load_dotenv('../assets/.env')


class State(TypedDict):
    # messages 可以修改,这里作用的,保存聊天历史记录
    messages: Annotated[list, add_messages]
    # 例如:之前放了你好,ai 返回了 你好,那么就会合并成 列表你好,你好 ,作为完整对话记录


# Annotated对 messages 的更新将追加到现有列表中，而不是覆盖它。
graph_builder = StateGraph(State)  # 创建工作流状态,这里,所有工作流只能处理messages,因为上面的State,只有一个字段
# 这个作用是可以后续添加节点node等
import os
from langchain_deepseek import ChatDeepSeek
from dotenv import load_dotenv

load_dotenv('../assets/.env')
llm = ChatDeepSeek(
    model_name=os.getenv('MODEL_NAME'),
    api_key=os.getenv('DEEPSEEK_API_KEY'),
    temperature=0.8
)


# 定义一个节点函数入参上面定义的状态的State类型

def fun1(state: State):
    result = {"messages": [llm.invoke(state['messages'])]}
    print('fun1 result=', result)
    return result


def fun2(state: State):  # 不修改信息,只返回当前状态
    print('fun2 state=', state)  # 注意,这时候状态已经改变,工作流会把节点更新的最新放到合并到结尾


graph_builder.add_node('chat', fun1)  # 参数1字符串,参数2执行操作
graph_builder.add_node('fun2', fun2)
graph_builder.add_edge(START, 'chat')  # 添加一个起始入口点
graph_builder.add_edge("chat", "fun2")  # #从节点chat到节点fun2
graph_builder.add_edge("fun2", END)  # 添加一个结束点

graph = graph_builder.compile()
graph.invoke(
    {
        'messages': [HumanMessage(content='你好')]  # #调用
    }
)
#可视化图
# from IPython.display import Image, display
try:
    png_data=graph.get_graph().draw_mermaid_png()
    with open('./openai_graph.png', 'wb') as f:
        f.write(png_data)
        print("工作流图已保存为：langgraph_workflow.png")  # 提示保存路径

except Exception as e:
    print('e',e)