# Author: O98K


class User(object):
    def __init__(self, name, pw):
        self.__name = name
        self.password = pw

    @property
    def get_name(self):
        return self.__name

    @get_name.setter
    def get_name(self, name):
        self.__name = name


if __name__ == '__main__':
    user = User(name='98k', pw='123')
    print(user.get_name)
    user.get_name = 'o98k'
    print(user.get_name)


"""
    @property           属性描述符，将对象内部的方法转换成计算属性，也就是直接通过 对象.函数名 取值
    @get_name.setter    修改属性值

"""
