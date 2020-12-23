# 异常处理
# try...except...finall..
import logging

logging.basicConfig(level=logging.INFO)
try:
    print('try...')
    logging.info('try--info...')  # 未输出,在import logging 下面配置：logging.basicConfig(level=logging.INFO)
    r = 10 / 0
    print('result: ', r)
except Exception as e:
    print('except: ', e)
    logging.exception(e)
else:  # 当没有错误发生时，会执行else
    print('else')
finally:
    print('finally')
print('end')
