"""
287. 寻找重复数
给定一个包含 n + 1 个整数的数组 nums ，其数字都在 [1, n] 范围内（包括 1 和 n），可知至少存在一个重复的整数。
假设 nums 只有 一个重复的整数 ，返回 这个重复的数 。
你设计的解决方案必须 不修改 数组 nums 且只用常量级 O(1) 的额外空间。
https://leetcode-cn.com/problems/find-the-duplicate-number
"""
from typing import List


class Solution:
    @staticmethod
    def findDuplicate(nums: List[int]) -> int:
        fast, slow = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[fast]
            fast = nums[fast]
            if slow == fast:
                break
        slow = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow


"""
邪门快慢指针，圈的入口就是重复数很好理解，但是将slow置零重新找到入口需要一点数理推导
很难 
"""
