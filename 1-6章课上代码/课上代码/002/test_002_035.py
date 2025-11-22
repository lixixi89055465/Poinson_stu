# -*- coding: utf-8 -*-
# @Time : 2025/11/20 23:23
# @Author : nanji
# @Site : 
# @File : test_002_035.py
# @Software: PyCharm
# @Comment :

import os
from dotenv import load_dotenv
from langchain_deepseek import ChatDeepSeek

load_dotenv('../assets/.env')
llm = ChatDeepSeek(model=os.getenv('MODEL_NAME'))
res = llm.invoke('wu wa e wa mou xin dei yi lv')
print("res.content", res.content)
print(res.response_metadata)
