# Author: O98K

"""
    全局解释器锁 global interpreter lock

    Python 中的一个线程 对应 C语言中的一个线程
    GIL使得同一时刻，在一个CPU上只有一个线程执行字节码，无法将多个线程映射到多个CPU上执行

"""

# import dis
#
#
# def add(value):
#     value = value + 1
#     return value
#
#
# print(dis.dis(add))

import threading

value = 0


def add():
    global value
    for i in range(1000000):
        value += 1


def desc():
    global value
    for i in range(1000000):
        value -= 1


add_thread = threading.Thread(target=add)
desc_thread = threading.Thread(target=desc)
add_thread.start()
desc_thread.start()

add_thread.join()
desc_thread.join()

print(value)
"""
    可以看出 
        1.GIL会根据执行的字节码行数以及时间片释放GIL
        2.遇到IO操作的时候主动释放

"""


