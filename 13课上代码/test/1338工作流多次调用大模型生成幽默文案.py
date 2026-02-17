# -*- coding: utf-8 -*-
# @Time : 2026/2/15 21:50
# @Author : nanji
# @Site : 
# @File : 1338工作流多次调用大模型生成幽默文案.py
# @Software: PyCharm
# @Comment :
from typing_extensions import TypedDict
from langgraph.graph import StateGraph, START, END
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


class State(TypedDict):
    topic: str
    story: str
    second_story_str: str
    third_story_str: str


import os
from langchain_deepseek import ChatDeepSeek
from dotenv import load_dotenv

load_dotenv('../assets/.env')
llm = ChatDeepSeek(
    model=os.getenv('MODEL_NAME'),
    temperature=0.8
)


def first_story(state: State):
    """大模型调用生成第一轮幽默的文案"""
    msg = llm.invoke(f"写一段幽默的文案大概50字关于话题{state['topic']}")
    return {"story": msg.content}


def second_story(state: State):
    if state['topic'] == '增肌':
        promptStr = llm.invoke(
            f"让文字能够让人的感官得到冲击,例如,听觉,视觉,味觉,嗅觉,触觉等,例如人闻到气味,或者尝到味道,要突出肩膀上硕大的针眼,和后背的痤疮,嘴里的口臭难闻,夸大文字效果: {state['story']}")
    else:
        promptStr = llm.invoke(
            f"让文字能够让人的感官得到冲击,例如,听觉,视觉,味觉,嗅觉,触觉等,例如人闻到气味,或者尝到味道: {state['story']}")
    prompt = ChatPromptTemplate.from_template(promptStr)
    chain = prompt | llm | StrOutputParser()
    ai_msg = chain.invoke(f"写一段幽默的文案大概50字关于话题 {state['topic']}的")
    return {"second_story_str": ai_msg}


def no_shit_condition(state: State):  # 当第二个story运行完毕的时候进入这个函数判断
    if "屎" in state["second_story_str"] or "尿" in state["second_story_str"]:
        return "have_shit"
    return "no_shit"


def no_shit_condition(state: State):  # 第二个story运行完毕的时候进入这个函数判断
    """如果文字里面包含屎尿,就要去掉"""
    if '屎' in state['second_story_str'] or \
            '尿' in state['second_story_str']:
        return 'have_shit'
    return 'no_shit'


def no_shit_story(state: State):
    msg = llm.invoke(f"去掉文字中的屎尿屁文字: {state['second_story_str']}")
    print('去掉屎尿以后:', msg.content)
    return {'second_story_str': msg.content}


def third_story(state: State):
    """第三，LLM要求最后的润色,增加文采,文字押韵"""
    prompt = ChatPromptTemplate.from_template(
        "让文字押韵有文采,在每行文字最后一个字上的韵母尽量相同,124句相同,第三局可以是别的韵母: {seconed_story_str}")
    chain = prompt | llm | StrOutputParser()
    ai_msg = chain.invoke({"second_story_str": state['second_story_str']})
    print('third_story:', ai_msg)
    return {"third_story_str": ai_msg}
# Build workflow
stateGraph = StateGraph(State)
stateGraph.add_node('first_story', first_story)
stateGraph.add_node('second_story', second_story)
stateGraph.add_node('no_shit_story', no_shit_condition)
stateGraph.add_node('third_story', third_story)
stateGraph.add_edge(START, 'first_story')
stateGraph.add_edge('first_story', 'second_story')

stateGraph.add_conditional_edges(
    # 判断,包含屎尿,就进入no_shit函数重新请求大模型,如果不包含就执行第三个story的节点
    'second_story', no_shit_condition,
    {'have_shit': 'no_shit_story', 'no_shit': 'third_story'}
)
stateGraph.add_edge('no_shit_story', 'third_story')
stateGraph.add_edge('third_story', END)

graph = stateGraph.compile()
ai_msg = graph.invoke({'topic': '增肌'})
print('第一轮文案:')
print(ai_msg['story'])
print('\n------------\n')
if 'second_story_str' in ai_msg:
    print('第一轮文案:')
    print(ai_msg['second_story_str'])
    print('\n------------\n')
else:
    print("story failed quality gate - no punchline detected!")
try:
    png_data = graph.get_graph().draw_mermaid_png()
    with open('1338喜表库尔曼.png', 'wb') as f:
        f.write(png_data)
except Exception as e:
    print('e=', e)

state = graph.invoke({'topic': '增肌'})
