# Author: O98K

"""
    信号量
    Semaphore 控制进入数量的锁
    文件的读、写  写一般只用一个线程写，读可使用多个线程实现

    阅读源码可以看出，实际上Semaphore底层调用的还是Condition()
"""

import time
from threading import Semaphore, Thread


class HtmlSpider(Thread):
    def __init__(self, url, semaphore):
        super().__init__(name='HtmlSpider')
        self.url = url
        self.semaphore = semaphore

    def run(self):
        time.sleep(1)
        print('get html text from {url}'.format(url=self.url))
        # 抓取完之后释放
        self.semaphore.release()


class UrlControl(Thread):
    def __init__(self, semaphore):
        super().__init__(name='UrlControl')
        self.semaphore = semaphore

    def run(self):
        for i in range(20):
            # 获取锁
            self.semaphore.acquire()
            html_thread = HtmlSpider("url_{id}".format(id=str(i)), self.semaphore)
            html_thread.start()


if __name__ == '__main__':
    # 指定信号量
    # 没获取完信号之后将会等待，直到被获取的被释放之后
    semaphore = Semaphore(3)
    urlcontrol = UrlControl(semaphore)
    urlcontrol.start()





