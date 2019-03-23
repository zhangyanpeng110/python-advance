# Author: O98K
from queue import Queue

import time
import threading


def get_detail_html(queue):
    """
    爬取文章详情页
    :param queue:
    :return:
    """
    while True:
        url = queue.get()
        # for url in detail_url_list:
        print("get detail html started")
        time.sleep(2)
        print("get detail html end")
        if queue.empty():
            break


def get_detail_url(queue):
    """
    爬取文章列表页
    :param queue:
    :return:
    """
    while True:
        print("get detail url started")
        time.sleep(2)
        for i in range(20):
            queue.put("http://projectsedu.com/{id}".format(id=i))
            print("get_detail_url ===>>> http://projectsedu.com/{id}".format(id=i))
        print("get detail url end")
        break


if __name__ == '__main__':
    detail_url_queue = Queue(maxsize=100)
    url_thread = threading.Thread(target=get_detail_url, args=(detail_url_queue,))
    url_thread.start()
    for i in range(50):
        html_thread = threading.Thread(target=get_detail_html, args=(detail_url_queue,))
        html_thread.start()

    start_time = time.time()

    """
    线程间通信方式：
        1.共享全局变量
            弊端：需要处理锁的获取和释放，否则会出现共享变量错乱等不可控的情况
        2.线程池
            线程池是线程安全的，自动阻塞，实际底层使用时 cpython 中的双端队列 deque
            所以继承了 deque 本身具有的线程安全机制
            1)queue中的get方法使得当队列里面没有对象时，发生阻塞
            2)queue中的put方法使得当队列已满的情况下发生阻塞，等到队列有空间的时候才 put
            3)queue还提供了判断队列是否为空、为满的方法
            4)task_down 方式实现 退出主线程
    """

    # 需要在某个地方调用 task_done 方法才会执行下面的 join 退出
    # detail_url_queue.task_done()
    detail_url_queue.join()

    # 当主线程退出的时候， 子线程kill掉
    print("last time: {}".format(time.time() - start_time))
