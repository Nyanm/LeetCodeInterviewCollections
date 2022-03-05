"""
给定一个未排序的整数数组 nums ，找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。
请你设计并实现时间复杂度为 O(n) 的算法解决此问题
https://leetcode-cn.com/problems/longest-consecutive-sequence/
"""
from typing import List


class Solution:
    @staticmethod
    def longestConsecutive(nums: List[int]) -> int:
        hash_table = {}
        for num in nums:
            hash_table[num] = 0

        def dfs(node):
            nonlocal max_len
            neigh = node + 1

            try:
                val = hash_table[neigh]
                if val:
                    hash_table[node] = val + 1
                    max_len = max(max_len, val + 1)
                    return val + 1
                cur_len = dfs(neigh)
                hash_table[node] = cur_len + 1
                max_len = max(max_len, cur_len + 1)
                return cur_len + 1
            except KeyError:
                hash_table[node] = 1
                max_len = max(max_len, 1)
                return 1

        max_len = 0
        for index in range(len(nums)):
            if not hash_table[nums[index]]:
                dfs(nums[index])

        return max_len

# DFS大饼卷一切
# 空间效率低得惨不忍睹
