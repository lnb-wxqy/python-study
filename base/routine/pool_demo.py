# Pool
# 如果要启动大量的子进程，可以使用进程池的方式批量创建子进程

from multiprocessing import Pool
import os, time, random


def long_time_task(name):
    print("Run task %s (%s)" % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s run %0.2f senconds.' % (name, (end - start)))


if __name__ == '__main__':
    print('Parent process %s.' % os.getpid())
    p = Pool(4)
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))
    print('Waiting for all subprocess done...')
    p.close()
    p.join()
    print('All subprocess done.')

# 运行结果
# Parent process 19088.
# Waiting for all subprocess done...
# Run task 0 (8748)
# Run task 1 (23384)
# Run task 2 (22640)
# Run task 3 (22456)
# Task 3 run 0.09 senconds.
# Run task 4 (22456)
# Task 2 run 0.18 senconds.
# Task 0 run 0.96 senconds.
# Task 1 run 1.43 senconds.
# Task 4 run 1.47 senconds.
# All subprocess done.

# 代码解读：
# Pool对象调用join()方法会等待所有子进程执行完毕，调用join()之前必须调用close(),调用close()之后就不能继续添加新的process了
# 请注意输出的结果，task 0，1，2，3是立刻执行的，而task 4要等待前面某个task完成后才执行，这是因为Pool的默认大小在我的电脑上是4，
# 因此，最多同时执行4个进程。这是Pool有意设计的限制，并不是操作系统的限制。如果改成：
# p = Pool(5)， 就可以同时跑5个进程。
# 由于Pool的默认大小是CPU的核数，如果你不幸拥有8核CPU，你要提交至少9个子进程才能看到上面的等待效果。
