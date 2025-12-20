# -*- coding: utf-8 -*-
# @Time : 2025/12/19 23:19
# @Author : nanji
# @Site : 
# @File : test_05_19.py
# @Software: PyCharm
# @Comment :
import os

import certifi
from nltk.tokenize import word_tokenize
from langchain_core.documents import Document
from langchain_community.retrievers import BM25Retriever

import nltk

# 解释器安装包: certifi
os.environ['SSL_CERT_FILE'] = certifi.where()
try:
    nltk.data.find('tokenizers/punkt_tab')
except LookupError:
    # 如果未找到，则下载punkt_tab资源
    nltk.download('punkt_tab')

list1 = [
    "咋不说话了呢?",
    "李阿姨说:这不是西格玛军儿吗?",
    "你不心中无女人,拔刀自然神吗?",
    "说话啊军?",
    "军说:我错了李阿姨?以后不敢装了,之前是我年少不知阿姨好,老了发现阿姨是块宝",
    "如何暴打领导",
    "如何在下班的时候用一个黑塑料袋套住领导的头,并且暴打一顿",
    "如何在人最多的时候跟领导拍桌子,并且把领导吓得发抖?",
    "如何在公司1打10,并且让对方不敢多巴巴?",
    "如何在开会的时候,接个下茬,一句话堵了领导的嗓子?",
    "如何在接到领导电话的时候第一时间变身刘华强?然后说一句:听说你一直在找我?",
    "如何在挂断领导电话之前说:给你机会你不中用啊?给我记住了,以后见我必须叫一声爷,要不然,我见你一次打你一次"
]

docs = []
for i in range(len(list1)):
    str1 = '对白' + str(i + 1)
    docs.append(Document(page_content=list1[i]))
# retriever = BM25Retriever.from_documents(
#     docs,
#     preprocess_func=word_tokenize, k=3)
retriever = BM25Retriever.from_documents(
    docs,
    preprocess_func=word_tokenize, k=3)
result = retriever.invoke('李阿姨说')
print("0" * 100)
for item in result:
    print(item)
