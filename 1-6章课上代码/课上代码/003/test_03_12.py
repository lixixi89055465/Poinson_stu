# -*- coding: utf-8 -*-
# @Time : 2025/11/23 1:32
# @Author : nanji
# @Site : 
# @File : test_03_12.py
# @Software: PyCharm
# @Comment :

import os
from dotenv import load_dotenv
from langchain_deepseek import ChatDeepSeek
from langchain_core.rate_limiters import InMemoryRateLimiter

load_dotenv('../assets/.env')
limiter = InMemoryRateLimiter(
    requests_per_second=2,
    check_every_n_seconds=0.1,
    max_bucket_size=2
)
llm = ChatDeepSeek(model=os.getenv('MODEL_NAME'),
                   timeout=30,
                   max_tokens=200,
                   stop='好',
                   max_retries=2,
                   rate_limiter=limiter,
                   temperature=0.8)
res = llm.invoke('你们怎么样啊')
print(res.content)
