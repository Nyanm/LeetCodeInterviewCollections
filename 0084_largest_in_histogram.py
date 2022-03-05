"""
给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。
求在该柱状图中，能够勾勒出来的矩形的最大面积。
https://leetcode-cn.com/problems/largest-rectangle-in-histogram/
"""
from typing import List


class Solution:
    @staticmethod
    def largestRectangleArea(heights: List[int]) -> int:
        mono_stack = [0]  # list of [value, index]
        length = len(heights)
        frontier = [[None, None] for _ in range(length + 2)]  # list of [Left, Right] frontier
        heights = [-1] + heights + [-1]

        for index in range(1, length + 1):
            if heights[index] >= heights[mono_stack[-1]]:
                mono_stack.append(index)
                frontier[index][0] = index
            else:
                while heights[index] < heights[mono_stack[-1]]:
                    bigger = mono_stack.pop()
                    frontier[bigger][1] = index
                frontier[index][0] = mono_stack[-1] + 1
                mono_stack.append(index)

        area = 0
        for index in range(1, length + 1):
            left, right = frontier[index]
            if not right:
                right = length + 1
            area = max(area, (right - left) * heights[index])

        return area


"""
单调栈玩的好花
monotonic adj. [数]单调的；没有变化的
大家代码都是穿一条裤子的，怎么我的就跑得这么慢
"""
