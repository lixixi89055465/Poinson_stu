# -*- coding: utf-8 -*-
# @Time : 2026/1/2 14:31
# @Author : nanji
# @Site : 
# @File : test_05_33.py
# @Software: PyCharm
# @Comment :
# 第一步,创建一个分割后的文档的检索器
import bs4
from dotenv import load_dotenv
from langchain_classic.chains.history_aware_retriever import create_history_aware_retriever
from langchain_community.vectorstores import FAISS
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
import os

load_dotenv('../../assets/.env')
from langchain_community.document_loaders import WebBaseLoader

# 设置环境变量，禁用 tokenizers 分词器 并行处理
os.environ['TOKENIZERS_PARALLELISM'] = 'false'
url = "https://download.csdn.net/download/boildoctor/802404?spm=1001.2014.3001.5501"
loader = WebBaseLoader(
    # (url,1)#不能这么给
    url,
    # 捕获这种标签 <div class="detail hidden no-preview"
    bs_kwargs={
        'parse_only': bs4.SoupStrainer(
            [
                'div'
            ],
            attrs={'class': 'detail hidden no-preview'}
        )
    }
)
docs = loader.load()
print(f'docs:{docs}')
splitter = RecursiveCharacterTextSplitter(chunk_size=200, chunk_overlap=50)
split_documents = splitter.split_documents(docs)  # 分割器返回分割后的文档
print(f'split_documents:{split_documents}')
for doc in split_documents:
    print("铭刻:义父追魂戟,把离手越进义父离你越远>---红字增幅+26----------)三(--> ")
    print(doc)

embedding = HuggingFaceEmbeddings(model_name="BAAI/bge-m3")  # 北京智源人工智能研究院 出的
vectorstore = FAISS.from_documents(split_documents, embedding=embedding)  # 通过分割后的小文档创建向量数据库
retriever = vectorstore.as_retriever()
# ;一.创建历史聊天感知链检索器:history_aware_retriever
# 历史聊天记录chat_history,或者叫上下文,都行
# 1.定义一个上下文(历史聊天记录)的系统提示词,这个是给后面整体提示词中,的system角色用的
context_sys_prompt = """
给定一段聊天记录以及用户提出的最新问题，
该问题可能会引用聊天记录中的上下文信息。
请构建一个独立的问题，使其在没有聊天记录的情况下也能被理解。
如果有必要，对问题进行重新表述，否则就按原样返回该问题。
"""
history_prompt = ChatPromptTemplate.from_messages(
    [
        ('system', context_sys_prompt),
        ('placeholder', "{chat_history}"),  # 这里放历史聊天记录,如果有的话就放这里,这个历史记录,第一次使用的时候是没有的,但是也能被感知到
        ('human', "{input}"),  # 这里是最终的用户输入,是多轮对话,每次用户输入的新问题
    ]
)
import os
from langchain_deepseek import ChatDeepSeek
from dotenv import load_dotenv

load_dotenv('../../assets/.env')

llm = ChatDeepSeek(
    model=os.getenv('MODEL_NAME'),
    temperature=0.8
)
# 3.创建历史感知检索器,用来检查是否输入了聊天历史记录,
# 本质上,是分支结构,里面会判断最终invoke输入的字典是否包含input 和chat_history,
# 其中chat_history可以不包含
history_aware_retriever=create_history_aware_retriever(llm,retriever,history_prompt)
print('history_aware_retriever:',history_aware_retriever)
