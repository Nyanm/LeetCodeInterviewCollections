"""
128. 最长连续序列
给定一个未排序的整数数组 nums ，找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。
请你设计并实现时间复杂度为 O(n) 的算法解决此问题。
https://leetcode-cn.com/problems/longest-consecutive-sequence
"""
from typing import List
from collections import defaultdict


class Solution:
    @staticmethod
    def longestConsecutive(nums: List[int]) -> int:
        if not nums:
            return 0

        seen = defaultdict(int)
        for num in nums:
            seen[num] = 1

        def dfs(node: int):
            nonlocal seen
            if seen[node - 1] == 1:
                dfs(node - 1)
            seen[node] = seen[node - 1] + 1

        for num in nums:
            dfs(num)

        return max(seen.values())


"""
TAG DFS 哈希表
O(n) 遍历一次，每个节点最多被访问一次

换defaultdict后简洁程度上升了一个档次，已经是猴面雀也能看懂的代码了呢（
"""
