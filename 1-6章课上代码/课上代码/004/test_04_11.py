# -*- coding: utf-8 -*-
# @Time : 2025/12/7 17:59
# @Author : nanji
# @Site : 
# @File : test_04_11.py
# @Software: PyCharm
# @Comment :
from collections.abc import Callable


class RullableLawada:
    def __init__(self, func: Callable[[int, int], int]):
        self.func = func
        print("软啦布拉乌达创建成功=======================>")

    def invoke(self, a, b):
        self.func(a, b)
        print('invoke 执行 id=', id(self))


def qian(func: Callable[[int, int], int]):
    print("qian执行了=======>")  # 执行了附加的东西
    return RullableLawada(func)


@qian
def tamenchongworengbaba(a, b):
    result = a + b
    print("tamenchongworengbaba他们冲我扔粑粑,我拿粑粑做蛋挞", result)
    return result


tamenchongworengbaba.invoke(3, 4)
tamenchongworengbaba.invoke(3, 4)


@qian
def add(a, b) -> int:
    result = a + b
    print("add执行", result)
    return result


def sub(a, b):
    result = a - b
    print('sub执行', result)
    return result


# r2 = RullableLawada(sub)
# print("r2类型",type(r2))
# a=r2.func(1,2)
# print(a)
print("0"*100)
add.invoke(10, 1)
# add.invoke(10, 2)
# print("1" * 100)
# qian(add)
# print("2" * 100)
# qian(add)
print(add)
print("3" * 100)
add(1, 2)
