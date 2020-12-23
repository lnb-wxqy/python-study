# 另一种有序集合：tuple元组
# tuple与list类似，但是tuple一旦初始化就不能修改
# 表达式：tuple=('element1','element2','element3')
# tuple没有list的append()、insert()、pop()方法
t = ('李白', '韩信', '赵云', '兰陵王')
print(t)
for i in t:
    print(i)

t2 = (1)  # 不是tuple
t3 = (1,)  # 这样定义表示只有一个元素的tuple
print(t2)
print(t3)

# '可变的tuple'
t4 = ('a', 'b', ['m', 'n'], 'c')
print(t4)  # ('a', 'b', ['m', 'n'], 'c')
t4[2][0] = 'X'
t4[2][1] = 'Y'
print(t4)  # ('a', 'b', ['X', 'Y'], 'c')
# 表面上看tuple确实变了，但其实变的不是tuple的元素，而是list的元素。tuple一开始指向的list并没有改成别的list，所以tuple所谓的不变是说，tuple
# 的每个元素指向不变。

print(type(()))  # <class 'tuple'>
