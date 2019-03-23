# Author: O98K

"""
    操作系统调度的  最小单元是能是线程
    对于IO操作来说，多线程和多进程性能差别不大

"""
# 1.代码逻辑比较简单时，通过 Thread 类实例化
# 2.代码逻辑比较复杂时，通过面向对象的思想继承 Thread 对象

import threading
import time


def get_detail_html(url):
    print('get detail html start...')
    time.sleep(2)
    print('get detail html end...')


def get_detail_url(url):
    print('get detail url start...')
    time.sleep(2)
    print('get detail url end...')


class GetDetailHtml(threading.Thread):
    def __init__(self, name):
        super().__init__(name=name)

    def run(self):
        print('get detail html start...')
        time.sleep(2)
        print('get detail html end...')


class GetDetailUrl(threading.Thread):
    def __init__(self, name):
        super().__init__(name=name)

    def run(self):
        print('get detail html start...')
        time.sleep(4)
        print('get detail html end...')


if __name__ == '__main__':
    # 实例化 Thread 方法 实现方式
    # html_thread = threading.Thread(target=get_detail_html, args=('',))
    # url_thread = threading.Thread(target=get_detail_url, args=('',))

    # 继承 Thread 类 方法实现方式
    html_thread = GetDetailHtml("get_detail_html")
    url_thread = GetDetailUrl("get_detail_url")

    # html_thread.setDaemon(True)
    # url_thread.setDaemon(True)

    start_time = time.time()
    print('start time ===>>>', start_time)
    html_thread.start()
    url_thread.start()

    # 2.等待子线程执行完，发生阻塞
    html_thread.join()
    url_thread.join()

    # join 使得主线程在等待子线程执行完之后才执行
    print('use tine ===>>>', time.time() - start_time)
    # 实际上产生了三个线程：主线程、html线程、url线程

"""
    注意：
    1.如果将子线程设置为守护进程则当主线程退出时会义无反顾地关闭子线程，即使子线程未执行完毕    
    2.使用 join 方法使得主线程等待子线程执行完毕之后才执行 join 之后的代码
    
"""
