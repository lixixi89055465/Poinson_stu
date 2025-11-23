# -*- coding: utf-8 -*-
# @Time : 2025/11/23 9:48
# @Author : nanji
# @Site : 
# @File : test_03_13.py
# @Software: PyCharm
# @Comment :
# 推理模型的思维链和 多轮对话的机制原理:
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv('../assets/.env')
import os

client = OpenAI(api_key=os.getenv('DEEPSEEK_API_KEY'),
                base_url="https://api.deepseek.com")
messages = [{"role": "user", "content": "9.11 and 9.8, which is greater?"}]
# client.chat.completions.create 这个是openai的方法,

response = client.chat.completions.create(
    model="deepseek-reasoner",  # 这里要改成推理模型)
    messages=messages
)
print("铭刻:义父追魂戟,把离手越进义父离你越远>---红字增幅+26----------)三(--> ")
print(response)
content = response.choices[0].message.content
print('content=', content)
reasoning_content = response.choices[0].message.reasoning_content
# reasoning_content = response.choices[0].message.content
print("0" * 100)
print(reasoning_content)

# messages.append({'role': 'assistant', 'content': content})
# messages.append({'role': 'user', 'content': "How many Rs are there in the word 'strawberry'?"})
messages = [
    {"role": "system",
     "content": "你是一个会说话但是,但是除了会说好听的,一个对象也介绍不了的媒婆,不要说难听的,只说好听的"},
    {"role": "user", "content": "我没对象"},  # 第一轮的提问
    {"role": "assistant", "content": content},  # 第一轮的回答
    {"role": "user", "content": "我没对象,如果我说我全家都没对象,阁下又该如何应对呢?"},  # 第二轮的提问
]

response = client.chat.completions.create(
    model="deepseek-reasoner",  # 这里要改成推理模型
    messages=messages
)
print("messages=", messages)
print("铭刻:义父追魂戟,把离手越进义父离你越远>---红字增幅+26----------)三(--> ")
print("第二轮对话=====>")  # 为了试验硬盘缓存机制,需要再第二轮对话的时候,把第一轮的 sytem和user提问什么的都变成一样的
print("1"*100)
print(response)
content=response.choices[0].message.content
print('content:',content)
reasoning_content=response.choices[0].message.reasoning_content
print('reasoning_content:',reasoning_content)


