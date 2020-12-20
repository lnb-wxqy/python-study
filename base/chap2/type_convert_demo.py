# 开发者: 五行缺雨

# 时间: 2020/12/14 20:51
# -------str()将其他类型转换为str类型----------
print(' -------str()将其他类型转换为str类型----------')
a = 10
b = 12.3
f = True
print(type(a), type(b), type(f))  # <class 'int'> <class 'float'> <class 'bool'>
print(type(str(a)), type(str(b)), type(str(f)))  # <class 'str'> <class 'str'> <class 'str'>

# -------int()将其他类型转换为int类型----------
print('-------int()将其他类型转换为int类型----------')
s = '12'
s2 = '12.4'  # ValueError: invalid literal for int() with base 10: '12.4'
ff = 345.55
fb = False
print(type(s), type(ff), type(fb))  # <class 'str'> <class 'float'> <class 'bool'>
# print(type(int(s)), type(int(s2)), type(int(ff)), type(int(fb)))  # <class 'int'> <class 'int'> <class 'int'>
print(type(int(s)), type(int(ff)), type(int(fb)))  # <class 'int'> <class 'int'> <class 'int'>

# -------float()将其他类型转换为float类型----------
print('-------float()将其他类型转换为float类型----------')
ss = '22'
ss2 = '22.22'
f2 = True
i = 98
print(type(ss), type(ss2), type(f2), type(i))  # <class 'str'> <class 'str'> <class 'bool'> <class 'int'>
print(type(float(ss)), type(float(ss2)), type(float(f2)),
      type(float(i)))  # <class 'float'> <class 'float'> <class 'float'> <class 'float'>
