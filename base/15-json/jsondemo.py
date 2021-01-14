import json

data = {
    'name': "linna",
    'age': 25
}


json_str = json.dumps(data)
print('原始数据：', repr(data))
print('json_str: ', json_str)

import sys
sys.stdout.write(chr(1))
sys.stdout.write(chr(1))
print ('')

for i in range(1,11):
    for j in range(1,i):
        sys.stdout.write(chr(219))
        sys.stdout.write(chr(219))
    print ('')
