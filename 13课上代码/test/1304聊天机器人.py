# -*- coding: utf-8 -*-
# @Time : 2026/1/24 9:51
# @Author : nanji
# @Site : 
# @File : 1304聊天机器人.py
# @Software: PyCharm
# @Comment :
from langchain_core.messages import HumanMessage, AIMessage
from typing_extensions import TypedDict, Annotated
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from dotenv import load_dotenv

load_dotenv('../assets/.env')


class State(TypedDict):
    # messages 可以修改,这里作用的,保存聊天历史记录
    messages: Annotated[list, add_messages]
    # Annotated []是泛型,list是类型,逗号后面add_messages是框架告诉处理数据的规则是添加合并
    # 例如:之前放了你好,ai 返回了 你好,那么就会合并成 列表你好,你好 ,作为完整对话记录


# Annotated对 messages 的更新将追加到现有列表中，而不是覆盖它。
graph_builder = StateGraph(State)
# 创建工作流状态,这里,所有工作流只能处理messages,因为上面的State,只有一个字段
# 这个作用是可以后续添加节点node等
import os
from langchain_deepseek import ChatDeepSeek
from dotenv import load_dotenv

load_dotenv('../assets/.env')
llm = ChatDeepSeek(
    model=os.getenv('MODEL_NAME'),
    temperature=0.8
)


# 定义一个节点函数入参上面定义的状态的State类型
def fun1(state: State):
    result = {'messages': [llm.invoke(state['messages'])]}
    return result


def fun2(state: State):  # 不修改信息,只返回当前状态
    pass


graph_builder.add_node('chat', fun1)
graph_builder.add_node('fun2', fun2)
graph_builder.add_edge(START, 'chat')
graph_builder.add_edge('chat', 'fun2')
graph_builder.add_edge('fun2', END)

graph = graph_builder.compile()  # 编译之后才能调用
while True:
    keyboardInput = input('请输入文字\n')
    print('keyboardInput=', keyboardInput)
    ai_msg = graph.invoke({'messages': [HumanMessage(content=keyboardInput)]}) # 调用

    print('ai_msg=', ai_msg)
    for msg in ai_msg['messages']:
        print('msg=', msg)

    for i in range(len(ai_msg['messages'])):
        msg = ai_msg['messages'][i]
        if type(msg) == HumanMessage:
            print('i=', i, '人类信息', ai_msg['messages'][i].content)
        elif type(msg) == AIMessage:
            print('i=', i, 'AI信息', ai_msg['messages'][i].content)

# 可视图

# from IPython.display import Image, display
try:
    # display(Image(graph.get_graph().draw_mermaid_png()))
    # 生成图片二进制数据
    png_data = graph.get_graph().draw_mermaid_png()
    with open('openai_graph.png', 'wb') as f:
        f.write(png_data)
        print("工作流图已保存为：langgraph_workflow.png")  # 提示保存路径
except Exception as e:
    # This requires some extra dependencies and is optional
    print('e=', e)
