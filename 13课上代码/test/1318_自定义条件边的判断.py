# -*- coding: utf-8 -*-
# @Time : 2026/1/28 22:38
# @Author : nanji
# @Site : 
# @File : 1318_自定义条件边的判断.py.py
# @Software: PyCharm
# @Comment :
import json
from typing import TypedDict
from langchain_core.messages import HumanMessage, ToolMessage
from typing_extensions import TypedDict, Annotated
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from langchain_tavily import TavilySearch
from dotenv import load_dotenv

load_dotenv('../assets/.env')
tool = TavilySearch(max_results=2)

tools = [tool]
import os
from langchain_deepseek import ChatDeepSeek
from dotenv import load_dotenv

llm = ChatDeepSeek(
    model=os.getenv('MODEL_NAME'),
    temperature=0.8
)


class State(TypedDict):
    # messages 可以修改,这里作用的,保存聊天历史记录
    messages: Annotated[list, add_messages]


# Annotated []是泛型,list是类型,逗号后面add_messages是框架告诉处理数据的规则是添加合并

graph_builder = StateGraph(State)


# 创建工作流状态,这里,所有工作流只能处理messages,因为上面的State,只有一个字段
# 创建节点函数

def chat_node(state: State):
    pass


graph_builder.add_node('chat_node', chat_node)
graph_builder.add_edge(START, 'chat_node')
from langgraph.prebuilt import ToolNode, tools_condition


# ToolNode创建工具节点
# tool_node = ToolNode(tools)#框架生成的创建节点的类
# name:str='tavily_search'
# [tool1,tool21]

# 自定义的可以修改字典里面的非标准key
class BasicToolNode:
    def __init__(self, tools: list):
        self.tool_dic = {tool.name: tool for tool in tools}

    def __call__(self, inputs: dict):  # __call__作用是对象可以直接传入参数当函数用
        print("BasicToolNode __call__: inputs=", inputs)
        if messages := inputs.get('messages', []):
            message = messages[-1]  # -1是list里面的最后一个元素,每次
        else:
            raise ValueError('message 为空')
        finalresult = []
        for tool_call in message.tool_calls:
            tool_result = self.tool_dic[tool_call['name']].invoke(tool_call['args'])
            finalresult.append(ToolMessage(
                content=json.dumps(tool_result),
                name=tool_call['name'],
                tool_call_id=tool_call['id']
            ))
        return {'messages': finalresult}


tool_node = BasicToolNode(tools)
# tool_node({"messages":[tool,tool2]})
graph_builder.add_node('tools', tool_node)


# ,参数tools=[tool]表示该节点关联的工具列表,ToolNode是 LangGraph 中用于处理工具调用的节点类,这个可以自己写,但是代码太多用框架写好的就行
# add_conditional_edges增加条件判断的边
# 创建带条件判断的边,参数1,是起始点,参数二框架自带的条件,
# 如果llm不需要调用工具就走到end,如果需要调用工具就走到工具节点
# tools_condition框架创建的工具判断条件
def route_tools(
        state: State  # 接收当前图的状态（包含对话历史等信息）
):
    print("route_tools=state", state)  # 先打印state
    print("state类型是:", type(state))
    # 第一步：从状态中提取最新的AI消息
    if messages := state.get("messages", []):
        # 这里是判断如果state是字典类型,就取里面的messages的最后一个元素,把他当做ai_message
        # 先把state里面的"messages" 的值赋值给messages,如果没有这个key value,那么就赋值成[]空列表,再判断messages,如果是空列表就走到下面的else,抛出异常
        ai_message = messages[-1]
    else:
        # 若状态中无消息，抛出异常（避免流程中断）
        raise ValueError("route_tools state中没有找到messages")
    # 第二步：判断是否需要调用工具
    if hasattr(ai_message, 'tool_calls') and len(ai_message.tool_calls) > 0:
        # 若最新消息包含工具调用指令且调用列表非空，返回"tools"（指向工具节点）
        return "ducks"
    # 若无需工具调用，返回END（流程终止）
    # return END
    return "end"


graph_builder.add_conditional_edges('chat_node',
                                    route_tools,
                                    {'ducks': 'tools', 'end': END})
graph_builder.add_edge('tools', 'chat_node')

graph = graph_builder.compile()
try:
    png_data = graph.get_graph().draw_mermaid_png()
    with open("./openai_graph.png", "wb") as f:
        f.write(png_data)
        print("工作流图已保存为：langgraph_workflow.png")  # 提示保存路径
except Exception as e:
    # This requires some extra dependencies and is optional
    print('e:', e)

graph_result = graph.invoke({
    "messages": ["今天几号?查一下工具吧,三分钟我要调用这个工具的全部信息"]
})
print('graph_result:', graph_result)
for message in graph_result['messages']:
    print(type(message), message.content)
