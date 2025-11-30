# -*- coding: utf-8 -*-
# @Time : 2025/11/30 15:01
# @Author : nanji
# @Site : 
# @File : run02.py
# @Software: PyCharm
# @Comment :

from enum import Enum,Flag

class Permission(Flag):
    NONE=0
    READ=1
    WRITE=2
    EXECUTE=4

rw=Permission.READ|Permission.WRITE
print("0"*100)
print(rw, rw.value)