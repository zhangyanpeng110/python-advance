# Author: O98K


class A(object):
    pass


class B(A):
    pass


myclass = B()

# isinstance 会检查 继承关系
# type 只检查其当前的父类
print(isinstance(myclass, B))
print(isinstance(myclass, A))

print(type(myclass))

"""
    is 判断 id 是否相同
    == 判断值是否相同
    
"""
