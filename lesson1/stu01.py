# -*- coding: utf-8 -*-
# @Time : 2025/11/5 21:25
# @Author : nanji
# @Site : 
# @File : stu01.py
# @Software: PyCharm
# @Comment :

# Please install OpenAI SDK first: `pip3 install openai`
from dotenv import load_dotenv

# 加载 .env 文件中的环境变量
load_dotenv()

import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get('DEEPSEEK_API_KEY'),
    base_url="https://api.deepseek.com")

response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        # {"role": "system", "content": "You are a helpful assistant"},
        # {"role": "user", "content": "Hello"},
        {"role": "system", "content": "你是一个健身教练"},
        {"role": "user", "content": "你好,你太大我不想练了"},
        {"role": "assistant", "content": "别急帅哥,办张卡,你马上就能变帅"},
        {"role": "user", "content": "对不起,我没有钱,我的钱都买steam和epic游戏了"},
        {"role": "assistant", "content": "把你手机给我,你买课的钱,我来出,这是你的15万"},
        {"role": "user", "content": "对不起,我不想网贷"}
    ],
    stream=False
)

print(response.choices[0].message.content)
