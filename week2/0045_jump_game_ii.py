"""
45. 跳跃游戏 II
给你一个非负整数数组 nums ，你最初位于数组的第一个位置。
数组中的每个元素代表你在该位置可以跳跃的最大长度。
你的目标是使用最少的跳跃次数到达数组的最后一个位置。
假设你总是可以到达数组的最后一个位置。
https://leetcode-cn.com/problems/jump-game-ii
"""
from typing import List


class Solution:

    # dijkstra solution, O(n^2)
    @staticmethod
    def jump_sp(nums: List[int]) -> int:
        if len(nums) <= 1:
            return 0
        stack, cnt = [0], 0
        nums[0] *= -1
        while stack:
            new_stack = []
            cnt += 1
            for node in stack:
                for index in range(node, node - nums[node] + 1):
                    if index >= len(nums) - 1:
                        return cnt
                    if index < len(nums) and nums[index] > 0:
                        nums[index] *= -1
                        new_stack.append(index)
            stack = new_stack
            # stack.sort(key=lambda x: x - nums[x])

    # greedy solution, O(n)
    @staticmethod
    def jump(nums: List[int]) -> int:
        border, next_border, cnt = 0, nums[0], 0
        for index in range(len(nums)):
            if index > border:
                border = next_border
                cnt += 1
            if index == len(nums) - 1:
                return cnt
            next_border = max(next_border, index + nums[index])
        return cnt


"""
拿到题目瞬间想到了权重为1的最短路算法
dijkstra解，最坏情况下需要对N个点查看N次，时间复杂度O(N^2)——尽管它们只会被标记一次
考虑到每个节点的出度有限，平均时间复杂度为O(N^(mean(nums)))

贪心解维护一个“范围”，感觉和 56 合并区间 的思想很像
很牛！
"""
