# 开发者: 五行缺雨

# 时间: 2020/12/17 0:35
# 枚举

from enum import Enum
Month=Enum('Month',('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

for name,member in Month._member_map_.items():
    print('name: ',name,'member: ',member)
