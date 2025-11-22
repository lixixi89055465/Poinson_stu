# -*- coding: utf-8 -*-
# @Time : 2025/11/23 0:25
# @Author : nanji
# @Site : 
# @File : test_03_10.py
# @Software: PyCharm
# @Comment :


import threading


def fun1(num):
    print('县城开始:', num, end='结束了\n')
    for i in range(10):
        print(num, ':', i)

thread1 = threading.Thread(target=fun1, args=(1,))
# thread1 = threading.Thread(target=fun1, args=(1))
thread1.start()
a=2,# 这个类型是元组
thread2=threading.Thread(target=fun1,args=(a))
thread2.start()

thread1.join()
thread2.join()
print("铭刻:义父追魂戟,把离手越进义父离你越远>---红字增幅+26----------)三(--> ")

