"""
给你一个整数数组 nums 和一个整数 k ，请你返回其中出现频率前 k 高的元素。你可以按 任意顺序 返回答案。
https://leetcode-cn.com/problems/top-k-frequent-elements/
"""
from typing import List
import heapq


class Solution:
    @staticmethod
    def topKFrequent(nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            if not freq.__contains__(num):
                freq[num] = 1
            else:
                freq[num] += 1

        cnt, heap = 0, []
        for key, val in freq.items():
            if cnt < k:
                heapq.heappush(heap, [val, key])
                cnt += 1
            else:
                if val > heap[0][0]:
                    heapq.heappop(heap)
                    heapq.heappush(heap, [val, key])
        return [heap[index][1] for index in range(len(heap))]


"""
口口声声说用堆维护出现次数速度更快，结果RT最低的答案都是直接跑的sort，多少有点黑色幽默了
"""
