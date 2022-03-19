"""
1. 两数之和
给定一个整数数组 nums和一个整数目标值 target，请你在该数组中找出 和为目标值 target 的那两个整数，并返回它们的数组下标。
你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。
你可以按任意顺序返回答案。
https://leetcode-cn.com/problems/two-sum
"""

from typing import List


class Solution:
    @staticmethod
    def twoSum(nums: List[int], target: int) -> List[int]:
        seen = {}
        for index in range(len(nums)):
            seen[nums[index]] = index
        for index in range(len(nums)):
            try:
                if seen[target - nums[index]] != index:
                    return [index, seen[target - nums[index]]]
            except KeyError:
                continue


"""
TAG 哈希表
O(n) 遍历两次元素：一次存表，一次查表，其余操作都是常数时间

最简单的查表
核心思想是把“验证 a + b = target”转换为“查找∃b 使 target - a = b”，今后在更多题目中会更多地遇到这种思想
第12行的判断隐含了 如果所查找的两个数相同，那么存入哈希表的序号一定比正在遍历的大 的条件
"""
