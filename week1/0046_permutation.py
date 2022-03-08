"""
给定一个不含重复数字的数组 nums ，返回其 所有可能的全排列 。你可以 按任意顺序 返回答案。
https://leetcode-cn.com/problems/permutations/
"""
from typing import List
from copy import deepcopy


class Solution:
    @staticmethod
    def permute(nums: List[int]) -> List[List[int]]:
        ans = [[nums[0]]]

        for outer in range(1, len(nums)):
            cur = nums[outer]
            new_ans = []
            last_ans = deepcopy(ans)
            for template in last_ans:
                for inner in range(len(template) + 1):
                    new_ans.append(template[:inner] + [cur] + template[inner:])

            ans = new_ans

        return ans


"""
灵感来自 78 Subsets
"""
