# Author: O98K


# try:
#     print('code start')
# except:
#     print('key error')
# else:
#     # try 内不存在异常
#     print('not error')
# finally:
#     # 不管存不存在异常，都会执行该语句
#     print('whatever true pr not!')

"""
    with 实际上就是简化 try except 语句
    
    上下文管理器的实现机制 就是通过使用 with 语句
    
    涉及魔法函数：
        __enter__
        __exit__
"""


class Simple(object):
    def __enter__(self):
        # 进入
        print('获取资源')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        # 退出
        print('退出，释放资源...')

    def do_something(self):
        print('实现其它功能')


with Simple() as simple:
    simple.do_something()
