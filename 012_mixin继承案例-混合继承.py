# Author: O98K

"""
多继承特性，使得当基类设计不合理时会造成属性关系混乱

Django Rest framework   就是使用这种设计模式
    mixin 设计模式
        1.mixin 类功能单一
        2.不和基类关联，可以和任一基类组合，基类可以不和mixin关联就能初始化成功
        3.不能使用 super
"""




