# Author: O98K

def gen_func():
    # 1. 可以产出值， 2. 可以接收值(调用方传递进来的值)
    try:
        yield "https://www.baidu.com/"
    except Exception as e:
        pass
    yield 2
    yield 3
    return "bobby"


if __name__ == "__main__":
    gen = gen_func()
    next(gen)
    gen.throw(Exception, "download error")
    print(next(gen))
    # gen.throw(Exception, "download error")
