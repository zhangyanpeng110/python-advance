# Author: O98K


class A(object):
    name = 'object a'

    def __init__(self, x, y):
        self.x = x
        self.y = y


a = A(1, 2)
print(a.x, a.y, a.name)

# print(A.x)
"""
  File "F:/code/python-advance/006_类变量和实例变量.py", line 15, in <module>
    print(A.x)
AttributeError: type object 'A' has no attribute 'x'
"""

print(A.name)

A.name = 'change name by A class'
a.name = 'get name from a instance'
# 因为实例中实际没有 name 这个变量，所以这里相当于添加 name 这个变量
# 而获取的时候因为本身实例就有了这个属性所以不会去找父类里面的
print(a.name)
print(A.name)

"""
    类变量：
        提供给类调用的，但实例也可通过类间接调用    实例共享类变量
        
    实例变量：
        提供给实例调用，但是只能通过实例调用

"""










