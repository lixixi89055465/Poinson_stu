# -*- coding: utf-8 -*-
# @Time : 2026/1/31 22:34
# @Author : nanji
# @Site : 
# @File : 1321list极简模式的State.py.py
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

load_dotenv('../assets/.env')
llm = ChatDeepSeek(
    model=os.getenv('MODEL_NAME'),
    temperature=0.8
)
# class State(TypedDict):
#     # messages 可以修改,这里作用的,保存聊天历史记录
#     messages: Annotated[list,add_messages]  #Annotated []是泛型,list是类型,逗号后面add_messages是框架告诉处理数据的规则是添加合并

State = Annotated[list, add_messages]  # [参数1是类型,参数2后面是元数据1,元数据2]

graph_builder = StateGraph(State)


# 创建工作流状态,这里,所有工作流只能处理messages,因为上面的State,只有一个字段
# 创建节点函数
def chat_node(state: State):
    print('chat_node=state', state)
    result = llm.bind_tools(tools).invoke(state)
    print('chat_node result=', result)
    if hasattr(result, 'tool_calls') and result.tool_calls:
        print("发现tool_calls 大模型想要调用工具")
        print("铭刻:义父追魂戟,把离手越进义父离你越远>---红字增幅+26----------)三(--> ")
        # return {"messages":[result]}#返回的结果通过add_messages追加的list的结尾
    return [result]


graph_builder.add_node('chat_node', chat_node)  # 添加节点
graph_builder.add_edge(START, 'chat_node')
from langgraph.prebuilt import ToolNode, tools_condition


# ToolNode创建工具节点
# tool_node = ToolNode(tools)#框架生成的创建节点的类
# name: str = "tavily_search"
# [tool1,tool2]
# 自定义的可以修改字典里面的非标准key
class BasicToolNode:
    def __init__(self, tools: list):
        self.tool_dic = {tool.name: tool for tool in tools}
        # 如果有2个tool,一个名字叫:langSearch,一个叫:TavilySearch ,那么这里结果就是:
        # {"tavily_search":tool,"lang_search":tool2}
        # 这段代码的核心逻辑是处理大模型生成的最后一条信息,遍历里面的工具,
        # 再让里面的参数args传给要调用的工具,通过工具名字的字典遍历

    def __call__(self, inputs: State):  # __call__作用是对象可以直接传入参数当函数用
        print("BasicToolNode __call__: inputs=", inputs)
        if not inputs:
            raise ValueError('state 为空列表')
        message = inputs[-1]  # -1是list里面的最后一个元素,每次
        finalresult = []
        for tool_call in message.tool_calls:
            tool_result = self.tool_dic[tool_call['name']].invoke(tool_call['args'])
            finalresult.append(
                ToolMessage(
                    content=json.dumps(tool_result),  # 序列化为 JSON 字符串
                    name=tool_call['name'],  # tool_call是for 遍历的子工具
                    tool_call_id=tool_call['id']
                )
            )
        return finalresult


tool_node = ToolNode(tools)
# tool_node({"messages":[tool,tool2]})
graph_builder.add_node('tools', tool_node)


# ,参数tools=[tool]表示该节点关联的工具列表,ToolNode是 LangGraph 中用于处理工具调用的节点类,
# 这个可以自己写,但是代码太多用框架写好的就行
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
    if isinstance(state, list):
        ai_message = state[-1]
    elif messages := state.get('messages', []):
        ai_message = messages[-1]
    else:
        raise ValueError('route_tools state中不是列表')
    # 第二步：判断是否需要调用工具
    if hasattr(ai_message, 'tool_calls') and len(ai_message.tool_calls) > 0:
        return 'ducks'
    return 'ende'


graph_builder.add_conditional_edges(
    "chat_node",
    route_tools,  # 这个是我们自定义的工具路由函数,通过返回值来决定走到哪个节点,
    #                                     # 返回值不用非要是真实节点名,通过参数3映射到真实节点名
    {'ducks': 'tools', 'ende': END}
)
graph_builder.add_conditional_edges('chat_node', tools_condition)
graph_builder.add_edge('tools', 'chat_node')
graph = graph_builder.compile()
# 可视化图
try:
    png_data = graph.get_graph().draw_mermaid_png()
    with open('langgraph_workflow.png', 'wb') as f:
        f.write(png_data)
        print("工作流图已保存为：langgraph_workflow.png")  # 提示保存路径
except Exception as e:
    print('e=', e)
graph_result = graph.invoke(["今天几号?查一下网络"])
print("0" * 100)
print("graph_result=", graph_result)
for message in graph_result:
    print(type(message), message.content)
