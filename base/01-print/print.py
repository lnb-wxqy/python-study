# 开发者: 五行缺雨

# 时间: 2020/12/13 21:37

# 输出数字
print(520)
print(98.4)

# 输出字符串
print('hello python')
print("helloWorld")

# 输出含有运算符的表达式
print(4 * 8)

# 不换行输出
print('hello', 'world', 'python')

# 输出到文件
# a+ 表示如果文件不存在则创建文件
fp = open("E:/file.txt", "a+")
print('helloWorld', file=fp)  # 输出中必须有file=fp
fp.close()

# r :原字符，字符串中的转义符不生效，原样输出
print(r"hello\nworld")
