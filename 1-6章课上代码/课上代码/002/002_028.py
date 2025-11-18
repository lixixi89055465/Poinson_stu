# -*- coding: utf-8 -*-
# @Time : 2025/11/18 16:06
# @Author : nanji
# @Site : 
# @File : 002_028.py
# @Software: PyCharm 
# @Comment :
import os
from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.prompts import PromptTemplate, FewShotPromptTemplate
from langchain_core.example_selectors import SemanticSimilarityExampleSelector
from langchain_community.vectorstores import FAISS
from langchain_openai import ChatOpenAI

# SemanticSimilarityExampleSelector
# Semantic语义
# Similarity相似性
# 核心选择策略差异
# SemanticSimilarityExampleSelector
# 策略：该选择器基于语义相似度来挑选示例。它会计算输入文本与每个示例文本之间的语义相似度得分，然后选择得分最高的 k 个示例。
# 特点：简单直接，能确保选择的示例与输入在语义上最为接近，适用于需要紧密围绕输入主题的场景。例如，在进行近义词查询时，它会优先选择与输入词语语义最相似的示例。
from langchain_core.example_selectors import SemanticSimilarityExampleSelector

# 核心选择策略差异
# SemanticSimilarityExampleSelector
# 策略：该选择器基于语义相似度来挑选示例。它会计算输入文本与每个示例文本之间的语义相似度得分，然后选择得分最高的 k 个示例。
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
    {"i": "蛋白粉味的砖头粉", "o": "要你命三千"},
    {"i": "那我 问你", "o": "语气助词,或者喘不上气了开始思考"},
]
selector = SemanticSimilarityExampleSelector.from_examples(
    embeddings=HuggingFaceEmbeddings(model_name="all-MiniLM-L12-v2"),
    examples=examples,
    vectorstore_cls=FAISS,
    k=5,
)
print(selector)
finalT = FewShotPromptTemplate(
    example_prompt=PromptTemplate.from_template('我输入了{i}输出一个{o}'),
    example_selector=selector,
    prefix='我给你下面的例子,你帮我推理',
    suffix='我现在输入了{input},那么阁下又该如何应对呢?'
)
msg = finalT.format(input='那我 问你')
print(msg)

load_dotenv('../assets/.env')
print(os.environ['MODEL_NAME'])
llm = ChatOpenAI(model=os.getenv('MODEL_NAME'), temperature=1)
res = llm.invoke(msg)
print(res.content)
