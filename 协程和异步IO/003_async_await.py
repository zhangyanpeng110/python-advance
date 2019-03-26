# Author: O98K
# python为了将语义变得更加明确，就引入了async和await关键词用于定义原生的协程

import types


@types.coroutine
def downloader(url):
    yield url


async def download_url(url):
    html = await downloader(url)
    return html


if __name__ == "__main__":
    coro = download_url("http://www.baidu.com")
    # 不能使用 next() 启动，是能使用 send()
    print('await data ===>>>', coro.send(None))


