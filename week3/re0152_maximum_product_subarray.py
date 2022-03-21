"""
152. 乘积最大子数组
给你一个整数数组 nums，请你找出数组中乘积最大的非空连续子数组（该子数组中至少包含一个数字），并返回该子数组所对应的乘积。
测试用例的答案是一个32-位 整数。
子数组 是数组的连续子序列。
https://leetcode-cn.com/problems/maximum-product-subarray
"""
from typing import List


class Solution:

    # memo solution
    @staticmethod
    def maxProductMemo(nums: List[int]) -> int:
        memo = [[None] * 2 for _ in range(len(nums))]  # a memo of [MaxVal, MinVal]
        memo[0] = [nums[0], nums[0]]
        greatest = nums[0]
        for index in range(1, len(nums)):
            max_val, min_val = memo[index - 1]
            memo[index][0] = max(max_val * nums[index], min_val * nums[index], nums[index])
            memo[index][1] = min(min_val * nums[index], max_val * nums[index], nums[index])
            greatest = max(greatest, memo[index][0])
        return greatest

    # rolling solution, with better memory efficiency
    @staticmethod
    def maxProduct(nums: List[int]) -> int:
        max_cur = min_cur = greatest = nums[0]
        for index in range(1, len(nums)):
            cur_num = nums[index]
            max_next = max(max_cur * cur_num, min_cur * cur_num, cur_num)
            min_next = min(max_cur * cur_num, min_cur * cur_num, cur_num)
            max_cur, min_cur = max_next, min_next
            greatest = max(max_cur, greatest)
        return greatest


"""
TAG 动态规划 滚动数组
时间O(n) 遍历一遍数组
空间O(1) 应用滚动数组后只记录上一次的状态，而状态转移方程保证了存储在上一次的状态就是 直到上一次的最优解

基础DP题目，只要写出状态转移方程就能很好地理解答案
特别需要注意由于求的是最大乘积，而考虑到负负得正的情况，应该在遍历过程中维护最大积和最小积
用双指针去思考这道题就完蛋了（悲）
"""
