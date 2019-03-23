# Author: O98K
# import os
# #fork只能用于linux/unix中
# pid = os.fork()
# print("bobby")
# if pid == 0:
#   print('子进程 {} ，父进程是： {}.' .format(os.getpid(), os.getppid()))
# else:
#   print('我是父进程：{}.'.format(pid))

import multiprocessing
import time


def get_html(times):
    time.sleep(times)
    print('sub_progress success...')
    return str(times)


if __name__ == '__main__':
    """
        进程间的数据是隔离的，子进程中的数据会由父进程中复制过来，所以在多进程通信中无法通过
        多线程通信中的共享全局变量的方法实现
    """
    # 创建进程
    # get_html_progress = multiprocessing.Process(target=get_html, args=(2,))
    # get_html_progress.start()
    # print(get_html_progress.pid)
    # get_html_progress.join()
    # print("main progress end...")

    # 使用线程池
    print("get cpu count ===>>>", multiprocessing.cpu_count())
    pool = multiprocessing.Pool(multiprocessing.cpu_count())
    # 创建进程时，参数必须能够被pickle，所以有些自定义的类对象实例是不能被作为参数的
    result = pool.apply_async(get_html, args=(3, ))

    print(result.get())

    # 等待所有任务执行完成
    # join 之前 必须先 close
    pool.close()
    pool.join()

    # imap 输出最先执行完的，而不按执行的顺序进行输出
    # for result in pool.imap(get_html, [1,5,3]):
    #     print("{} sleep success".format(result))

    # for result in pool.imap_unordered(get_html, [1,5,3]):
    #     print("{} sleep success".format(result))
