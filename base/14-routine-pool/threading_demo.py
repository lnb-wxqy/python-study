# 多线程
# Python的标准库提供了两个模块：_thread和threading，_thread是低级模块，threading是高级模块，
# 对_thread进行了封装。绝大多数情况下，我们只需要使用threading这个高级模块。
import time, threading


# 子线程要执行的代码
def loop():
    print('thread %s is running....' % threading.current_thread().name)
    n = 0
    while n < 5:
        n = n + 1
        print('thread %s>>> %s' % (threading.current_thread().name, n))
        time.sleep(1)  # 单位：seconds
    print('thread %s end' % threading.current_thread().name)


print('thread %s is running...' % threading.current_thread().name)
t = threading.Thread(target=loop, name='loopThread')
t.start()
t.join()
print('thread %s end' % threading.current_thread().name)
