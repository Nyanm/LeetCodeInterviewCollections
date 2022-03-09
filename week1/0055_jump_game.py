"""
给定一个非负整数数组 nums ，你最初位于数组的 第一个下标 。
数组中的每个元素代表你在该位置可以跳跃的最大长度。
判断你是否能够到达最后一个下标。
https://leetcode-cn.com/problems/jump-game/
"""
from typing import List


class Solution:
    @staticmethod
    def canJump(nums: List[int]) -> bool:
        available = 0
        for index in range(len(nums)):
            available = max(available, nums[index] + index)
            if available >= len(nums) - 1:
                return True
            if available <= index:
                return False


"""
水题，豪哥收拾书包的两分钟里写出来的
"""
