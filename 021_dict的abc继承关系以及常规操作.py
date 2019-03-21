# Author: O98K

from collections.abc import Mapping, MutableMapping

# dict 属于 mapping 类型

temp = {}
# temp 属于 dict 类型，但是不是继承 MutableMapping 只是实现了内部的某些方法
# MutableMapping.register(dict)
print(isinstance(temp, MutableMapping))

# 1.clear
temp_dict = {'name': 'a', 'age': 18, 'company': {'name': 'ss'}}

# 2.dict 中的 copy 为浅拷贝
# 浅拷贝 简单的说只是 将新变量的地址指向了原来的对象，原来的对象值修改，新变量值获取的值变成相应的值
temp_dict2 = temp_dict.copy()
temp_dict['company']['name'] = 'b'
print(temp_dict2)  # {'name': 'a', 'age': 18, 'company': {'name': 'b'}}

# 3.formkeys
# 通过get 方法取值

# 4.setdefault
# 如果存在，则取出返回该值，如果不存在则添加并且返回该值
setdefault_value = temp_dict.setdefault('gender', 'male')
print(setdefault_value)
print(temp_dict.setdefault('name', '55'))
print(temp_dict)

# 5.update
temp_dict.update(address='sss')

print(temp_dict)
