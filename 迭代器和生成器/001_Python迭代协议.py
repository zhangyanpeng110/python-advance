# Author: O98K

"""
    迭代协议：
        1.可迭代类型     Iterable        可通过 for 等循环方式取值
        2.迭代器        Iterator

    迭代器是访问集合内元素的一种方式
        一般用来遍历数据，访问数据的方式与通过下标、索引访问的方式不一样
        迭代器不能返回，也就是说只能从前往后读取，不能返回读取之前的元素它提供了一种惰性方式访问数据的方式

    调用 for 循环的时候，实际上是调用了 魔法函数iter

**********************************************************************
    生成器函数：
        1.函数里只要存在 yield
        2.返回的是一个生成器对象，为惰性求职，延迟求值提供了可能

    原理：
        每次返回、退出都保存了当前状态，只要拿到栈帧就能返回到上一次执行的位置继续执行

    应用场景：


"""

import inspect
frame = None
def func():
    func2()


def func2():
    global frame
    frame = inspect.currentframe()


# python.exe 使用 PyEval_EvalFramEx(c函数)去执行 func 函数
# 1.首先创建一个栈帧
#   Python中一切皆对象指的是 栈帧对象、字节码对象
#   当 func 调用子函数 func2 ，优惠创建一个栈帧，所有的栈帧都分配到堆内存上，所以这就决定了
#   调用者而存在，
import dis

print(dis.dis(func))
"""
 30           0 LOAD_GLOBAL              0 (func2)
              2 CALL_FUNCTION            0
              4 POP_TOP
              6 LOAD_CONST               0 (None)
              8 RETURN_VALUE
None
"""
func()
print(frame.f_code.co_name)
caller_frame = frame.f_back
print(caller_frame.f_back)
"""
func2
<frame object at 0x000001F90BEE8E58>
"""