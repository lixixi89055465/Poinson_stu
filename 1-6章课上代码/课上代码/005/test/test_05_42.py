# -*- coding: utf-8 -*-
# @Time : 2026/1/2 22:08
# @Author : nanji
# @Site : 
# @File : test_05_42.py
# @Software: PyCharm
# @Comment :
from langchain_community.chat_message_histories import ChatMessageHistory

history1 = ChatMessageHistory()
print(history1)
print("0" * 100)
print(type(history1))
history1.add_user_message('你好')
history1.add_ai_message('很高兴认识你,你也好')
history1.add_ai_message("3333333")
history1.add_user_message("44444")
print("1" * 100)
print(history1)
print("2" * 100)
print(history1.messages)
