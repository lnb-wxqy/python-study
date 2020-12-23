# datetime 是Python处理日期和时间的标准库

# 1.获取当前时间和日期
from datetime import datetime, timedelta

# 注意：datetime是模块，datetime模块还包含一个datetime类，
# 通过 from datetime import datetime 导入的采石datetime这个类，
# 如果仅导入import datetime，则必须引用全名datetime.datetime
now = datetime.now()
print(now)

# 2.获取指定日期和时间,直接用参数构造一个datetime
dt = datetime(2020, 12, 22, 10, 56, 55)
print(dt)

# 3.datetime转换为timestamp，只需要调用timestamp()方法即可
# 注意：timestamp()返回的是s，要想使用毫秒，需乘以1000
dt_stamp = dt.timestamp() * 1000
print(dt_stamp)

# 4.timestamp转换为datetime，调用datetime.fromtimestamp(time)方法即可
# 注意: 参数time是秒 s
st = 1608605815
st_datetime = datetime.fromtimestamp(st)  # 本地时间
print(st_datetime)
utc_st = datetime.utcfromtimestamp(st)
print(utc_st)

# 字符串str转datetime，strptime()方法
cday = datetime.strptime('2020-12-20 11:17:22', '%Y-%m-%d %H:%M:%S')
print(cday, type(cday))

# datetime转为字符串str，datetime.strftime()方法
now = datetime.now()
strTime = now.strftime('%a,%b,%d %H:%M')
print(strTime)
strTime = now.strftime('%Y-%m-%d %H:%M:%S')
print(strTime)

# datetime加减,需导入tiemdelta类后可以直接使用+和-运算
now2 = datetime.now()
print('now2: ', now2)
t2 = datetime(2020, 11, 11, 11, 11, 11)
print(t2)
newNow2 = now2 + timedelta(hours=10)
print('newNow2: ', newNow2)

newNow3 = now2 - timedelta(days=1)
print('newNow3: ', newNow3)

newNow4 = now2 + timedelta(days=2, hours=3, minutes=20)
print('newNow4: ', newNow4)

utcNow = datetime.utcnow()
print(utcNow)
