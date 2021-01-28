# -*- coding: utf-8 -*-
# @Time    : 2021/1/28 17:15
# @Author  : Zoey
# @File    : training_3.py
# @describe:

"""
给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 的那 两个 整数，并返回它们的数组下标。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。

你可以按任意顺序返回答案

输入：nums = [2,7,11,15], target = 9
输出：[0,1]

输入：nums = [3,2,4], target = 6
输出：[1,2]

输入：nums = [3,3], target = 6
输出：[0,1]
"""

nums = [3, 2, 3]
target = 6
for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        if nums[i] + nums[j] == target:
            print(i, j)
