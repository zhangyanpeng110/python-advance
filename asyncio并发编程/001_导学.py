# Author: O98K

"""
    事件循环+回调（驱动生成器）+epoll(IO多路复用)
    asyncio 是 Python用于解决异步io编程的一整套解决方案
    tornado、gevent、twisted(scrapy, django channels)
    torando(实现web服务器), django+flask(uwsgi, gunicorn+nginx)
    tornado可以直接部署, 不过通常以：nginx+tornado进行部署

"""

import asyncio
import time
from functools import partial


async def get_html(url):
    print('start get {}'.format(url))
    # time.sleep(2)
    await asyncio.sleep(2)
    return url


def callback(url, future):
    print(url)
    print("send email to 98K")


if __name__ == '__main__':
    start_time = time.time()

    loop = asyncio.get_event_loop()
    # get_future = asyncio.ensure_future(get_html('https://www.baidu.com'))
    # print(get_future.result())

    # task 和 ensure_future 差别不大
    # 最后实现的都是 将协程注册到 loop 中
    task = loop.create_task(get_html('https://www.baidu.com'))
    task.add_done_callback(partial(callback, 'https://www.baidu.com'))
    loop.run_until_complete(task)
    print(task.result())

    print(time.time() - start_time)
