# Author: O98K

"""
    Python 可以说是没有类型的，类型的符号只是一种标志，所以在编译时无法发现代码的错误，只有在运行时
    才能发现错误，所以不需要明确指定变量的类型

    在设计实现某些功能时，会强制如果需要使用它必须实现某些方法
    比如强制某个子类必须遵循某些方法

"""


import abc


class Base(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def get(self, key):
        pass

    @abc.abstractmethod
    def set(self, key):
        pass


class ChildClass(Base):

    def get(self, key):
        pass

    def set(self, key):
        pass


# 通过设计抽象基类，使得子类必须遵循父类的规则  重载父类的某些方法等
# 不在子类中添加 约束必须添加的方法 就会报错
myclass = ChildClass()

"""
    不建议使用 抽象基类，这样子就打破了 Python的 自由 理念

    尽量使用 鸭子类型 的概念 或者 minxin 实现某些功能，因为这样子比较灵活
"""






