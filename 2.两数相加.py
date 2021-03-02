#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] 两数相加
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # 解法一
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 头结点
        l3 = ListNode(0)
        l0 = l3
        # 进位
        flag = 0
        while l1 != None or l2 != None:
            # 考虑一个链表为空，另一个链表非空的情况
            if l1:
                v1 = l1.val
                l1 = l1.next
            else:
                v1 = 0
            
            if l2:
                v2 = l2.val
                l2 = l2.next
            else:
                v2 = 0
            '''
            以下写法值得借鉴
            # v1 = l1.val if l1 else 0
            # v2 = l2.val if l2 else 0
            '''
            
            # flag的值的确定，l3的赋值
            value = v1 + v2 + flag
            flag = value // 10
            
            '''下面两行不可以写成：
            l3 = l3.next
            l3 = ListNode(value % 10)
            因为第一行的l3并未获取next节点，属于非法引用（野指针），
            因此必须先构造节点赋值给l3.next才可以
            '''
            l3.next = ListNode(value % 10)
            l3 = l3.next
        
        # 考虑最后一位是进位的情况
        if flag:
            l3.next = ListNode(flag)
        
        # 返回除头结点以外的链表
        return l0.next

# @lc code=end

