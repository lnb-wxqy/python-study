# 高阶函数
# 1.map和reduce. python内建了map()he reduce()函数
# map: map()函数接收两个参数，一个是函数，一个是迭代器Iterable,map将传入的函数一次作用到序列的每个元素，
# 并把结构作为新的Iterator返回。
# 举例：要把函数 f(x)=x^2,作用在一个list[1,2,3,4,5,6,7,8,9]上，就可以用map()实现如下：
def f(x):
    return x * x


r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(list(r))  # [1, 4, 9, 16, 25, 36, 49, 64, 81]

# 举例2;把list所有数据转换为字符串：
newLst = list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(newLst)  # ['1', '2', '3', '4', '5', '6', '7', '8', '9']

print(sum([1, 2, 3]))


# reduce 略。。。

# filter()函数：和map()类似，filter()也接收一个函数和一个序列。和map()不同的是，filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。
# 举例1：在一个list中，删掉偶数，只保留奇数
def is_odd(n):
    return n % 2 == 1


lst = list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15]))
print(lst)  # [1, 5, 9, 15]


# 举例2：把已list中的空字符串去掉
def not_empty(s):
    return s and str.strip(s)


new_lst = list(filter(not_empty, ['A', '', 'B', None, 'C', '  ']))
print(new_lst)  # ['A', 'B', 'C']

# sorted()：排序算法
# 举例：对list排序
newLst = sorted([36, 5, -12, 9, -21])
print(newLst)  # [-21, -12, 5, 9, 36]

# sorted() 可以接受一个key函数来实现自定义的排序，例如按绝对值大小排序：
newLst = sorted([36, 5, -12, 9, -21], key=abs)
print(newLst)  # [5, 9, -12, -21, 36]

# 对字符串集合list排序
# 默认情况下，对字符串排序，是按照ASCII的大小比较的，由于'Z' < 'a'，结果，大写字母Z会排在小写字母a的前面。
newLst = sorted(['bob', 'about', 'Zoo', 'Credit'])
print(newLst)  # ['Credit', 'Zoo', 'about', 'bob']

# 将大写转成小写，并逆序排序
newLst = sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True)
print(newLst)  # ['Zoo', 'Credit', 'bob', 'about']
