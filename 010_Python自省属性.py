# Author: O98K


"""
    通过一定的机制 查询到对象的内部结构

"""


class Person:
    name = "user"


class Student(Person):
    def __init__(self, scool_name):
        self.scool_name = scool_name


if __name__ == "__main__":
    user = Student("222")

    # 通过__dict__查询属性
    print(user.__dict__)
    user.__dict__["school_addr"] = "广州市"
    print(user.school_addr)
    print(Person.__dict__)
    print(user.name)
    a = [1, 2]

    # dir 列出对象所有的属性
    print(dir(a))
