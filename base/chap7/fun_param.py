# 函数的参数

# 1.位置参数
# 求x的n次方
def power(x, n):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s


print(power(5, 2))


# 2.默认参数
# 注：必选参数在前，默认参数在后
def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s


print(power(5))  # 调用的是默认参数的方法

#  定义默认参数要牢记一点：默认参数必须指向不变对象！
# 采坑示例：默认参数是一个空集合
'''
>>> def add_end(L=[]):
	L.append('END')
	return L

>>> add_end([1,2,3])
[1, 2, 3, 'END']
第一次调用正常
>>> add_end()
['END']
第二次调用不正常，因为list集合是可变对象
>>> add_end()
['END', 'END']
>>> 
'''


def add_end(L=[]):
    L.append('END')
    return L


# 修改为add_end2(),无论调用多少次都不会有问题
def add_end2(L=None):
    if L is None:
        L = []
    L.append('end')
    return L


# 3.可变参数
def calc(*nums):
    sum = 0
    for n in nums:
        sum += n * n
    return sum


print(calc(1, 2, 3))
# 如果已经有一个list或tuple，可以将list或tuple转换为可变参，只需要在list或tuple前加‘*’即可
lst = [1, 2, 3, 4]
print(calc(*lst))


# 4.关键字参数
# 注意：kw获取的是dic字典的一份拷贝，对kw的改动不会影响外部dic字典
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)


person('Merry', 30)
person('Merry', 30, gender='girl')

# 同样可以传入一个字典
dic = {'gender': 'girl', 'height': 123}
person('merry', 19, **dic)


# 5.命名关键字
# 命名关键字参数必须传入参数名
# * 后面的参数成为命名关键字,即：city和job是命名关键字
def person(name, age, *, city, job):
    print(name, age, city, job)


# 调用方式
person('cherry', 12, city='Beijing', job='gopher')


# 如果命名关键字前边有可变参数，则命名关键字前不需要*
def person(name, age, *args, city, job):
    print(name, age, args, city, job)


person('五行缺雨', 20, 'sleep', 'eat', city='废都', job='gopher')

'''
小结：
Python的函数具有非常灵活的参数形态，既可以实现简单的调用，又可以传入非常复杂的参数
1.默认参数一定要用不可变对象。如果是可变对象，程序运行是回报逻辑错误！
2.注意定义可变参数和关键字参数：
    *args是可变参数，args接收的是一个元组tuple
    **kw是关键字参数，kw接收的是一个字典dict
  以及调用函数是如何传入可变参数和关键字参数的语法：
    可变参数既可以直接传入：fun((1,2,3))，也可以先组装list或tuple，再通过*args传入：fun(*(1,2,3))
    关键字参数既可以直接传入：fun((a=1,b=2)),也可以先组装dict，再通过**kw传入：fun(**{'a':1,'b':2})
3.命名关键字蚕食是为了限制调用者可以传入的参数名，同时可以提供默认值；
  定义命名关键字参数在没有可变参数的情况下不要忘了写分隔符*，否则定义的将是位置参数

'''













