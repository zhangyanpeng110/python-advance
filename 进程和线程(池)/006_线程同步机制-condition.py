# Author: O98K

from threading import Thread
from threading import Condition


class A(Thread):
    def __init__(self, condition):
        super().__init__(name='A')
        self.condition = condition

    def run(self):
        with self.condition:
            print("{} : 收到你唤醒的锁了，谢谢你!现在我使用完了并且唤醒了你给我的锁，记得获取哟！！！ ".format(self.name))
            self.condition.notify()
            self.condition.wait()

            print("{} : 才不呢，就聊会儿天好吗？？？ ".format(self.name))
            self.condition.notify()
            self.condition.wait()


class B(Thread):
    def __init__(self, condition):
        super().__init__(name='B')
        self.condition = condition

    def run(self):
        with self.condition:
            print("{} : 我唤醒的一把锁 ".format(self.name))
            self.condition.notify()
            self.condition.wait()

            print("{} : 收到你唤醒的锁了，不客气！现在我们来开始 嘿嘿嘿 好不好？？？ ".format(self.name))
            self.condition.notify()
            self.condition.wait()


if __name__ == '__main__':
    condition = Condition()
    A_thread = A(condition)
    B_thread = B(condition)

    # 启动顺序很重要
    # 1.在调用with condition 之后才能调用wait或者notify方法
    # 2.condition有两层锁
    #   一把底层锁会在线程调用了wait方法的时候释放
    #   上面的锁会在每次调用wait的时候分配一把并放入到condition的等待队列中，等到notify方法的唤醒
    B_thread.start()
    A_thread.start()

    B_thread.join()
    A_thread.join()
