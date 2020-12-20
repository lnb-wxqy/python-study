# 装饰器函数
import functools

def log(func):
    print('call %s()' % func.__name__)


@log
def now():
    print('2020-12-16')


now

# 偏函数
# Python的functools模块提供了很多有用的功能，其中一个就是偏函数（Partial function）
# 使用
# functools.partial就是帮助我们创建一个偏函数的，不需要我们自己定义int2()，可以直接使用下面的代码创建一个新的函数int2
# 所以，简单总结functools.partial的作用就是，把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数，调用这个新函数会更简单。
int2 = functools.partial(int, base=2)
int_ = int2('10000')
print(int_)
