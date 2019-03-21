# Author: O98K

# 列表生成器
# 性能高于列表操作，但局限于内部逻辑比较简单的，否则代码的可读性不高
# 列表生成式，第一：能用尽量用， 因为效率高
temp = [1, 5, 6, 40, 2, 3, 50]
res = [i for i in temp if i % 2 == 0]
print(res)

# 生成器表达式
# [] 变成 ()
gen = (i for i in temp if i % 2 == 0)
print(gen)  # <generator object <genexpr> at 0x000002A21A48B888>

# 字典推导式
temp_dict = {"name": "z", "gender": "male"}
res_dict = {value: key for key, value in temp_dict.items()}
print(res_dict)


# 集合推导式        无序
temp_set = {key for key, value in temp_dict.items()}
print(type(temp_set))

