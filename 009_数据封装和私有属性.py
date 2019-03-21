# Author: O98K


class User:
    def __init__(self, birthday):
        self.__birthday = birthday

    def get_birthday(self):
        return self.__birthday


if __name__ == "__main__":
    user = User('1990-02-01')
    # 虽然是内置属性，原则上是不提供给外部访问，外部也无法访问到的
    # 但可通过其它方式访问，所以 并没有绝对的安全，只是这种定义方式是约定俗成的而已
    print(user._User__birthday)
    print(user.get_birthday())
