"""
给你一个整数数组 nums ，找到其中最长严格递增子序列的长度。
子序列 是由数组派生而来的序列，删除（或不删除）数组中的元素而不改变其余元素的顺序。
例如，[3,6,2,7] 是数组 [0,3,1,6,2,2,7] 的子序列。
https://leetcode-cn.com/problems/longest-increasing-subsequence
"""
from typing import List


class Solution:
    @staticmethod
    def lengthOfLIS(nums: List[int]) -> int:

        def search(cur_list: list, val: int) -> int:
            if len(cur_list) == 1:
                return val > cur_list[0]
            mid = len(cur_list) // 2
            if val > cur_list[mid]:
                return search(cur_list[mid:], val) + mid
            else:
                return search(cur_list[:mid], val)

        lis = [nums[0]]
        for index in range(1, len(nums)):
            if nums[index] > lis[-1]:
                lis.append(nums[index])
            else:
                lis[search(lis, nums[index])] = nums[index]
        return len(lis)


"""
打开小猪过河的代码开始硬抄
维护一个递增的序列是核心思想，但是替换序列中的元素才是这个算法的精髓
"""
