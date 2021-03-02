#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        # 方法一，需要栈中存在初始元素
        dic = {'{': '}',  '[': ']', '(': ')', '?': '?'}
        stack = ['?']
        for c in s:
            if c in dic: stack.append(c)
            elif dic[stack.pop()] != c: return False 
        return len(stack) == 1

        # 方法二，初始栈为空（推荐）
        # dic = {')':'(',']':'[','}':'{'}
        # stack = []
        # for i in s:
        #     if stack and i in dic:   # 栈不为空且s中元素在字典中
        #         if stack[-1] == dic[i]: stack.pop()
        #         else: return False
        #     else: stack.append(i)
        # return not stack
# @lc code=end

