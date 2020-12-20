# while 循环
n = 0
while n < 10:
    print("n: ", n)
    n += 1
print("GOOD BYE!")

# continue用法
i = 0
while i < 10:
    i += 1
    if i % 2 == 0:
        continue
    print("i: ", i)

# break
j = 0
while j < 10:
    j += 1
    if j > 5:
        break
    print("j: ", j)
