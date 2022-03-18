"""
135. 分发糖果
n 个孩子站成一排。给你一个整数数组 ratings 表示每个孩子的评分。
你需要按照以下要求，给这些孩子分发糖果：
每个孩子至少分配到 1 个糖果。
相邻两个孩子评分更高的孩子会获得更多的糖果。
请你给每个孩子分发糖果，计算并返回需要准备的 最少糖果数目 。
https://leetcode-cn.com/problems/candy
"""
from typing import List


class Solution:
    @staticmethod
    def candy(ratings: List[int]) -> int:
        nums = [1] * len(ratings)
        for index in range(1, len(ratings)):
            if ratings[index] > ratings[index - 1]:
                nums[index] = nums[index - 1] + 1
        for index in range(len(ratings) - 2, -1, -1):
            if ratings[index] > ratings[index + 1]:
                nums[index] = max(nums[index], nums[index + 1] + 1)
        return sum(nums)


"""
贪心水题
"""
