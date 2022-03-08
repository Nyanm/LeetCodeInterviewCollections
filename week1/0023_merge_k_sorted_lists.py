"""
给你一个链表数组，每个链表都已经按升序排列。
请你将所有链表合并到一个升序链表中，返回合并后的链表。
https://leetcode-cn.com/problems/merge-k-sorted-lists/
"""
from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    @staticmethod
    def mergeKLists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        if not lists:
            return None

        def merge(node1: ListNode, node2: ListNode) -> ListNode:
            head = ListNode()  # empty head node, will be removed latter
            cur = head
            while node1 and node2:
                if node1.val <= node2.val:
                    cur.next = node1
                    node1 = node1.next
                else:
                    cur.next = node2
                    node2 = node2.next
                cur = cur.next

            if not node1:
                cur.next = node2
            elif not node2:
                cur.next = node1

            return head.next

        while len(lists) > 1:
            length = len(lists)
            new_lists = []
            for index in range(0, length, 2):
                if index + 1 < length:
                    new_lists.append(merge(lists[index], lists[index + 1]))
                else:
                    new_lists.append(lists[index])
            lists = new_lists

        return lists[0]


"""
一次过爽了爽了
"""
