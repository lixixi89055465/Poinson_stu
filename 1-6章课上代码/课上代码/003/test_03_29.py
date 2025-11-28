# -*- coding: utf-8 -*-
# @Time : 2025/11/28 22:16
# @Author : nanji
# @Site : 
# @File : test_03_29.py
# @Software: PyCharm
# @Comment :

from typing import Any
from pydantic import BaseModel, Field, field_validator


class ZhouZhou(BaseModel):
    name: str = Field(description="jojo的奇妙冒险中的一个任务名字")
    age: int = Field(description="年龄")

    @field_validator('age')
    def validate_age(cls, value):
        if value < 18:
            print('未满18岁')
        if value > 65:
            print("退休了,可以回家打游戏,到大街上,抽嘎了")
        return value


ZhouZhou(name="空条承太郎", age=23)  # 对象被创建的时候就会执行验证
ZhouZhou(name="空条承太郎", age=66)  # 对象被创建的时候就会执行验证
