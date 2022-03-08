"""
给定一个长度为 n 的整数数组height。有n条垂线，第 i 条线的两个端点是(i, 0)和(i, height[i])。
找出其中的两条线，使得它们与x轴共同构成的容器可以容纳最多的水。
返回容器可以储存的最大水量。
说明：你不能倾斜容器。
https://leetcode-cn.com/problems/container-with-most-water
"""
from typing import List


class Solution:
    @staticmethod
    def maxArea(height: List[int]) -> int:
        length = len(height)
        left, right = 0, length - 1
        volume = 0

        while right > left:
            volume = max(min(height[left], height[right]) * (right - left), volume)
            if height[left] >= height[right]:
                right -= 1
            else:
                left += 1

        return volume


"""
乍一看像是 42 接雨水 一类的单调栈问题，结果是个双指针
答案很容易出，证明要花点心思
"""
