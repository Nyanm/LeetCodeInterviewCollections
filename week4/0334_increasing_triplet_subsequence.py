"""
334. 递增的三元子序列
给你一个整数数组 nums ，判断这个数组中是否存在长度为 3 的递增子序列。
如果存在这样的三元组下标 (i, j, k) 且满足 i < j < k ，使得 nums[i] < nums[j] < nums[k] ，返回 true ；否则，返回 false 。
https://leetcode-cn.com/problems/increasing-triplet-subsequence
"""
from typing import List
from math import inf


class Solution:
    @staticmethod
    def increasingTriplet(nums: List[int]) -> bool:
        low, mid = nums[0], inf
        for index in range(1, len(nums)):
            if nums[index] > mid:
                return True
            if nums[index] > low:
                mid = nums[index]
            else:
                low = nums[index]
        return False


"""
本质上是最大递增子序列(LIS)的弱化版问题，对N=3的子序列进行二分查找的问题被近似成了O(1)的问题，获得了总体O(N)的时间复杂度
"""
