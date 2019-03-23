# Author: O98K

"""
    GIL 的存在使得Python无法利用多线程的优势

    多进程、多线程的比较：
        1.耗CPU的操作，使用多进程优势更大     计算类型
        2.IO操作，使用多线程编程
        3.进程的切换代价大于线程的切换

"""

import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from concurrent.futures import ProcessPoolExecutor


def fib(n):
    if n <= 2:
        return 1
    return fib(n - 1) + fib(n - 2)


def random_sleep(n):
    time.sleep(n)
    return n


if __name__ == "__main__":
    # 1.耗CPU的操作 对比
    # Windows 环境下，实现多进程，需要将执行代码放在 if __name__ == "__main__": 中执行
    # with ProcessPoolExecutor(3) as executor:          # last time is: 18.88746976852417
    # with ThreadPoolExecutor(3) as executor:  # last time is: 37.611387968063354
    #     all_task = [executor.submit(fib, (num)) for num in range(25, 40)]
    #     start_time = time.time()
    #     for future in as_completed(all_task):
    #         data = future.result()
    #         print("exe result: {}".format(data))
    #
    #     print("last time is: {}".format(time.time() - start_time))

    # 2.IO操作 测试
    # with ProcessPoolExecutor(3) as executor:      # last time is: 20.16511583328247
    with ThreadPoolExecutor(3) as executor:         # last time is: 20.006487607955933
        all_task = [executor.submit(random_sleep, (num)) for num in [2] * 30]
        start_time = time.time()
        for future in as_completed(all_task):
            data = future.result()
            print("exe result: {}".format(data))

        print("last time is: {}".format(time.time() - start_time))
