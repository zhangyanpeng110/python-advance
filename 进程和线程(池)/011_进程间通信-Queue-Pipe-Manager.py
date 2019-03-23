# Author: O98K
import time
from multiprocessing import Process, Queue, Pool, Pipe, Manager


# def producer(a):
#     a += 100
#     time.sleep(2)
#     print('producer 中的a值 ===>>>', a)
#
#
# def consumer(a):
#     time.sleep(2)
#     print('进程间的数据是隔离的，所以consumer 中的a值不随着producer中的改变而改变 ===>>>', a)
#
#
# if __name__ == "__main__":
#     # 1.验证多进程中无法使用共享变量的方式实现进程间通信
#     a = 1
#     my_producer = Process(target=producer, args=(a,))
#     my_consumer = Process(target=consumer, args=(a,))
#     my_producer.start()
#     my_consumer.start()
#     my_producer.join()
#     my_consumer.join()


# def producer(queue):
#     queue.put("from producer")
#     time.sleep(2)
#
#
# def consumer(queue):
#     time.sleep(2)
#     data = queue.get()
#     print('consumer get data from queue ===>>>', data)
#
#
# if __name__ == "__main__":
#     # 2.multiprocessing中的queue不能用于pool进程池
#     #   pool中的进程间通信需要使用manager中的Queue
#     queue = Manager().Queue(10)
#     pool = Pool(2)
#
#     pool.apply_async(producer, args=(queue,))
#     pool.apply_async(consumer, args=(queue,))
#
#     pool.close()
#     pool.join()


# def producer(send_pipe, recevie_pipe):
#     send_pipe.send("send message from producer")
#     time.sleep(2)
#     print(recevie_pipe.recv())
#
#
# def consumer(send_pipe, recevie_pipe):
#     print(recevie_pipe.recv())
#
#     send_pipe.send("send message from consumer")
#
#
# if __name__ == "__main__":
#     # 3.通过pipe实现进程间通信
#     # pipe的性能高于queue，因为queue中存在锁的操作，耗费了部分资源
#     recevie_pipe, send_pipe = Pipe()
#     # pipe只能适用于两个进程
#     producer_process = Process(target=producer, args=(send_pipe, recevie_pipe))
#     consumer_process = Process(target=consumer, args=(send_pipe, recevie_pipe,))
#
#     producer_process.start()
#     consumer_process.start()
#     producer_process.join()
#     consumer_process.join()


def add_user(progress_list, userinfo):
    progress_list.append(userinfo)


if __name__ == "__main__":
    # 4.Manager实现进程间的通信     内存共享
    progress_list = Manager().list()
    from queue import PriorityQueue

    first_progress = Process(target=add_user, args=(progress_list, {'name': 'user_a', 'age': 18}))
    second_progress = Process(target=add_user, args=(progress_list, {'name': 'user_b', 'age': 20}))

    first_progress.start()
    second_progress.start()
    first_progress.join()
    second_progress.join()

    print(progress_list)
