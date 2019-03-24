 # Author: O98K


class Single(object):
    """
        __new__ 在 __init__ 之前执行

        1.__new__ 控制对象的生成过程，在对象生成之前执行
        2.__init__ 完善对象
        注意：
            如果 __new__ 没有指定返回对象(*****注意是返回对象)，则不会触发执行 __init__
    """

    def __new__(cls, *args, **kwargs):
        print('first execute')
        return super().__new__(cls, *args, **kwargs)

    def __init__(self):
        print("after __new__ return cls")


myclass1 = Single()
# myclass2 = Single()
#
# print(id(myclass1))
# print(id(myclass2))

