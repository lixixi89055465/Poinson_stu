"""
prompts是提示的意思
Template模板
PromptTemplate提示词模板
"""
import os

from dotenv import load_dotenv
from langchain_openai import OpenAI, ChatOpenAI
from langchain_core.prompts import PromptTemplate

"""
PromptTemplate.from_template类方法接收一个字符串模板作为输入，
该模板中可以包含使用花括号 {} 包裹的变量占位符，
这些占位符将在后续使用模板生成提示时被具体的值替换。其基本调用格式如下：

"""
# load_dotenv("../assets/.env")
load_dotenv("../assets/.env")
print(os.getenv("OPENAI_API_BASE"))
prompt_template = PromptTemplate.from_template("你是一个天气预报系统告诉我{city}{data}的天气预报")
template_format = prompt_template.format(city="哈尔滨", data="明天")
print(r"---------{} -------".format(template_format))
llm = ChatOpenAI(model="gpt-3.5-turbo-0613",
                 openai_api_key="hk-2l8xr81000053052db08020dea40797aaaf526c81a7154a1",
                 openai_api_base="https://api.openai-hk.com"
                 )
response = llm.invoke(template_format)
print(response.content)
