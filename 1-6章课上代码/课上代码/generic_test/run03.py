# -*- coding: utf-8 -*-
# @Time : 2025/11/30 16:05
# @Author : nanji
# @Site : 
# @File : run03.py
# @Software: PyCharm
# @Comment :
s1 = 'HelloWorld'
s2 = 'Hello' + 'World'
s3 = ''.join('Hello' + 'World')
print(id(s1), id(s2), id(s3))
print(s1 is s2)
print(s1 is s3)
print("0" * 100)
print(s1 == s2)
print(s1 == s3)
