# -*- coding: utf-8 -*-
# @Time : 2025/11/30 9:13
# @Author : nanji
# @Site : 
# @File : covar.py
# @Software: PyCharm
# @Comment :

from typing import List, TypeVar, Generic


class Animal:
    pass


class Cat(Animal):
    pass


class Dog(Animal):
    pass


# AnimalType = TypeVar('AnimalType', bound=Animal)
AnimalType = TypeVar('AnimalType', bound=Animal,covariant=True)


class Store(Generic[AnimalType]):
    def __init__(self, stock: List[AnimalType]) -> None:
        self.stock = stock

    def buy(self) -> AnimalType:
        return self.stock.pop()


wang = Store[Dog]([Dog(), Dog()])
li = Store[Animal]([Cat(), Cat()])
print("0" * 100)
print(wang.buy())

a: Animal = wang.buy()
# d: Animal = wang.buy()
a2: Animal = li.buy()
# c: Cat = wang.buy()
print("1" * 100)
print(Store[int]([]))
