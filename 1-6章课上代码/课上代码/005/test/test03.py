# -*- coding: utf-8 -*-
# @Time : 2025/12/27 23:13
# @Author : nanji
# @Site : 
# @File : test03.py
# @Software: PyCharm
# @Comment :
import json

data = {"name": "小明", "info": "Hello 😊"}
print("0"*100)
print(json.dumps(data, ensure_ascii=True))

