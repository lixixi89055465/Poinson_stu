# -*- coding: utf-8 -*-
# @Time : 2025/12/7 0:49
# @Author : nanji
# @Site :https://blog.csdn.net/yeshang_lady/article/details/140762560
# @File : testRunnableGenerator.py
# @Software: PyCharm
# @Comment :
import os
from langchain_core.runnables import RunnableLambda, RunnableGenerator
from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import CommaSeparatedListOutputParser
from langchain_deepseek import ChatDeepSeek

prompt = PromptTemplate.from_template("输出1到{max_value}之间的所有整数。每个数字之间用逗号,分隔。")


def add_one(x):
    return ' '.join([str((int(i) + 1)) for i in x])


runnable = RunnableLambda(add_one)
# llm = ChatOpenAI()
load_dotenv('../assets/.env')
llm = ChatDeepSeek(
    model=os.getenv('MODEL_NAME'),
    # stop = "三",#下面的bind相当于这里填入
    # stop = "很",
    temperature=0.8
)
chain = prompt | llm | CommaSeparatedListOutputParser() | runnable
print(chain.invoke({"max_value": "10"}))
# 流式处理
# stream_llm = ChatOpenAI(model_kwargs={"stream": True})
stream_llm = ChatDeepSeek(
    model=os.getenv('MODEL_NAME'),
    model_kwargs={'stream': True}
)


def stream_add_one(x):
    for i in x:
        if i.content.isdigit():
            yield str((int(i.content) + 1))


stream_chain = prompt | stream_llm | RunnableGenerator(stream_add_one)
for chunk in stream_chain.stream({"max_value": "10"}):
    print(chunk)
