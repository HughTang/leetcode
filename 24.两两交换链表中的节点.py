#
# @lc app=leetcode.cn id=24 lang=python3
#
# [24] 两两交换链表中的节点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    '''
    此题最重要的是引用（指针）的使用，可以这么理解：
    （1）p = xxx相当于指针p指向了链表的另一个节点，
        对链表本身的结构没有影响；
    （2）p.next = xxx相当于指针p所指向的链表的那个节点中
        的next变量发生了变化，对链表节点结构产生了影响。
    因此，若要对链表节点进行调整，一般是给p.next赋值更改，
    而移动指针到另一个节点，则一般通过给p赋值来实现。
    '''
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy = ListNode(0,head)
        tmp = dummy
        while tmp.next and tmp.next.next:
            q = tmp.next
            p = q.next
            tmp.next = p
            q.next = p.next
            p.next = q
            tmp = q
        return dummy.next
# @lc code=end

