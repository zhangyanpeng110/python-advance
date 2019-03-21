# Author: O98K

"""
    经典类和新式类(继承 object)的属性查找区别：
        Python 2.X 深度优先         默认经典类
        Python 3.X 广度优先         均为新式类

    mro(method resolution order)        C3 算法
"""


class A(object):
    name = 'object A'

    def __init__(self, name):
        self.name = 'A instance'


class B(object):
    name = 'object B'

    def __init__(self, name):
        self.name = name


class C(object):
    name = 'object C'

    def __init__(self, name):
        self.name = 'C instance'


class D(C, B):
    # class D(B, C):
    # 继承的先后顺序 影像查找属性的顺序
    # name = 'object D'

    def __init__(self, name):
        pass


myclass = A('myclass instance')
print(myclass.name)
print(A.name)

dclass = D('D')
print('dclass ===>>>', dclass.name)
