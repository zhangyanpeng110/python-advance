# Author: O98K
import threading
import time
from threading import RLock
import variables
# 如果直接导入 from variables import detail_url_list 时，多线程情况下会导致在不同的此线程间的使用时 隔离的


# 生产者 和 消费者 的概念
# 1. 生产者当生产10个url以后就就等待，保证detail_url_list中最多只有十个url
# 2. 当url_list为空的时候，消费者就暂停

def get_detail_html(lock):
    detail_url_list = variables.detail_url_list
    while True:

        if len(variables.detail_url_list):
            lock.acquire()
            if len(detail_url_list):
                url = detail_url_list.pop()
                lock.release()
                # for url in detail_url_list:
                print("get detail html start...")
                time.sleep(2)
                print("get detail html end...")
            else:
                lock.release()
                time.sleep(1)


def get_detail_url(lock):
    detail_url_list = variables.detail_url_list
    while True:
        print("get detail url start...")
        time.sleep(4)
        for i in range(20):
            lock.acquire()
            if len(detail_url_list) >= 10:
                lock.release()
                time.sleep(1)
            else:
                detail_url_list.append("http://projectsedu.com/{id}".format(id=i))
                lock.release()
        print("get detail url end...")


# 1. 线程通信方式- 共享变量

if __name__ == "__main__":
    lock = RLock()
    url_thread = threading.Thread(target=get_detail_url, args=(lock,))
    url_thread.start()
    for i in range(10):
        html_thread = threading.Thread(target=get_detail_html, args=(lock,))
        html_thread.start()
    # # thread2 = GetDetailUrl("get_detail_url")
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

    # url_thread.join()
    # html_thread.join()

    print('use tine ===>>>', time.time() - start_time)
