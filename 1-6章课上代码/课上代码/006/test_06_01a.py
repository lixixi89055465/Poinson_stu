# -*- coding: utf-8 -*-
# @Time : 2026/1/3 21:18
# @Author : nanji
# @Site : 
# @File : test_06_01.py
# @Software: PyCharm
# @Comment :
import requests
import json
import os

# 区别在于url不同,一个是rerank,翻译过来叫重新排序,一个叫web-search,是网络搜索
url = "https://api.langsearch.com/v1/rerank"
from dotenv import load_dotenv

load_dotenv('../assets/.env')
api = os.getenv('LangSearchAPI')
print('api=', api)
# 下面是带参考文档的
data = json.dumps({  # 给接口传入的数据
    "model": "langsearch-reranker-v1",
    "query": "告诉我哈尔滨市2025年5月14日天气预报",  # 查询问题
    "top_n": 2,  # 选出3个最靠前的
    "return_documents": True,
    "documents": [
        "体脂率9%",
        "身高181.5",
        "告诉我哈尔滨市2025年5月14日天气预报",
        "体重70公斤",
        "天气晴朗",
        "乌云密布",
    ]
})
# 这个是请求头
headers = {
    'Authorization': os.getenv("LangSearchAPI"),  # token,
    'Content-Type': 'application/json'
    # 这个是类型,例如text/html, text/plain, application/json, multipart/form-data, image/jpeg, video/mp4
}
# 这个可以帮助筛选文档
# 下面是发送请求POST PUT Get ,请求后台接口
# url是请求接口地址,headers是请求头,data是传过去的数据,也可以是流
response = requests.request("POST", url, headers=headers, data=data)
print(response.text)
