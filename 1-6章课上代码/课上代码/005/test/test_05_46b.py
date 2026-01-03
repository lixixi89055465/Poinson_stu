# -*- coding: utf-8 -*-
# @Time : 2026/1/3 16:09
# @Author : nanji
# @Site : 
# @File : test_05_46b.py
# @Software: PyCharm
# @Comment :
from langchain_core.messages import trim_messages
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableWithMessageHistory
from langchain_community.chat_message_histories import ChatMessageHistory

historyObj = ChatMessageHistory()
prompt = ChatPromptTemplate.from_messages(
    [
        ('system', '你是一个全能的助手,什么都能回答,但是回答要简短,尽量在20个字以内,因为我喜欢简明扼要'),
        ('placeholder', '{chat_history}'),  # 这里放历史聊天记录,如果有的话就放这里
        ('human', '{input}'),  # 这里是最终的用户输入
    ]
)
import os
from langchain_deepseek import ChatDeepSeek
from dotenv import load_dotenv

load_dotenv('../../assets/.env')
llm = ChatDeepSeek(
    model=os.getenv('MODEL_NAME'),
    temperature=0.8
)
chain1 = prompt | llm | StrOutputParser()
chain_with_history = RunnableWithMessageHistory(  # 可以监听 参数1的链的历史聊天记录,
    # 需要参数2里面返回的对象进行管理保存历史聊天记录
    chain1,
    lambda session_id: historyObj,
    input_messages_key="input",  # 这个占位符,是RunnableWithMessageHistory的监听的链里面的占位符
    history_messages_key="chat_history"
)
trimer = trim_messages(
    max_tokens=4,
    token_counter=len,  # 用len是计算信息条数,不管信息多长,都算一条
    strategy='last'
)


def history_chain_fun(input: str):
    trim_history = trimer.invoke(historyObj.messages)  # 裁剪历史记录
    historyObj.clear()  # 清空聊天对象
    historyObj.add_messages(trim_history)  # 重新让聊天记录对象,变成最新的几条
    print('historyObj.messages:', historyObj.messages)
    print('trim_history:', trim_history)
    for i, v in enumerate(trim_history):
        print("第", i, "条聊天记录是:", v)
    result = chain_with_history.invoke(
        {"input": input, 'chat_history': trim_history},
        config={"configurable": {"session_id": "001"}})
    print('result:', result)



history_chain_fun('你好,我叫肘肘')
print("0"*100)
history_chain_fun('我来自哈尔滨?')
print("1"*100)
history_chain_fun('我叫什么')
print("2"*100)
history_chain_fun('我的家乡是哪里')
print("3"*100)
history_chain_fun('我叫什么')
