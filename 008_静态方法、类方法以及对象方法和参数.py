# Author: O98K


class Date(object):
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def tomorrow(self):
        self.day += 1

    @staticmethod
    def get_year():
        pass

    @classmethod
    def set_year(cls, year):
        cls.year = year

    def __str__(self):
        return "{year}-{month}-{day}".format(year=self.year, month=self.month, day=self.day)


if __name__ == '__main__':
    new_date = Date(2019, 3, 16)
    new_date.tomorrow()
    print(new_date)

    # print((1, (2, 3)))
    # print(type((1)))

    # 1.对象方法

    # 2.静态方法   @staticmethod

    # 3.类方法     @classmethod


