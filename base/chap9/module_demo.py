#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '

__author__ = '五行缺雨'

import sys

'''
第1行和第2行是标准注释，第1行注释可以让这个hello.py文件直接在Unix/Linux/Mac上运行，第2行注释表示.py文件本身使用标准UTF-8编码；

第4行是一个字符串，表示模块的文档注释，任何模块代码的第一个字符串都被视为模块的文档注释；

第6行使用__author__变量把作者写进去，这样当你公开源代码后别人就可以瞻仰你的大名；
'''

def test():
    args = sys.argv
    print(args)


if __name__ == '__main__':
    test()

