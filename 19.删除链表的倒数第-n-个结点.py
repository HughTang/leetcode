#
# @lc app=leetcode.cn id=19 lang=python3
#
# [19] 删除链表的倒数第 N 个结点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # 此题的关键在于L-n+1的使用，；两种方法的复杂度相同，推荐快慢指针法
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # 方法一：暴力求解
        # dummy = ListNode(0,head)
        # 在寻找链表长度时，cur首先指向第一个非空元素
        # cur = head
        # length = 0
        # while cur:
        #     length += 1
        #     cur = cur.next
        # 在寻找待删除元素的前驱结点时，cur指向空头结点
        # cur = dummy
        # for i in range(1,length-n+1):
        #     cur = cur.next
        # cur.next = cur.next.next
        # return dummy.next

        # 方法二：快慢指针法
        dummy = ListNode(0,head)
        # first为快指针，一开始指向第一个非空元素
        first = head
        # second为慢指针，一开始指向空头结点
        second = dummy
        for i in range(n):
            first = first.next
        while first:
            second = second.next
            first = first.next
        second.next = second.next.next
        return dummy.next

# @lc code=end

