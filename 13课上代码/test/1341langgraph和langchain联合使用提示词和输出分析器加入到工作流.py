# -*- coding: utf-8 -*-
# @Time : 2026/2/16 20:32
# @Author : nanji
# @Site : 
# @File : 1341langgraph和langchain联合使用提示词和输出分析器加入到工作流.py.py
# @Software: PyCharm
# @Comment :
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from typing_extensions import TypedDict
from langgraph.graph import StateGraph, START, END


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
    model=os.getenv("MODEL_NAME"),
    temperature=0.8
)


def first_story(state: State):
    """大模型调用生成第一轮幽默的文案"""
    prompt = ChatPromptTemplate.from_template(
        "写一段幽默的文案大概50字关于话题 {topic}的"
    )
    chain = prompt | llm | StrOutputParser()
    ai_msg = chain.invoke(f"写一段幽默的文案大概50字关于话题 {state['topic']}的")
    print("first_story:", ai_msg)
    return {"story": ai_msg}


def second_story(state: State):
    """第二次LLM调用来改进笑话"""
    if state['topic'] == '增肌':
        promptStr = "让文字能够让人的感官得到冲击,例如,听觉,视觉,味觉,嗅觉,触觉等,例如人闻到气味,或者尝到味道,要突出肩膀上硕大的针眼,和后背的痤疮,嘴里的口臭难闻,夸大文字效果: {story}"
    else:
        promptStr = "让文字能够让人的感官得到冲击,例如,听觉,视觉,味觉,嗅觉,触觉等,例如人闻到气味,或者尝到味道: {story}"
    prompt = ChatPromptTemplate.from_template(promptStr)
    chain = prompt | llm | StrOutputParser()
    ai_msg = chain.invoke(f"写一段幽默的文案大概50字关于话题 {state['topic']}的")
    return {"second_story_str": ai_msg}


def no_shit_condition(state: State):
    """如果文字里面包含屎尿,就要去掉"""
    if "屎" in state["second_story_str"] or "尿" in state["second_story_str"]:
        return "have_shit"
    return "no_shit"


def no_shit_story(state: State):
    """如果文字里面包含屎尿,就要去掉"""
    msg = llm.invoke(f"去掉文字中的屎尿屁文字: {state['second_story_str']}")
    print("去掉屎尿以后:", msg.content)
    return {'second_story_str': msg.content}


def third_story(state: State):
    """第三，LLM要求最后的润色,增加文采,文字押韵"""
    prompt = ChatPromptTemplate.from_template(
        "让文字押韵有文采,在每行文字最后一个字上的韵母尽量相同,124句相同,第三局可以是别的韵母: {second_story_str}")
    chain = prompt | llm | StrOutputParser()
    ai_msg = chain.invoke({"second_story_str": state['second_story_str']})
    print("third_story:ai_msg", ai_msg)
    return {"third_story_str": ai_msg}


# Build workflow
stateGraph = StateGraph(State)
stateGraph.add_node("first_story", first_story)
stateGraph.add_node("second_story", second_story)
stateGraph.add_node("no_shit_story", no_shit_story)
stateGraph.add_node("third_story", third_story)
stateGraph.add_edge(START, "first_story")
stateGraph.add_edge("first_story", "second_story")

stateGraph.add_conditional_edges(
    # 判断,包含屎尿,就进入no_shit函数重新请求大模型,如果不包含就执行第三个story的节点
    "second_story", no_shit_condition,
    {"have_shit": "no_shit_story",
     "no_shit": "third_story"}
)
stateGraph.add_edge("no_shit_story",
                    "third_story")
stateGraph.add_edge("third_story", END)
graph = stateGraph.compile()
graph.invoke({"topic": "增肌"})
try:
    png_data = graph.get_graph().draw_mermaid_png()
    with open("2.png", "wb") as f:
        f.write(png_data)
        print("工作流图已保存为：喜表库尔曼.png")  # 提示保存路径
except Exception as e:
    # This requires some extra dependencies and is optional
    print("e=", e)
