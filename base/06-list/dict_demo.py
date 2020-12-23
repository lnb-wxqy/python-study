# dict: 字典，key-value，类似于java或go的map,key不能重复
# 和list比较，dict有以下几个特点：
#
# 1.查找和插入的速度极快，不会随着key的增加而变慢；
# 2.需要占用大量的内存，内存浪费多。
#
# 而list相反：
#
# 1.查找和插入的时间随着元素的增加而增加；
# 2.占用空间小，浪费内存很少。
# 所以，dict是用空间来换取时间的一种方法。
dic1 = {'name': '五行缺雨', 'gender': '爷们'}
print(dic1)

dic2 = {}
dic2['name'] = 'she'
dic2['gender'] = 'girl'
print(dic2)

flag = 'name' in dic2
print(flag)

g = dic2.get('gender')
print(g)

g2 = dic2.get('xx')
if g2 is None:
    print('死你骂谁')

dic2.pop('name')
print(dic2)

items = dic2.items()
print(items)

keys = dic2.keys()
print(keys)

# 遍历dict
print('--------遍历key---------')
for k in dic1.keys():
    print(k)

# 遍历key-value
print('--------遍历value--------')
for k, v in dic1.items():
    print('key: %s,value:%s' % (k, v))
    print(k, v)
