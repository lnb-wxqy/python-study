# 文件读写

# 读取文本
try:
    # 传入文件名和标示符,标识符r表示 读
    f = open('E:/lnb/test.txt', 'r')
    read = f.read()
finally:
    if f:
        f.close()
print(read)

# 上面关闭f的方式比较繁琐，python提供了with语句来自动帮我们调用close()方法
with open('E:/lnb/test.txt', 'r') as f:
    print(f.read())

# 如果文件很小，read()一次性读取最方便；如果不能确定文件大小，反复调用read(size)比较保险；如果是配置文件，调用readlines()最方便：
with open('E:/lnb/test.txt', 'r') as f:
    for line in f.readlines():
        print(line)

# 读取二进制 标识符用rb
with open('E:/lnb/保险.docx', 'rb') as f:
    print(f.read())
