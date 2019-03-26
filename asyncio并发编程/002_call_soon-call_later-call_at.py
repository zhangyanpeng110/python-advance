# Author: O98K

import asyncio


def callback(times, loop):
    print("sleep time ===>>>{0}, loop time ===>>>{1}".format(times, loop.time()))


def stoploop(loop):
    loop.stop()


# call_later, call_at, call_soon
if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    now = loop.time()
    # 指定时间调用
    loop.call_at(now + 4, callback, 2, loop)
    loop.call_at(now + 5, callback, 1, loop)
    loop.call_at(now + 6, callback, 3, loop)

    # 立即调用
    # loop.call_soon(stoploop, loop)
    loop.call_soon(callback, 4, loop)
    # 延时一定时间后调用
    loop.call_later(5, callback, 3, loop)

    loop.run_forever()
