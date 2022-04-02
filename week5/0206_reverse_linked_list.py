"""
206. 反转链表
给你单链表的头节点 head ，请你反转链表，并返回反转后的链表。
https://leetcode-cn.com/problems/reverse-linked-list/
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, _next=None):
        self.val = val
        self.next = _next


class Solution:
    @staticmethod
    def reverseList(head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        _before, _cur = None, head
        while _cur:
            _next = _cur.next
            _cur.next = _before
            # update node
            _before = _cur
            _cur = _next
        return _before


"""
破题写了17分钟，写错一个边界条件导致无限循环了
"""
