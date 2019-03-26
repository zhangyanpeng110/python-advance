# Author: O98K

def generator_func():
    # 1.可以产出值
    # 2.可以接收值(调用方传递进来的值)   实现协程的基础
    try:
        data = yield "http://www.baidu.com"
    except BaseException:
        pass

    yield "yield通过send方法传递的数据===>>>{}".format(data)
    yield 3
    return "end"


if __name__ == "__main__":
    generator = generator_func()

    # 1.next 方法启动生成器
    # print('next 方法启动生成器 ===>>>', next(generator))

    # 2.send 方法启动生成器
    generator.send(None)
    print('send 方法传递data ===>>>', generator.send('send data'))

    # 关闭生成器之后，再调用next()
    # 报错 StopIteration

    print("gen closed")
