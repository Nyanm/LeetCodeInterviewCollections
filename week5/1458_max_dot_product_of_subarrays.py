"""
1458. 两个子序列的最大点积
给你两个数组 nums1 和 nums2 。
请你返回 nums1 和 nums2 中两个长度相同的 非空 子序列的最大点积。
数组的非空子序列是通过删除原数组中某些元素（可能一个也不删除）后剩余数字组成的序列，但不能改变数字间相对顺序。比方说，[2,3,5] 是 [1,2,3,4,5] 的一个子序列而 [1,5,3] 不是。
https://leetcode-cn.com/problems/max-dot-product-of-two-subsequences
"""
from typing import List
from math import inf


class Solution:
    @staticmethod
    def maxDotProduct(nums1: List[int], nums2: List[int]) -> int:
        len1, len2 = len(nums1), len(nums2)
        memo = [[-inf] * (len2 + 1) for _ in range(len1 + 1)]
        for idx1 in range(1, len1 + 1):
            for idx2 in range(1, len2 + 1):
                cur_pdt = nums1[idx1 - 1] * nums2[idx2 - 1]  # current product
                memo[idx1][idx2] = max((memo[idx1 - 1][idx2 - 1] + cur_pdt), cur_pdt,
                                       memo[idx1 - 1][idx2], memo[idx1][idx2 - 1])
        return int(memo[-1][-1])


"""
不如乘积最大子数组
"""
