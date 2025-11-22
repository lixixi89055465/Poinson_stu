# -*- coding: utf-8 -*-
# @Time : 2025/11/22 14:27
# @Author : nanji
# @Site : 
# @File : test_002_005b3.py
# @Software: PyCharm
# @Comment :
# from pydantic import BaseModel, Field
from pydantic import BaseModel, Field, field_validator
# from langchain_core.pydantic_v1 import BaseModel,Field
# from langchain_core.output_parsers import PydanticOutputParser
from langchain.output_parsers import PydanticOutputParser
import json


class ZhouZhou(BaseModel):
    name: str = Field(min_length=2, max_length=6, description='姓名')
    age: int = Field(gt=0, lt=999, description="年龄")  # 限定一个验证的大小

    @field_validator('name')
    def name_validator(cls, a):
        if '夏妮' in a:
            print('发现相声界的评论家,红色预警')
        return a

    @field_validator("age")
    def age_validator(cls, a):
        if a == 888:
            print('发现藏马')
        return a


# res_content = '{"name": "张三", "age": 18,"money":9999}'
res_content = '{"name": "张夏妮三", "age": 888}'
parser = PydanticOutputParser(pydantic_object=ZhouZhou)

try:
    parsed = parser.parse(res_content)
    print('执行成功')
    dic = parsed.model_dump()
    print(dic['name'])
    print("0" * 100)
    jsonstr = json.dumps(dic, ensure_ascii=True, indent=None)
    print("1" * 100)
    print(jsonstr)
    print("2" * 100)

except Exception as error:
    print('执行错误')
    print(error)
    pass
