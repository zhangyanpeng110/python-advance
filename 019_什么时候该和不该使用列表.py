# Author: O98K

"""
    array

    deque

补充概念：
    数组：
        地址是连续的，读写性能高
    链表：
        地址非连续性，每个元素后面会指定下一个元素的地址
"""
import array

# array和list的区别：array 只能存放指定的数据类型

# 创建的时候指定类型
my_array = array.array('i')
my_array.append(10)

my_array.append('a')
# TypeError: an integer is required (got type str)

print(my_array)
