# -*- coding: utf-8 -*-
# @Time : 2025/12/12 23:50
# @Author : nanji
# @Site : 
# @File : test_04_16.py
# @Software: PyCharm
# @Comment :
# RunnableParallel一般跟这个混用,把字典进行分解
from langchain_core.messages import HumanMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import chain, RunnableParallel, RunnablePassthrough


@chain
def makeDocs(_):
    resultlit = []
    for i in range(1, 11):
        str1 = '肘肘吃了' + str(i) + '个鸡蛋'
        resultlit.append(str1)
    print(resultlit)
    return resultlit


print("0" * 100)
# print(makeDocs(3))

# run1 = RunnableParallel({'docs': makeDocs, 'question': RunnablePassthrough()})
# result = run1.invoke('肘肘最多吃了几个鸡蛋')
# print("1" * 100)
# print(result, result)
# dic1 = {
#     'docs': [
#         '肘肘吃了1个鸡蛋', '肘肘吃了2个鸡蛋', '肘肘吃了3个鸡蛋', '肘肘吃了4个鸡蛋', '肘肘吃了5个鸡蛋',
#         '肘肘吃了6个鸡蛋', '肘肘吃了7个鸡蛋', '肘肘吃了8个鸡蛋', '肘肘吃了9个鸡蛋', '肘肘吃了10个鸡蛋'
#     ],
#     'question': '肘肘最多吃了几个鸡蛋'
# }

prompt = ChatPromptTemplate.from_template('根据我提供的文档:{docs},回答问题:{question}')
# result = prompt.invoke(dic1)
# print(result)
import os
from langchain_deepseek import ChatDeepSeek
from dotenv import load_dotenv

load_dotenv('../assets/.env')
llm = ChatDeepSeek(
    model=os.getenv('MODEL_NAME'),
    temperature=0.8
)
chain1 = {'docs': makeDocs, 'question': RunnablePassthrough()} | prompt | llm | StrOutputParser()
# ai_msg = chain1.invoke('肘肘最多吃了几个鸡蛋')
ai_msg = chain1.invoke('肘肘一共吃了几个鸡蛋')
print("0" * 100)
print('ai_msg:', ai_msg)
