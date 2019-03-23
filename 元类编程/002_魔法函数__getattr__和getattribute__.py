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

    def __getattr__(self, item):
        """
        查找不到该属性时，触发执行
        可灵活添加逻辑处理异常
        :param item:
        :return:
        """
        return "not find attr"

    def __getattribute__(self, item):
        """
        无条件返回 指定的返回值，如果函数内有指定的话
        常在框架中使用，强制限制必须返回指定值
        :param item:
        :return:
        """
        return 'default return'


if __name__ == '__main__':
    user = User(name='98k', pw='123')
    # __getattr__ 在查找不到属性时触发执行，而不会抛出查找不到该属性的错误
    print(user.age)

