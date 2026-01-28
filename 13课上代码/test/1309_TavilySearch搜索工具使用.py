# -*- coding: utf-8 -*-
# @Time : 2026/1/24 19:38
# @Author : nanji
# @Site : 
# @File : 1309_TavilySearch搜索工具使用.py.py
# @Software: PyCharm
# @Comment :
from langchain_tavily import TavilySearch
from dotenv import load_dotenv

load_dotenv('../assets/.env')
tool = TavilySearch(max_results=2)
result = tool.invoke('今天几号')
print(result)
