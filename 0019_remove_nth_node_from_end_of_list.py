"""
给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。
https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list/
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    @staticmethod
    def removeNthFromEnd(head: ListNode, n: int) -> ListNode:
        node_array = []
        cur = head
        while cur:
            node_array.append(cur)
            cur = cur.next

        if len(node_array) == 1:
            return None
        elif len(node_array) == n:
            return head.next
        elif n == 1:
            node_array[-2].next = None
            return head

        node_array[-n - 1].next = node_array[-n + 1]
        del node_array[-n]
        return head


"""
花了点时间判断边界条件
"""
