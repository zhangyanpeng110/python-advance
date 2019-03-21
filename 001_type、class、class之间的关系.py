# Author: O98K

# 1.type 也是一个类

class A:
    pass

class B(A):
    pass

myclass = B()

# 2.object 所有类（包括python内置的）的最顶层的基类
print(type(int))
print('int bases ===>>>', int.__bases__)
print(B.__bases__)




