# -*- coding: utf-8 -*-
# @Time : 2025/12/12 23:36
# @Author : nanji
# @Site : 
# @File : test04.py
# @Software: PyCharm
# @Comment :
import json

x = {'name':'你猜','age':19,'city':'四川'}

#用dumps将python编码成json字符串
# y = json.dumps(x)
# print(y)

z = json.dumps(x, indent=0)
print(z)
