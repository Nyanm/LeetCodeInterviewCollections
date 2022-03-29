"""
1248. 统计「优美子数组」
给你一个整数数组 nums 和一个整数 k。如果某个连续子数组中恰好有 k 个奇数数字，我们就认为这个子数组是「优美子数组」。
请返回这个数组中 「优美子数组」 的数目。
https://leetcode-cn.com/problems/count-number-of-nice-subarrays
"""
from typing import List


class Solution:
    @staticmethod
    def numberOfSubarrays(nums: List[int], k: int) -> int:
        odd_list, cnt = [], 0
        for index in range(len(nums)):
            if nums[index] % 2:
                odd_list.append(index)
        if len(odd_list) < k:
            return cnt
        odd_list = [-1] + odd_list + [len(nums)]
        for index in range(1, len(odd_list) - k):
            left = odd_list[index] - odd_list[index - 1]
            right = odd_list[index + k] - odd_list[index + k - 1]
            cnt += left * right
        return cnt


"""
很有趣的哈希+滑动窗口题目
第一反应是时间复杂度O(N^2)的DP，这和暴力解根本没区别啊kora!
"""
