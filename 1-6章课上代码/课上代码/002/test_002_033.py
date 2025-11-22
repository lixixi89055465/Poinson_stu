# -*- coding: utf-8 -*-
# @Time : 2025/11/19 21:57
# @Author : nanji
# @Site : 
# @File : test_002_033.py
# @Software: PyCharm
# @Comment :
import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv("../assets/.env")
print(os.getenv('MODEL_NAME'))
model_name = os.getenv("MODEL_NAME")
base_url = os.getenv("OPENAI_API_BASE")
api_key = os.getenv("OPENAI_API_KEY")
print(model_name)
print(base_url)
print(api_key)
print("当前目录:", os.getcwd())  # 打印当前目录,


class PsLian(OpenAI):
    def __init__(self):
        self.llm = OpenAI(
            api_key=api_key,
            base_url=base_url
        )

    def invoke(self, msg) -> str:
        response = self.llm.chat.completions.create(
            model=model_name,
            messages=[
                {
                    "role": "user",
                    "content": msg
                }
            ]
        )
        print("铭刻:义父追魂戟,把离手越进义父离你越远>---红字增幅+26----------)三(--> ")
        return response.choices[0].message.content


llm = PsLian()
print("abc")
res = llm.invoke("你好，我们中国人们银行")
print(res)
