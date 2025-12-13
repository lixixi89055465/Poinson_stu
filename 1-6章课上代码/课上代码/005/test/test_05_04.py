# -*- coding: utf-8 -*-
# @Time : 2025/12/13 15:55
# @Author : nanji
# @Site : 
# @File : test_05_04.py
# @Software: PyCharm
# @Comment :
# ssl 证书查找的问题
# 开发者模式里面查找cookie选配参数
# https://www.bilibili.com/video/BV1MuRZYsEmL
# https://python.langchain.com/api_reference/community/document_loaders.html
# 安装并配置证书库 ,解决错误ssl_shutdown_timeout
# 解释器安装包: certifi
import os

import certifi

os.environ['SSL_CERT_FILE'] = certifi.where()
# 需要安装包:解释器中安装:  bilibili-api-python
bili_jct = "20fcb150a75ab5deae8e1f408fdfdad3"
SESSDATA = "295e3c2d%2C1781103928%2C502f3%2Ac2CjBq89xySvZef8uNcUkxGNIbXZY33dhyboKvakdXIvoYvMzDbfOmlXTSdDUctJ2tZqQSVlRNbkNMQlFwNzlyZEcxMF82Z0xfRENOQkN1WUV6WHAyNFVWOTNIYlpkeU5OM3FVVmNIUEIwTEgwU2tENnlLTTN0dFZXT3ZqWDZoS3huNkl3SklZdzFBIIEC"
buvid3 = "0FCE2E85-1A97-0260-FE9D-747CFD40466171297infoc"

from langchain_community.document_loaders import BiliBiliLoader

urls = [
    "https://www.bilibili.com/video/BV1MuRZYsEmL"
]
loader = BiliBiliLoader(
    urls,
    sessdata=SESSDATA,
    bili_jct=bili_jct,
    buvid3=buvid3,
)
docs = loader.load()
for doc in docs:
    print("页面内容")
    print(doc.page_content)
    print("元数据")
    print(doc.metadata)
