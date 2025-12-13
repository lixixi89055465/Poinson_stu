# -*- coding: utf-8 -*-
# @Time : 2025/12/7 16:20
# @Author : nanji
# @Site : 
# @File : test_04_08a.py
# @Software: PyCharm
# @Comment :
# RunnableParallel
# parallel并行的意思
from langchain_core.runnables import RunnableLambda, RunnableParallel


def add(a, b):
    result = a + b
    print("add()=", result)
    return result


def sub(a, b):
    result = a - b
    print("sub()=", result)
    return result


runnable2 = RunnableLambda(lambda x: add(x[0], x[1]))
runnable3 = RunnableLambda(lambda x: sub(x[0], x[1]))


#
# runnable2.invoke((1,1))
# runnable3.invoke((10,1))
# chain=RunnableParallel(run1=runnable2,run2=runnable3)#语法,用任意命名的参数kwargs的语法,可以把其他runnable对象放进来,用逗号隔开
# chain=RunnableParallel(run1=runnable2,run2=runnable3)#语法,用任意命名的参数kwargs的语法,可以把其他runnable对象放进来,用逗号隔开

def makeTuple(a, b):
    result = (a, b)
    print("调用制造元组makeTuple,生成的元组是=", result)
    return result


# makeTuple(1,1)
runnable1 = RunnableLambda(lambda x: makeTuple(x[0], x[1]))
runnable1.invoke((1, 1))
chain = runnable1 | {'run3': runnable2, 'run4': runnable3}
# 管道操作符|强制转换,字典转并行 放在链里面可以省略外面的RunnableParallel
result = chain.invoke((1, 1))
print(result)
print("0" * 100)
print(type(result))
print("1" * 100)
print(result['run3'])
print("2" * 100)
print(result['run4'])
