"""
给你两个非空 的链表，表示两个非负的整数。它们每位数字都是按照逆序的方式存储的，并且每个节点只能存储一位数字。
请你将两个数相加，并以相同形式返回一个表示和的链表。
你可以假设除了数字 0 之外，这两个数都不会以 0开头。
https://leetcode-cn.com/problems/add-two-numbers
"""


# Definition for singly-linked list.
def generate(num_list):
    length = len(num_list)
    res = [ListNode() for _ in range(length)]
    for index in range(length):
        res[index].val = num_list[index]
        try:
            res[index].next = res[index + 1]
        except IndexError:
            res[index].next = None
    return res[0]


class ListNode:
    def __init__(self, val=0, next_node=None):
        self.val = val
        self.next = next_node


class Solution:
    @staticmethod
    def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        res = []
        while True:

            if l1 is not None:
                reg1 = l1.val
                l1 = l1.next
            else:
                reg1 = 0
            if l2 is not None:
                reg2 = l2.val
                l2 = l2.next
            else:
                reg2 = 0

            sum_val = reg1 + reg2 + carry
            temp = ListNode(val=(sum_val % 10))
            res.append(temp)
            if len(res) > 1:
                res[-2].next = res[-1]

            carry = sum_val // 10
            if l1 == l2 is None and not carry:
                return res[0]

# 直接两数相加估计会快一点，但是按节点相加有一种形式主义的美感（确信
