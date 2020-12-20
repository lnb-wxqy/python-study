name = "python"
flag = False

if name == "python":
    flag = True
    print('welcome python')
else:
    print(name)

#  elif用法
num = 5
if num == 3:
    print("三")
elif num == 2:
    print("二")
elif num == 1:
    print("一")
else:
    print(num)

# python不支持switch
# python多条件判断
n = 9
if 0 < n < 10:
    print("n在0到10之间")
if n > 0 or n < 100:
    print("嘻嘻哈哈")
