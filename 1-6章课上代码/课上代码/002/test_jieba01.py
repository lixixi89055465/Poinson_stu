# -*- coding: utf-8 -*-
# @Time : 2025/11/18 14:27
# @Author : nanji
# @Site : 
# @File : test_jieba01.py
# @Software: PyCharm 
# @Comment :
#
# import jieba
#
# txt = open("utf8_sanguo.txt", 'r', encoding='utf-8').read()
# # txt = open("utf8_sanguo.txt", 'r', encoding='gb18030').read()
# words = jieba.lcut(txt)
# counts = {}
# for word in words:
#     if len(word) == 1:
#         continue
#     else:
#         counts[word] = counts.get(word, 0) + 1
#
# items = list(counts.items())
# items.sort(key=lambda x: x[1], reverse=True)
# for i in range(3):
#     word, count = items[i]
#     print("{0:<5}{1:>5}".format(word, count))

def get_text():
    txt=open('1.txt','r',encoding='utf-8').read()
    txt=txt.lower()
    for ch in '!"#$%&()*+,-./:;<=>?@[\\]^_‘{|}~':
        txt=txt.replace(ch,' ')
    return txt

file_txt=get_text()
words=file_txt.split()
counts={}
for word in words:
    if len(word)==1:
        continue
    else:
        counts[word]=counts.get(word,0)+1

items=list(counts.items())
items.sort(key=lambda x:x[1],reverse=True)
for i in range(5):
    word,count=items[i]
    print('{0:<5}->{1:>5}'.format(word,count))