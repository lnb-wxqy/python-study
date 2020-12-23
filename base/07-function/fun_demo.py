# 函数定义
import math


# 自定义函数，求绝对值
def my_abs(x):
    # 检查参数类型
    if not isinstance(x, (int, float)):
        raise TypeError('bad operate type')
    if x >= 0:
        return x
    else:
        return -x


print(my_abs(-99))  # 99


# print(my_abs('ab'))

# 返回多个值
def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny


x, y = move(100, 100, 60, math.pi / 6)
print(x, y)

'''
请定义一个函数quadratic(a, b, c)，接收3个参数，返回一元二次方程 ax^2+bx+c=0 的两个解。
提示：
一元二次方程的求根公式为：
​	
'''


def quadratic(a, b, c):
    if a == 0:
        raise TypeError('bad operate,a not be 0')
    n1 = (-b + math.sqrt(my_abs(b * b - 4 * a * c))) / (2 * a)
    n2 = (-b - math.sqrt(my_abs(b * b - 4 * a * c))) / (2 * a)
    return n1, n2


x1, x2 = quadratic(2, 3, 1)
print(x1, x2)
x1, x2 = quadratic(1, 3, -4)
print(x1, x2)
