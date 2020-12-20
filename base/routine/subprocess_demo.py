# 子进程
# subprocess模块可以让我们非常方便地启动一个子进程，然后控制其输入和输出。
# 例：在Python代码中运行命令nslookup www.python.org，这和命令行直接运行的效果是一样的：
import subprocess
from multiprocessing import Process, Queue
import os, time, random

print('$ nslookup www.python.org')
r = subprocess.call(['nslookup', 'www.python.org'])
print('Exit code: ', r)

# 如果子进程还需要输入，则可以通过communicate()方法输入：

print('$ nslookup')
p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
# 此处用utf-8会报异常 'utf-8' codec can't decode byte 0xc8 in position 2: invalid continuation byte
print(output.decode('gbk'))
print('Exit code: ', p.returncode)
'''
输出结果：
$ nslookup
默认服务器:  public1.alidns.com
Address:  223.5.5.5

> > 服务器:  public1.alidns.com
Address:  223.5.5.5

python.org	MX preference = 50, mail exchanger = mail.python.org
> 
Exit code:  0

Process finished with exit code 0
'''


# 进程间通信
# Process之间肯定是需要通信的，操作系统提供了很多机制来实现进程间的通信。Python的multiprocessing模块包装了底层的机制，
# 提供了Queue、Pipes等多种方式来交换数据

# 写数据进程执行的代码
def write(q):
    print('Process to write: %s' % os.getpid())
    for value in ['a', 'b', 'c', 'd']:
        print('Put %s to queue...' % value)
        q.put(value)
        time.sleep(random.random())


def read(q):
    print('Process to read: %s' % os.getpid())
    while True:
        value = q.get(True)
        print('Get %s from queue.' % value)


if __name__ == '__main__':
    # 父进程创建queue，并传给各个子进程
    q = Queue()
    # 写进程
    pw = Process(target=write, args=(q,))
    # 读进程
    pr = Process(target=read, args=(q,))
    # 启动子进程pw和pr
    pw.start()
    pr.start()

    # 等待pw结束
    pw.join()
    # pr进程是死循环，无法等待结束，只能强行终止
    pr.terminate()

'''
输出结果：
Process to write: 12692
Put a to queue...
Process to read: 23320
Get a from queue.
Put b to queue...
Get b from queue.
Put c to queue...
Get c from queue.
Put d to queue...
Get d from queue.
'''

# 在Unix/Linux下，multiprocessing模块封装了fork()调用，使我们不需要关注fork()的细节。由于Windows没有fork调用，
# 因此，multiprocessing需要“模拟”出fork的效果，父进程所有Python对象都必须通过pickle序列化再传到子进程去，所以，
# 如果multiprocessing在Windows下调用失败了，要先考虑是不是pickle失败了。

'''
小结：
在Unix/Linux下，可以使用fork()调用实现多进程。

要实现跨平台的多进程，可以使用multiprocessing模块。

进程间通信是通过Queue、Pipes等实现的。
'''
