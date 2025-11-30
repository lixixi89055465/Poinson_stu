# -*- coding: utf-8 -*-
# @Time : 2025/11/30 14:58
# @Author : nanji
# @Site : 
# @File : run01.py
# @Software: PyCharm
# @Comment :
from enum import Enum


class Permission(Enum):
    NONE = 0
    READ = 1
    WRITE = 2
    EXECUTE = 4


print(Permission.READ)
print("0" * 100)
print(Permission(1))

