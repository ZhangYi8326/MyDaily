# -*- coding: utf-8 -*-
# @Time    : 2021/1/28 15:15
# @Author  : Zoey
# @File    : training_2.py
# @describe:
"""
判断字符串是否是回文字符串
"""

# 方法1
a = "abddba"
b = ""
for i in range(-1, -len(a)-1, -1):
    b += a[i]
if b == a:
    print(b)
else:
    print("a不是回文")

# 方法2
a = "aba"
b = a[:: -1]
if b == a:
    print(b)
else:
    print("不对")
