# -*- coding: utf-8 -*-
# @Time : 2025/12/28 21:46
# @Author : nanji
# @Site : 
# @File : test_05_25.py
# @Software: PyCharm
# @Comment :
# 文档压缩的意义:让大模型帮忙减少冗余文档,因为第一次的文档是向量数据库查询得来的文档
# LLMChainExtractor  提取器,本质是一个链,里面带着 让大模型 提取文档的默认提示词模板
from dotenv import load_dotenv
import os
from langchain_classic.retrievers import ContextualCompressionRetriever
from langchain_classic.retrievers.document_compressors import LLMChainExtractor
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

load_dotenv('../../assets/.env')
from langchain_community.document_loaders import WebBaseLoader
import bs4
from langchain_text_splitters import RecursiveCharacterTextSplitter

os.environ['TOKENIZERS_PARALLELISM'] = 'false'
url = "https://blog.csdn.net/boildoctor/article/details/123654243"
loader = WebBaseLoader(
    url,
    bs_kwargs={
        'parse_only': bs4.SoupStrainer(
            [
                "article"  # 这个标签的寻找方式,详见后面的视频课程:05_11手动筛选html网页源代码获取loader使用的标签
            ],
        )
    }
)
docs = loader.load()
splitter = RecursiveCharacterTextSplitter(chunk_size=200, chunk_overlap=40)
split_documents = splitter.split_documents(docs)  # 分割器返回分割后的文档
# 创建向量数据库
embedding = HuggingFaceEmbeddings(model_name='shibing624/text2vec-base-chinese')
# 嵌入的作用:是把自然语言文本转化到向量数据库中的过程
vectorstore = Chroma.from_documents(split_documents, embedding=embedding)
# 创建检索器,相当于在检索器执行invoke时在向量数据库里面查询
retriever = vectorstore.as_retriever()
result1 = retriever.invoke("重签名是什么")
print("铭刻:义父追魂戟,把离手越进义父离你越远>---红字增幅+26----------)三(--> ")
print("result1=", result1)
for i in range(len(result1)):
    print(str(i), " :", result1[i].page_content)
print("铭刻:义父追魂戟,把离手越进义父离你越远>---红字增幅+26----------)三(--> ")
print("3" * 100)
import os
from langchain_deepseek import ChatDeepSeek
from dotenv import load_dotenv

load_dotenv("../../assets/.env")
llm = ChatDeepSeek(
    model=os.getenv('MODEL_NAME'),
    temperature=0.8
)

# 创建提取器,压缩器
extractor = LLMChainExtractor.from_llm(llm)
print('extractor:', extractor)

compression_retriever = ContextualCompressionRetriever(
    base_compressor=extractor,
    base_retriever=retriever
)
print('compression_retriever:', compression_retriever)
result2 = compression_retriever.invoke('重签名是什么?')
print("4" * 100)
print('result2:', result2)
for i, v in enumerate(result2):
    print(f'{i} : {v.page_content}')
