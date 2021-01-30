# -*- coding: utf-8 -*-
# @Time    : 2021/1/29 16:26
# @Author  : Zoey
# @File    : training_4.py
# @describe:

"""
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。
有效字符串需满足：
左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合

输入：s = "()"
输出：true

输入：s = "()[]{}"
输出：true

输入：s = "(]"
输出：false

输入：s = "([)]"
输出：false

"""

s = "()[]{}"
left = ""
right = ""
value = ["()", "[]", "{}"]
if len(s) % 2 != 0 or len(s) == 0 or s[0] == ")" or s[0] == "]" or s[0] == "}":
    print("无效字符3")
else:
    for i in range(len(s)):
        if s[i] == "(" or s[i] == "[" or s[i] == "{":
            left = left + s[i]
        elif s[i] == ")" or s[i] == "]" or s[i] == "}" and s != "":
            right = right + s[i]
            if left == "" and right != "":
                break
            else:
                result = left[-1] + right[0]
                if result in value:
                    left = left[0:-1]
                    right = ""
                else:
                    break
    if left == "" and right == "":
        print(True)
    else:
        print(False)
