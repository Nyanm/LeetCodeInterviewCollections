"""
给你一个整数数组 nums，有一个大小为k的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 k个数字。滑动窗口每次只向右移动一位。
返回 滑动窗口中的最大值 。
https://leetcode-cn.com/problems/sliding-window-maximum
"""
from typing import List


class Solution:
    @staticmethod
    def maxSlidingWindow(nums: List[int], k: int) -> List[int]:
        mono_queue = []
        ans = []

        if k == 1:
            return nums

        def add(__index):
            nonlocal mono_queue

            if not mono_queue:
                mono_queue.append(__index)
                return

            if len(mono_queue) == k:
                mono_queue.pop(0)

            while nums[__index] > nums[mono_queue[-1]]:
                mono_queue.pop()
                if not mono_queue:
                    break

            mono_queue.append(__index)

        for index in range(len(nums)):
            add(index)
            if index < k - 1:
                continue
            if mono_queue[0] < index - (k - 1):
                mono_queue.pop(0)
            ans.append(nums[mono_queue[0]])

        return ans


"""
len(iterable) = iterable.__len__  即调用可迭代对象的长度时间复杂度为O(1)
以前一直以为要遍历一遍来着

测试例好大，跑了八秒一度以为自己要凉了
"""
