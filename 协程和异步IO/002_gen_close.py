# Author: O98K


def generator_func():
    # 1.可以产出值
    # 2.可以接收值(调用方传递进来的值)
    try:
        yield "http://www.baidu.com"
    except BaseException:
        pass
    # yield 2
    # yield 3
    return "end"


if __name__ == "__main__":
    generator = generator_func()
    print('return data ===>>>', next(generator))
    generator.close()
    print("gen closed")

    # GeneratorExit是继承自BaseException， Exception
