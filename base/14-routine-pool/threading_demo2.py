# 多线程锁

# 不加锁示例
import time, threading

balance = 0
lock = threading.Lock()


def change_it(n):
    global balance
    balance = balance + n
    balance = balance - n


# 加锁
def run_thread(n):
    for i in range(200000):
        # 先获取锁
        lock.acquire()
        try:
            change_it(n)
        finally:
            # 改完后释放锁
            lock.release()


t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(9,))

t1.start()
t2.start()

t1.join()
t2.join()
print(balance)

# 代码解释：
'''
我们定义了一个共享变量balance，初始值为0，并且启动两个线程，先存后取，理论上结果应该为0，但是，
由于线程的调度是由操作系统决定的，当t1、t2交替执行时，只要循环次数足够多，balance的结果就不一定是0了。
'''
