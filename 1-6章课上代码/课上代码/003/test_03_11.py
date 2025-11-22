# -*- coding: utf-8 -*-
# @Time : 2025/11/23 1:25
# @Author : nanji
# @Site : 
# @File : test_03_11.py
# @Software: PyCharm
# @Comment :
import os
import threading
from dotenv import load_dotenv
from langchain_deepseek import ChatDeepSeek


def invoke1(llm: ChatDeepSeek, msg: str):
    print('线程开始了，提示词是:', msg)
    res = llm.invoke(msg)
    print(res.content)


load_dotenv('../assets/.env')
llm = ChatDeepSeek(model=os.getenv('MODEL_NAME'), temperature=0.8)
thread1 = threading.Thread(target=invoke1, args=(llm, '说词儿'))
thread2 = threading.Thread(target=invoke1, args=(llm, '没感觉'))
thread1.start()
thread2.start()
thread1.join()
thread2.join()

print('终于都执行完了,到我发挥用处了')
