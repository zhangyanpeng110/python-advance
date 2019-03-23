# Author: O98K

from threading import Lock, RLock
from threading import Thread


count = 10
# lock = Lock()
lock = RLock()


def add():
    global count
    global lock
    for i in range(1000000):
        lock.acquire()
        count += 1
        lock.release()


def desc():
    global count
    global lock
    for i in range(1000000):
        # RLock 使得在一个线程里面，可以连续调用 acquire，但是一定要注意 acquire的次数必须和 release 的次数相对应，避免线程死锁
        lock.acquire()
        # lock.acquire()
        count -= 1
        # lock.release()
        lock.release()


if __name__ == '__main__':
    add_thread = Thread(target=add)
    desc_thread = Thread(target=desc)

    add_thread.start()
    desc_thread.start()

    add_thread.join()
    desc_thread.join()

    print(count)


"""
    优点：
        实现线程安全，避免数据混乱
    缺点：
        1)获取、释放锁耗费性能
        2)容易造成死锁   
            lock.acquire() 之后会将其它线程锁死，直到 lock.release()
            如果 获取锁之后不及时释放会造成死锁
     
    解决：
        Python 提供 RLock        
        RLock 使得在一个线程里面，可以连续调用 acquire，但是一定要注意 acquire的次数必须和 release 的次数相对应
        

"""