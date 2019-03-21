# Author: O98K

import contextlib


# 1.通过装饰器 将函数变成上下文管理器
@contextlib.contextmanager
def read_file(file_path):
    print('open file')
    yield {}
    print('close file')


with read_file('笔记.txt') as f:
    print(f)
