# Author: O98K

"""
    魔术方法是重载运算符的昵称，形式是__init__类似这样的前后双下滑线组成的函数
    常用：
        __init__,__new__,__call__,__str__,__getitem__ 等

    作用：
        增强对象的类型，增加属性等


1.非数学运算
    字符串表示
        __repr__ __str__

    集合、序列相关
        __len__ __getitem__ __setitem__ __delitem__ __contains__
    .......
2.数学运算
    一元运算符
    二元运算符

"""


class A(object):
    def __init__(self):
        pass

    def __getitem__(self, item):
        return item


# 通过魔法函数使得 类A的实例能够成为可迭代对象
myclass = A()
for i in myclass:
    print('<>')


"""
    Python 为一门解释器函数，所以Python通过魔法函数或者其它的机制改变Python 代码的执行
    举例：
        len() 求长度的时候，实际上内部会尽可能实现计算的性能，通过直接借助底层由 C 语言
        定义这些对象处理而实现快速的计算
    
        所以在使用方法的时候尽量使用Python内部函数


"""

