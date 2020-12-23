# collections是Python内建的一个集合模块，提供了许多有用的集合类。
# 1. namedtuple
'''
# 我们知道tuple可以表示不变集合，例如：一个点的二维坐标表示为：
# p = (1, 2)
# 但是看到(1,2)，很难看出这是表示坐标的，namedtuple改出场了
'''

from collections import namedtuple, deque, defaultdict, OrderedDict, Counter

Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print(p.x, p.y)

# namedtuple是一个函数，它用来创建一个自定义的tuple对象，并且规定了tuple元素的个数，并可以用属性而不是索引来引用tuple的某个元素。
# 这样一来，我们用namedtuple可以很方便地定义一种数据类型，它具备tuple的不变性，又可以根据属性来引用，使用十分方便。

# 类似的，可以用坐标和半径表示一个圆
Circle = namedtuple('CirCle', ['x', 'y', 'r'])

# 2. deque
'''
# 使用list存储数据时，按索引访问元素很快，但是插入和删除元素就很慢了，因为list是线性存储，数据量大的时候，插入和删除效率很低。
# deque 是为了高效实现插入和删除操作的双向链表，适合用于队列和栈
# deque除了实现list的append()和pop()外，还支持appendleft()和popleft(),这样就可以非常高效的往头部添加或删除元素
'''

q = deque(['a', 'b', 'c'])
q.append('x')
q.appendleft('y')
print(q)

# 3. defaultdict
'''
使用dict时，如果引用的key不存在，就会抛出keyError.如果希望key不存在时，返回一个默认值，就可以使用defaultdict
注意：默认值是调用函数返回的，而函数在创建defaultdict对象时传入
除了再key不存在是返回默认值，defaultdict其他行为跟dict是完全一样的
'''
dd = defaultdict(lambda: 'N/A')
dd['k1'] = 'abc'
print(dd['k1'])  # 存在，输出：abc
print(dd['k2'])  # 不存在，输出：N/A

# 4. OrderedDict
# dict的key是无序的，迭代dict是，无法确定key的顺序。OrderedDict会按照Key插入的顺序排列，注意：不是key本身排序。
od = OrderedDict()
od['a'] = 1
od['c'] = 2
od['d'] = 4
od['b'] = 3

keys = od.keys()
print(list(keys))  # ['a', 'c', 'd', 'b']


# OrderedDict可以实现一个FIFO（先进先出）的dict，当容量超出限制时，先删除最早添加的Key：
class LastUpdateOrderedDict(OrderedDict):
    def __init__(self, capacity):
        super(LastUpdateOrderedDict, self).__init__()
        self._capacity = capacity

    def __setitem__(self, key, value):
        # 三目运算符，好别扭
        containsKey = 1 if key in self else 0
        if len(self) - containsKey >= self._capacity:
            last = self.popitem(last=False)
            print('remove', last)
        if containsKey:
            del self[key]
            print('set: ', (key, value))
        else:
            print('add: ', (key, value))
        OrderedDict.__setitem__(self, key, value)


# chainMap
'''
ChainMap可以把一组dict串起来并组成一个逻辑上的dict。ChainMap本身也是一个dict，但是查找的时候，会按照顺序在内部的dict依次查找。
什么时候使用ChainMap最合适？举个例子：应用程序往往都需要传入参数，参数可以通过命令行传入，可以通过环境变量传入，还可以有默认参数。我们可以用ChainMap实现参数的优先级查找，即先查命令行参数，如果没有传入，再查环境变量，如果没有，就使用默认参数。
'''

# 5. Counter
# Counter是一个简单的计数器，例如：统计字符出现的个数
c = Counter()
for ch in 'programming':
    c[ch] = c[ch] + 1

print(c)  # 输出：Counter({'r': 2, 'g': 2, 'm': 2, 'p': 1, 'o': 1, 'a': 1, 'i': 1, 'n': 1})

# 可以一次性update
c.update('hello')
print(c)  # 输出：Counter({'r': 2, 'o': 2, 'g': 2, 'm': 2, 'l': 2, 'p': 1, 'a': 1, 'i': 1, 'n': 1, 'h': 1, 'e': 1})
