"""
给你一个未排序的整数数组 nums ，请你找出其中没有出现的最小的正整数。
请你实现时间复杂度为 O(n) 并且只使用常数级别额外空间的解决方案。
https://leetcode-cn.com/problems/first-missing-positive/
"""
from typing import List


class Solution:
    @staticmethod
    def firstMissingPositive(nums: List[int]) -> int:
        length = len(nums)
        for index in range(length):
            if nums[index] > length or nums[index] <= 0:
                nums[index] = length + 1

        for index in range(length):
            abs_num = abs(nums[index])
            if abs_num <= length:
                target = abs_num - 1
                if nums[target] > 0:
                    nums[target] = nums[target] * -1

        for index in range(length):
            if nums[index] >= 0:
                return index + 1
        return length + 1

# 原地哈希
# 看上去好像不难，但是要考虑的边界情况很复杂，提交失败了一万次
