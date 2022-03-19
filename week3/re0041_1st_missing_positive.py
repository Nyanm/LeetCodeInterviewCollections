"""
41. 缺失的第一个正数
给你一个未排序的整数数组 nums ，请你找出其中没有出现的最小的正整数。
请你实现时间复杂度为 O(n) 并且只使用常数级别额外空间的解决方案。
https://leetcode-cn.com/problems/first-missing-positive/
"""
from typing import List


class Solution:
    @staticmethod
    def firstMissingPositive(nums: List[int]) -> int:
        length = len(nums)
        # specify invalid numbers (greater than length of the array and negative numbers)
        for index in range(length):
            if nums[index] > length or nums[index] <= 0:
                nums[index] = length + 1
        # using is-place hash to mark those elements in the range of [1, array.len]
        for index in range(length):
            abs_num = abs(nums[index])
            if abs_num != length + 1 and nums[abs_num - 1] > 0:
                nums[abs_num - 1] *= -1
        # finding the first missing positive
        for index in range(length):
            if nums[index] > 0:
                return index + 1
        return length + 1


"""
TAG 原地哈希
时间O(n) 遍历三遍（使用swap()的算法只需要两遍），空间O(1)

接触到的第一道原地哈希题目
巧妙地利用了 数组中从1开始的连续正数数量不会超过arr.len 的性质，利用数组下标指代数字
"""
