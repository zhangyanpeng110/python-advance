# Author: O98K

# 列表操作

a = [2, 5]

# += 符号 添加的对象不一定需要时列表
a += (1, 3)
print(a)

# extend 方法 内部调用 魔法函数 __iadd__ 所以是将对象中的每个元素循环添加到列表中
"""
    def __iadd__(self, *args, **kwargs): # real signature unknown
"""
a.extend(range(2))
print(a)

# append 直接将对象添加到列表中
a.append(range(2))
print(a)


import numbers
class Group:
    #支持切片操作
    def __init__(self, group_name, company_name, staffs):
        self.group_name = group_name
        self.company_name = company_name
        self.staffs = staffs

    def __reversed__(self):
        self.staffs.reverse()

    def __getitem__(self, item):
        cls = type(self)
        if isinstance(item, slice):
            return cls(group_name=self.group_name, company_name=self.company_name, staffs=self.staffs[item])
        elif isinstance(item, numbers.Integral):
            return cls(group_name=self.group_name, company_name=self.company_name, staffs=[self.staffs[item]])

    def __len__(self):
        return len(self.staffs)

    def __iter__(self):
        return iter(self.staffs)

    def __contains__(self, item):
        if item in self.staffs:
            return True
        else:
            return False


staffs = ["A", "V", "B", "Z"]
group = Group(company_name="ZG", group_name="user", staffs=staffs)
reversed(group)

# __contains__ 实现可判断对象中是否存在 某个元素 也就是使用 in 方法
for user in group:
    print(user)