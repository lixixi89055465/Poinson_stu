# -*- coding: utf-8 -*-
# @Time : 2025/12/13 15:36
# @Author : nanji
# @Site : 
# @File : test02.py
# @Software: PyCharm
# @Comment :

# https://blog.csdn.net/rengang66/article/details/155447018
import bs4
from langchain_community.document_loaders import WebBaseLoader

# 加载新闻文章内容
loader = WebBaseLoader(
    web_paths=(
    "https://techcrunch.com/2024/12/28/google-ceo-says-ai-model-gemini-will-the-companys-biggest-focus-in-2025/",),
    # 配置BeautifulSoup只解析特定的div元素
    bs_kwargs=dict(
        parse_only=bs4.SoupStrainer(
            "div",
            attrs={"class": [
                "entry-content wp-block-post-content is-layout-constrained wp-block-post-content-is-layout-constrained"]},
        )
    ),
    # 在请求头中设置用户代理，模拟浏览器访问
    header_template={
        "User_Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36",
    },
)
# 加载和处理文档
docs = loader.load()
print(f"文档数量: {len(docs)}")
print("0" * 100)
print(docs[0].page_content[:300])

import nest_asyncio
nest_asyncio.apply()
loader.requests_per_second = 1
# 加载和处理文档
docs = loader.load()
print("2"*100)
print(docs[0].page_content[:100])