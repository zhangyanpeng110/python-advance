# Author: O98K

class A(object):
    def __init__(self):
        print('A')


class B(A):
    def __init__(self):
        print('B')
        super().__init__()


if __name__ == '__main__':
    myclass = B()

"""
    super 并不是调用父类的 构造函数
    
    super 执行的顺序与 mro 属性查找的顺序相同

"""