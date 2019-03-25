# Author: O98K
import socket
import time
from urllib.parse import urlparse
from selectors import DefaultSelector, EVENT_READ, EVENT_WRITE

"""
    优点：
        单线程下实现，效率高
    缺点：
        1.可读性差
        2.异常处理困难
        3.共享状态管理困难
"""

selector = DefaultSelector()
urls = []
stop_flag = False


class Fetcher(object):
    def connected(self, key):
        selector.unregister(key.fd)
        self.client.send(
            "GET {} HTTP/1.1\r\nHost:{}\r\nConnection:close\r\n\r\n".format(self.path, self.host).encode("utf8"))
        selector.register(self.client.fileno(), EVENT_READ, self.readable)

    def readable(self, key):
        d = self.client.recv(1024)
        if d:
            self.data += d
        else:
            selector.unregister(key.fd)
            data = self.data.decode("utf8")
            html_data = data.split("\r\n\r\n")[1]
            print(html_data)
            self.client.close()
            urls.remove(self.spider_url)
            if not urls:
                global stop
                stop = True

    def get_url(self, url):
        self.spider_url = url
        url = urlparse(url)
        self.host = url.netloc
        self.path = url.path
        self.data = b""
        if self.path == "":
            self.path = "/"

        # 建立socket连接
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 设置 非阻塞 setblocking(False)
        self.client.setblocking(False)

        try:
            self.client.connect((self.host, 80))  # 阻塞不会消耗cpu
        except BlockingIOError as e:
            # import traceback
            # traceback.format_exc()
            pass

        # 注册
        # print('self.client.fileno ===>>>', self.client.fileno())
        selector.register(self.client.fileno(), EVENT_WRITE, self.connected)


def loop():
    """
        事件循环，不停的请求socket的状态并调用对应的回调函数
            1.selecter 本身不支持 register 模式
            2.socket 状态变化以后的回调是有开发者完成的===并不是自动回调
        回调 + 事件循环 + select/poll/epoll
    :return:
    """
    while not stop_flag:
        ready = selector.select()
        # print("ready ===>>>", ready)
        for key, mask in ready:
            call_back = key.data
            call_back(key)


if __name__ == '__main__':
    fetcher = Fetcher()
    start_time = time.time()
    for url_id in range(1, 21):
        url = "http://shop.projectsedu.com/goods/{url_id}/".format(url_id=url_id)
        urls.append(url)
        fetcher = Fetcher()
        fetcher.get_url(url)
    loop()
    print('use time ===>>>', time.time() - start_time)

    # f1 = Fetcher()
    # f2 = Fetcher()
    # print(id(f1))
    # print(id(f2))

"""
    Windows环境下会报错：
          File "d:\python36\Lib\selectors.py", line 314, in _select
            r, w, x = select.select(r, w, w, timeout)
        OSError: [WinError 10022] 提供了一个无效的参数。
"""