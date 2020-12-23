# python 循环打印示例：菱形、三角形、矩形
rows = int(input('输入列数：'))
i = j = k = 1  # 声明变量，i用于控制外层循环（图形行数），j用于控制空格的个数，k用于控制*的个数
# 等腰直角三角形
print('等腰直角三角形')
for i in range(0, rows):
    for k in range(0, rows - i):
        print("*   ", end='')  # end= 可以不换行输出
        k += 1
    i += 1
    print("\n")


# pass 占位符

def blank():
    pass

