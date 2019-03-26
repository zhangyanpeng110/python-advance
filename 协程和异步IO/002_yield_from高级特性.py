# Author: O98K

# python3.3新加了yield from语法
my_list = [1, 2, 3]
my_dict = {
    "url_1": "http://projectsedu.com",
    "url_2": "http://www.imooc.com",
}


def my_chain(*args, **kwargs):
    for my_iterable in args:
        yield from my_iterable
        # for value in my_iterable:
        #     yield value


for value in my_chain(my_list, my_dict.items(), range(5, 10)):
    print(value)


# def g1(gen):
#     yield from gen
#
#
# def main():
#     g = g1(my_list)
#     g.send(None)


# 1.main 调用方 g1(委托生成器) gen 子生成器
# 2.yield from会在调用方与子生成器之间建立一个双向通道


def sales_sum(pro_name):
    total = 0
    nums = []
    while True:
        x = yield
        print(pro_name + "销量: ", x)
        if not x:
            break
        total += x
        nums.append(x)
    return total, nums


if __name__ == "__main__":
    my_gen = sales_sum("手机")
    my_gen.send(None)   # 启动生成器
    my_gen.send(1200)
    my_gen.send(1500)
    my_gen.send(3000)

    # 不使用 yield from 则需要开发者自己处理 StopIteration 异常
    try:
        # 发送None关闭
        my_gen.send(None)
    except StopIteration as e:
        result = e.value
        print(result)
