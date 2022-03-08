"""
给你一个整数数组 nums ，数组中的元素 互不相同 。返回该数组所有可能的子集（幂集）。
解集 不能 包含重复的子集。你可以按 任意顺序 返回解集。
https://leetcode-cn.com/problems/subsets/
"""
from typing import List
from copy import deepcopy


class Solution:
    @staticmethod
    def subsets(nums: List[int]) -> List[List[int]]:
        res = [[]]
        for ele in nums:
            new_res = deepcopy(res)
            for sub in new_res:
                sub.append(ele)
            res = new_res + res
        return res


"""
leetcode里居然支持直接调用deepcopy，不清楚它到底引用了哪些库
"""
