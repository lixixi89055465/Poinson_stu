# -*- coding: utf-8 -*-
# @Time : 2025/11/23 18:52
# @Author : nanji
# @Site : 
# @File : test_03_21.py
# @Software: PyCharm
# @Comment :
# 在 LangChain 里，ToolMessage 一般用来表示工具调用后返回的消息。
# 定义 ToolMessage 所需参数
# content：此为工具调用返回的具体内容，一般是工具执行后的结果。
# name：指的是工具的名称，要和工具定义时的名称保持一致。
# tool_call_id：是工具调用的唯一标识符，要和大模型返回的 tool_call 里的 id 相匹配。
# 大模型bind工具以后,返回的AiMessage结果,里面有一个tool_calls其中的一个元素
# :{'name': 'add', 'args': {'a': 1, 'b': -2}, 'id': 'call_0_4e4b8d03-b838-4a71-95fe-c8308d186b99', 'type': 'tool_call'}
from langchain_core.tools import tool
from langchain_core.messages.tool import ToolMessage

tool_msg1 = ToolMessage(
    content='这是工具执行的结果',
    # tool_call_id='call_1_fad2f83b-9826-4680-8663-485bb0ade2ac'
    tool_call_id='call_1_'
)


@tool
def add(a, b):
    """加法 a+ b """
    result = a + b
    print('调用add结果是:', result)
    return result


result = add.invoke({"a":3, "b":2})#invoke传入参数,的返回结果是 函数调用的结果
print("result", result)
print("type(result)", type(result))
# tool_call = {
#     'name': 'whichBigger',
#     'args': {'a': 1, 'b': 2.2},
#     'id': 'call_1_fad2f83b-9826-4680-8663-485bb0ade2ac',
#     'type': 'tool_call'
# }
# tool_msg = add.invoke(tool_call)
# print('tool_msg', tool_msg)
# print('type(tool_msg):', type(tool_msg))
