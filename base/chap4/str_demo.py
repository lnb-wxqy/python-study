# 字符串
# 字符串索引：0为开始值，-1为从末尾开始的值

s = 'python'
print(s)
print(s[0:-1])  # pytho 输出第一个至倒数第二个字符，[0:-1]包含左边，不包含右边
print(s[:-1])  # pytho
print(s[2:5])  # tho

# 格式化输出
print('我叫 %s,今年%d岁了' % ('爱丽丝', 10))

# str.format()函数
# 基本语法是通过 {} 和 : 来代替以前的 % 。
# 1. 按位置顺序输出
print("{},{}".format('hello', 'python'))  # hello,python
print("{1},{0}".format('hello', 'python'))  # python,hello

# 参数输出
# 2.1.按参数名输出
print("网名：{name},性别：{gender}".format(name="五行缺雨", gender="爷们"))
# 2.2 通过字典设置参数
site = {"name": "五行缺雨", "hobby": "不详"}
print("网名：{name},爱好：{hobby}".format(**site))

# 数字格式化，参考菜鸟教程：https://www.runoob.com/python/att-string-format.html

# ord()函数获取字符的整数表示，chr()函数把编码转换为对应的字符：
print(ord('中'))
print(ord('A'))

print(chr(66))

# len()函数，计算字符串的长度
print(len('中文'))
