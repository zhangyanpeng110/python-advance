# Author: O98K

import bisect

# 维护已排序的序列
# 内部实现机制    二分查找


list_ = [0, 2, 5]
bisect.insort(list_, 1)
bisect.insort(list_, 100)
bisect.insort(list_, 30)

print(list_)

# collections 中可实现双端队列
from collections import deque
