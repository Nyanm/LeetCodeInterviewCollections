"""
以数组 intervals 表示若干个区间的集合，其中单个区间为 intervals[i] = [starti, endi] 。
请你合并所有重叠的区间，并返回一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间。
https://leetcode-cn.com/problems/merge-intervals
"""
from typing import List


class Solution:
    @staticmethod
    def merge(intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        ans = [intervals[0]]
        for index in range(1, len(intervals)):
            if intervals[index][0] <= ans[-1][1]:
                ans[-1][1] = max(ans[-1][1], intervals[index][1])
            else:
                ans.append(intervals[index])
        return ans


"""
最开始还想过拉一张表遍历来做……
题解很有意思，我是笨比
"""
