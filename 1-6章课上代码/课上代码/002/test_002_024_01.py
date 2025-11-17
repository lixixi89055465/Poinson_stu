# -*- coding: utf-8 -*-
# @Time : 2025/11/17 21:48
# @Author : nanji
# @Site : 
# @File : test_002_024_01.py
# @Software: PyCharm
# @Comment :

import os
from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.prompts import PromptTemplate, FewShotPromptTemplate
from langchain_core.example_selectors import MaxMarginalRelevanceExampleSelector
from langchain_community.vectorstores import FAISS
from langchain_openai import ChatOpenAI

os.environ['TOKENIZERS_PARALLELISM'] = 'false'
examples = [
    {"i": "苹果", "o": "水果"},
    {"i": "香蕉", "o": "水果"},
    {"i": "汽车", "o": "交通工具"},
    {"i": "自行车", "o": "交通工具"},
    {"i": "猫", "o": "动物"},
    {"i": "狗", "o": "动物"},
    {"i": "蛋白粉", "o": "营养补剂"},
    {"i": "蛋清粉", "o": "助推燃料"},
    {"i": "蛋白粉味的玉米粉", "o": "碳水"},
]
s1 = MaxMarginalRelevanceExampleSelector.from_examples(
    examples,
    HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2", cache_folder='D://models'),
    FAISS,
    k=6,
)
print(s1)
t1 = PromptTemplate.from_template("输入了{i}输出一个{o}")
fspt = FewShotPromptTemplate(
    example_selector=s1,
    example_prompt=t1,
    prefix='我输入下面的例子,你来推理吧',
    suffix='我现在输入一个{i},你推理一下,输出什么?'
)
msg = fspt.format(i='蛋清屁')
print(msg)
# 功能：结合了语义相似度和多样性，通过最大边际相关性（MMR）算法选择示例。
# 它不仅会选择与输入语义相似的示例，还会尽量保证所选示例之间的多样性。
load_dotenv('../assets/.env')
print(os.getenv('MODEL_NAME'))
llm = ChatOpenAI(model=os.getenv('MODEL_NAME'), temperature=1)
res = llm.invoke(msg)
print(res.content)
