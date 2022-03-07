"""
给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
https://leetcode-cn.com/problems/trapping-rain-water/
"""
from typing import List


class Solution:
    @staticmethod
    def trap(height: List[int]) -> int:
        rain = 0
        length = len(height)
        left, right = [None] * length, [None] * length
        mono_stack = []  # a stack with indexes

        for index in range(length):
            if mono_stack:  # left border
                if height[index] <= height[mono_stack[-1]]:  # push smoothly
                    left[index] = mono_stack[-1]
                    mono_stack.append(index)
                else:
                    while True:
                        if not mono_stack:
                            mono_stack.append(index)  # a lethal diarrhea
                            break
                        if height[index] > height[mono_stack[-1]]:  # pop until monotone
                            smaller = mono_stack.pop()
                            right[smaller] = index
                        else:
                            left[index] = mono_stack[-1]
                            mono_stack.append(index)  # push this bulk element
                            break
            else:
                mono_stack.append(index)  # new highest element, no border

        for index in range(1, length):
            if left[index - 1] is not None and left[index] is not None:
                left[index] = left[index - 1]
            if right[length - index] is not None and right[length - index - 1] is not None:
                right[length - index - 1] = right[length - index]

        for index in range(length):
            if left[index] is not None and right[index] is not None:
                rain += min(height[left[index]] - height[index], height[right[index]] - height[index])

        return rain


"""
手撕一道困难，从0开始画图推动态规划条件
很有成就感！
"""
