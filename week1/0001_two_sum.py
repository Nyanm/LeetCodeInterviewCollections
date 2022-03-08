"""
给定一个整数数组 nums和一个整数目标值 target，请你在该数组中找出 和为目标值 target 的那两个整数，并返回它们的数组下标。
你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。
你可以按任意顺序返回答案。
https://leetcode-cn.com/problems/two-sum
"""
from typing import List


def twoSum_on2(nums: List[int], target: int) -> List[int]:
    len_num = len(nums)
    for index1 in range(len_num):
        for index2 in range(index1 + 1, len_num):
            if nums[index1] + nums[index2] == target:
                return [index1, index2]


def twoSum(nums: List[int], target: int) -> List[int]:
    len_num = len(nums)
    hashtable = dict(zip(nums, range(0, len_num)))
    for index1 in range(len_num):
        res = target - nums[index1]
        try:
            index2 = hashtable[res]
            if index1 == index2:
                continue
            return [index1, index2]
        except KeyError:
            pass

# 手生了，被一个KeyError卡了好久
