# Author: O98K

from concurrent.futures import ThreadPoolExecutor, as_completed, wait, FIRST_COMPLETED
from concurrent.futures import Future
from multiprocessing import Pool
import time

"""
    futures 未来对象，task 的返回容器
    线程池的出现：
        使得主线程中可以获取到某一个线程的状态或者某一个任务的状态和返回值
        futures 使得 多线程、多进程、携程 的编码接口、设计理念一致
"""


def get_html(times):
    time.sleep(times)
    print('get page {} success'.format(times))
    return times


executor = ThreadPoolExecutor(max_workers=3)

# 1.使用 submit 提交执行的函数到线程池中， submit 是立即返回
task1 = executor.submit(get_html, (3))
task2 = executor.submit(get_html, (4))

# done 方法判断某个任务是否执行完毕
# print(task1.done())

# result 方法获取 task 执行的结果
# print(task1.result())

# cancel 取消任务，前提是任务状态处于：RUNNING, FINISHED
# if self._state in [RUNNING, FINISHED]:
#     return False
task3 = executor.submit(get_html, (5))
print(task3.cancel())

# 2.获取已经成功的 task 的返回值
urls = [3, 4, 2]
all_task = [executor.submit(get_html, (url, )) for url in urls]

# wait 方法使得可指定 task 是否执行完等情况之后才执行后面的 逻辑
wait(all_task, return_when=FIRST_COMPLETED)

print('wait 指定的task 已执行完毕')






