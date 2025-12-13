# -*- coding: utf-8 -*-
# @Time : 2025/12/13 14:41
# @Author : nanji
# @Site : 
# @File : test_05_01.py
# @Software: PyCharm
# @Comment :
# langchain-community==0.0.20
import bs4
from dotenv import load_dotenv

load_dotenv('../assets/.env')
# 这个是WebBaseLoader在网页所在服务器发送请求的时候发给服务器的
# openai.env 里面添加上USER_AGENT 可以不显示此警告,
# 这个环境变量要加载在WebBaseLoader 这个包引入之前
from langchain_community.document_loaders import WebBaseLoader

# url = "http://47.93.135.183"
url = "http://47.93.135.183:8080"
# url = "https://lilianweng.github.io/posts/2023-06-23-agent/"

# loader = WebBaseLoader(url).load() #这个默认是全家在
loader = WebBaseLoader(
    url,
    bs_kwargs={
        'parse_only': bs4.SoupStrainer(
            # 'h1',# 可以单独传一个
            [
                'h1',
                'p',
                # 找一个这个标签的<div class="inner">
                'div'
                # {"name": "div", "attrs": {"class": "prompt"}}  # 嵌套会出现警告
            ],
            attrs={"class": "post-title"}
            # attrs=dict(class = "prompt")#错误,class 是关键字
        )
    }
).load()
print("0" * 100)
print('loader:', loader)

dic1 = {'name': '张三', 'age': 18}
print("0"*100)
print('dic1:', dic1)
