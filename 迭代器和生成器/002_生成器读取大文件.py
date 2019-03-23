# Author: O98K

# 读取大文件时获取到的 f文件句柄中，可指定read(x) x 为偏移量


def readlines(f, newline):
    buf = ''
    while True:
        while newline in buf:
            pos = buf.index(newline)
            yield buf[:pos]
            buf = buf[pos + len(newline):]

        chunk = f.read(4096)
        if not chunk:
            # 读取到文件末尾
            yield buf
            break
        buf += chunk


def readfile(path, newline_flag):
    with open(path) as f:
        for line in readlines(f, newline_flag):
            print(line.strip('\n'))


if __name__ == '__main__':
    import os
    path = os.path.join(os.path.dirname(__file__), 'test.txt')
    newline_flag = '{|}'
    readfile(path, newline_flag)
