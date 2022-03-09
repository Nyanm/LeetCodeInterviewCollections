"""
给定整数数组 nums 和整数 k，请返回数组中第 k 个最大的元素。
请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。
https://leetcode-cn.com/problems/kth-largest-element-in-an-array/
"""
from typing import List
import heapq


class Solution:
    @staticmethod
    def findKthLargest(nums: List[int], k: int) -> int:
        min_heap = []
        for index in range(len(nums)):
            if len(min_heap) < k:
                heapq.heappush(min_heap, nums[index])
                continue
            if min_heap[0] < nums[index]:
                heapq.heappop(min_heap)
                heapq.heappush(min_heap, nums[index])

        return min_heap[0]


"""
一眼堆
"""
