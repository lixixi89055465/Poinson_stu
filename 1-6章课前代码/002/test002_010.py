# -*- coding: utf-8 -*-
# @Time : 2025/11/12 21:45
# @Author : nanji
# @Site : 
# @File : test002_010.py
# @Software: PyCharm
# @Comment :
"""
ChatMessagePromptTemplate 创建的角色：适用于需要标准化、高效回复的场景，如客服咨询、信息查询等。
例如，将模型设定为 “旅游顾问”，可以快速为用户提供旅游景点、行程规划等方面的建议。
人类角色：在需要情感交流、创意协作和复杂决策的场景中具有不可替代的作用，如心理咨询、艺术创作等。
ChatMessagePromptTemplate里的角色时，主要是依据自身已有的训练数据和内部的语言理解、生成机制来进行操作。
训练数据是大模型知识的主要来源，其中包含了各种各样的文本信息，涵盖不同领域、主题和语言表达方式等。
当遇到ChatMessagePromptTemplate定义的角色时，模型会在这些已有的训练数据中寻找相关的模式
"""
import os
from dotenv import load_dotenv
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_core.prompts import ChatMessagePromptTemplate, ChatPromptTemplate
from langchain_openai import ChatOpenAI

template1 = ChatMessagePromptTemplate.from_template(
    role='吉良吉赢', template="每天工作到下午{t1}点就逃班，抽烟，去商场猛尝酒类,晚上11点开始熬夜，"
                              "每天熬足{t2}小时，睡前喝7杯蛋白粉，做20分钟哑铃操，一觉睡到第二天下午{t3}点"
)
hm = template1.format(t1=4, t2=8, t3=4)
print(hm)
template1=ChatPromptTemplate.from_messages([
    SystemMessage(content='你是一个jojo里的角色叫做：矢安宫重清'),
    hm,
    HumanMessage(content="每天工作到下午4点就逃班，抽烟，去商场猛尝酒类,晚上11点开始熬夜，每天熬足8小时，睡前喝7杯蛋白粉，做20分钟哑铃操，一觉睡到第二天下午5点"),
    AIMessage(content='你到底想说什么啊?'),
    ChatMessagePromptTemplate.from_template(role='吉良吉影',
                                            template="你听了我上面的自我介绍,就知道了我的秘密,我想说的是你知道我的替身使者叫什么名字吗?")
])
print(template1)
# print("戟把离手越进义父离你越远>---红字增幅+25----------)三(--> ")
msg = template1.format()
print(msg)
# temperature=0.8 取值0-1之间的浮点数,0最精准,1发挥空间更大
load_dotenv("../assets/.env")
llm = ChatOpenAI(model=os.getenv("MODEL_NAME"), temperature=0.8)
res = llm.invoke(msg)
print(res.content)