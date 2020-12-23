# list集合： list是python内置的一个有序列表
# 表达式： list=['l1','l2','l3']

lis = ['貂蝉', '西施', '妲己', '昭君']
print(lis)  # 输出

print('---------遍历-----------')
# 遍历
for li in lis:
    print(li)

print('---------根据索引遍历-----------')
# 根据索引遍历
for index in range(0, len(lis)):
    print(lis[index])

# 添加元素
print('---------添加元素-----------')
lis.append('鲁班')
lis.append('小书包')
print(lis)

print('-------在指定位置插入元素------')
# 在指定位置插入元素
lis.insert(3, '程咬金')
for i in range(0, len(lis)):
    print(i, lis[i])

print('---------删除list末尾元素--------------')
lis.pop()
print(lis)

print('---------删除list指定位置元素--------------')
lis.pop(3)
print(lis)
