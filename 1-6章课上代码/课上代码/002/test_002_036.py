# -*- coding: utf-8 -*-
# @Time : 2025/11/22 8:35
# @Author : nanji
# @Site : 
# @File : test_002_036.py
# @Software: PyCharm
# @Comment :

class PsDoom:
    def __init__(self):
        self.killed = 0
        self.dead = 0
        self.score = 'F'

    def gameBegin(self):
        self.killed = 999
        self.dead = 0
        self.score = 'SSS'

    def __enter__(self):
        print('doom 进入地狱')
        print('恶魔开始战力\n shake it baby')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('doom 开始通关了,恶魔devil may cry')
        if exc_type is not None:
            print(f'异常类型{exc_type}')
            print(f'异常信息{exc_val}')
            print(f'回溯信息{exc_tb}')


def IGotLucky():
    return PsDoom();


with IGotLucky() as cb:
    print(f'obj={cb}')
    cb.gameBegin()
    print(f'obj.killed={cb.killed}')
    print(f'obj.dead={cb.dead}')
    print(f'obj.score={cb.score}')
    print("铭刻:义父追魂戟,把离手越进义父离你越远>---红字增幅+26----------)三(--> ")
    a=1/0
