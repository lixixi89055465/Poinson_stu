# -*- coding: utf-8 -*-
# @Time : 2025/12/13 8:47
# @Author : nanji
# @Site : 
# @File : test_04_18.py
# @Software: PyCharm
# @Comment :
# retriever检索器,取回的意思
# Document 的作用
# Document 能把文本内容和相关元数据组合成一个对象，方便在代码里进行管理和操作。
# 例如，在你的代码中，向量数据库存储的就是 Document 对象列表，这样每个文本都能关联其对应的元数据
# 和唯一标识符。
# 2. 检索和匹配
# 当使用检索器（如 retriever）从向量数据库中查找与问题相关的文档时，返回的结果就是 Document 对象列表。
# 这样可以方便地获取文档的内容和元数据，为后续的处理提供依据。
# 3. 与大语言模型集成
# 在问答系统里，Document 对象的内容可以作为上下文信息传递给大语言模型，辅助模型生成更准确的回答。例如，
# 在你的代码中，RunnableParallel 会把检索到的 Document 对象列表作为上下文信息传递给提示模板，然后再传递给大语言模型。
# 设置环境变量，禁用 tokenizers 并行处理
import os
from langchain_community.vectorstores import FAISS
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_huggingface import HuggingFaceEmbeddings

os.environ[r'TOKENIZERS_PARALLELISM'] = 'false'
# 创建 FAISS 向量数据库 ,
# vectorstore = FAISS.from_texts(
#     [
#         "肘肘深蹲时候使用蛋清反重力系统",
#         "肘肘锻炼肩膀中束的时候使用重力对抗系统增加难度",
#         "肘肘吃鸡蛋的时候用臀大肌夹碎鸡蛋"
#     ],
#     embedding=HuggingFaceEmbeddings(model_name='all-MiniLM-L12-v2',
#                                     cache_folder='D:/workspace/all-MiniLM-L12-v2')
# )
# retriever = vectorstore.as_retriever()  # 通过向量数据库创建检索器VectorStoreRetriever
# print('retriever:', retriever)
# result = retriever.invoke('肘肘锻炼肩膀中束用的什么')  # 生成列表[Document]
# print('ai_msg:', ai_msg)
# print("result=",result)
prompt = ChatPromptTemplate.from_template(
    """
    根据语境回答问题
    {docs}
    问题:{question}
    """
)
# chain1= {"docs":retriever,"question":RunnablePassthrough()} | prompt