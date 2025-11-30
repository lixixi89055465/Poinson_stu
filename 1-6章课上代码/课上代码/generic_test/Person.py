# -*- coding: utf-8 -*-
# @Time : 2025/11/30 14:17
# @Author : nanji
# @Site : 
# @File : Person.py
# @Software: PyCharm
# @Comment :
import attr
from operator import attrgetter


class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender


wang = Person('wang', 18, 'M')
get_name = attrgetter("name", "age", "name.find")
name, age, find = get_name(wang)
print("0" * 100)
print(f"{name},{age},{find}", name, age, find)
