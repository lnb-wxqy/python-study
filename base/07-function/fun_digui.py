# 递归函数
# 求n的阶乘: n!=1*2*...*(n-1)*n

def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)


# ret = fact(1000) # 参数为1000时报错，Traceback (most recent call last)，RecursionError: maximum recursion depth exceeded in comparison
print(fact(3))


# tip：使用递归函数需要注意防止栈溢出。在计算机中，函数调用是通过栈（stack）这种数据结构实现的，每当进入一个函数调用，栈
# 就会加一层栈帧，每当函数返回，栈就会减一层栈帧，由于栈的大小是有限的，所以递归函数调用的次数过多，会导致栈溢出。如上面fact(1000)
# tip2：解决递归调用栈溢出的方法是通过尾递归优化，事实上尾递归和循环的效果是一样的，所以把循环看成是一种特殊的尾递归函数也是可以的。
# 尾递归：是指在函数返回的时候，调用自身本身，并且，return语句不能包含表达式。这样，编译器或者解释器就可以把尾递归优化，是递归本身无论调用
# 多少次，都只占用一个栈帧，不会出现栈溢出的情况。上面fact(n)函数由于return n*fact(n-1)引入了乘法表达式，所有就不是尾递归了。
# 改进：
def fact_iter(n, product):
    if n == 1:
        return product
    return fact_iter(n - 1, n * product)


'''
尾递归调用时，如果做了优化，栈不会增长，因此，无论多少次调用也不会导致栈溢出。
遗憾的是，大多数编程语言没有针对尾递归做优化，Python解释器也没有做优化，所以，即使把上面的fact(n)函数改成尾递归方式，也会导致栈溢出。'''
