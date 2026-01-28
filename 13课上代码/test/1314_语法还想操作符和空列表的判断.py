# -*- coding: utf-8 -*-
# @Time : 2026/1/28 22:33
# @Author : nanji
# @Site : 
# @File : 1314_语法还想操作符和空列表的判断.py.py
# @Software: PyCharm
# @Comment :
inputs = {"messages": ["你好", "把你的手机"]}
inputs = {}
result = inputs.get('messages', [])
print('result=\t', result)

# 海象运算符,第一步先把:=右边的值赋值给左边的变量,第二部,再用if 判断这个变量
if i := 3:
    print(i)
else:
    print('假')

if []:
    print('真')
else:
    print('假')
