"""
382. 链表随机节点
给你一个单链表，随机选择链表的一个节点，并返回相应的节点值。每个节点 被选中的概率一样 。
实现 Solution 类：
Solution(ListNode head) 使用整数数组初始化对象。
int getRandom() 从链表中随机选择一个节点并返回该节点的值。链表中所有节点被选中的概率相等。
https://leetcode-cn.com/problems/linked-list-random-node
"""
from typing import Optional
import random


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.head = head

    def getRandom(self) -> int:
        node = self.head
        rnd_val, cnt = 0, 1
        while node:
            if random.random() < (1 / cnt):
                rnd_val = node.val
            cnt += 1
            node = node.next
        return rnd_val


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()


"""
水塘采样问题 https://zhuanlan.zhihu.com/p/29178293
面试应该不会考到 k > 1 的情况吧（心虚）
"""
