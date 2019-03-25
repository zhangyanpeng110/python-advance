# Author: O98K
import time
import asyncio
import socket
from urllib.parse import urlparse


async def get_url(url):
    """
        创建协程，并通过socket请求HTML
    :return:
    """
    url = urlparse(url=url)
    host = url.netloc
    path = url.path
    if path == "":
        path = "/"

    # 建立socket连接
    reader, writer = await asyncio.open_connection(host=host, port=80)
    """
        reader = StreamReader(limit=limit, loop=loop)
        writer = StreamWriter(transport, protocol, reader, loop)
    """
    writer.write("GET {} HTTP/1.1\r\nHost:{}\r\nConnection:close\r\n\r\n".
                 format(path, host).encode("utf8"))
    all_lines = []
    async for raw_line in reader:
        data = raw_line.decode('utf-8')
        all_lines.append(data)
    html_text = "".join(all_lines)
    return html_text


async def main():
    """
        创建协程
    :return:
    """
    tasks = []
    for url in range(1, 20):
        url = "http://shop.projectsedu.com/goods/{}/".format(url)
        tasks.append(asyncio.ensure_future(get_url(url=url)))
    for task in asyncio.as_completed(tasks):
        result = await task

        print(result)


if __name__ == '__main__':
    start_time = time.time()
    # 创建事件循环
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())

    print("task completed, use time ===>>> {}".format(time.time() - start_time))
