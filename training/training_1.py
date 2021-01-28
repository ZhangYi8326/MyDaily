# -*- coding: utf-8 -*-
# @Time    : 2021/1/28 15:11
# @Author  : Zoey
# @File    : training_1.py
# @describe:

"""
有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
"""
x = ["1", "2", "3", "4"]
total = 0
for i in x:
    for j in x:
        for k in x:
            if i != j and i != k and j != k:
                print(i+j+k)
                total += 1
print(total)
