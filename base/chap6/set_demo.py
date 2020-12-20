# set: set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key.
# 要创建一个set，需要提供一个list作为输入集合；
s = set([1, 2, 3])
print(s, type(s))  # {1, 2, 3} <class 'set'>

# 重复元素在set中会被过滤
s2 = set([1, 2, 3, 4, 5, 5, 5, 5])
print(s2)  # {1, 2, 3, 4, 5}

# add()添加元素
s2.add(12)
s2.add(14)
print(s2)

# remove()删除元素
s2.remove(12)
print(s2)
