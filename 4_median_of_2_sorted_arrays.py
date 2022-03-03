"""
给定两个大小分别为 m 和 n 的正序（从小到大）数组nums1 和nums2。请你找出并返回这两个正序数组的 中位数 。
算法的时间复杂度应该为 O(log (m+n)) 。
https://leetcode-cn.com/problems/median-of-two-sorted-arrays
"""
from typing import List


class Solution:
    @staticmethod
    def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
        len1, len2 = len(nums1), len(nums2)
        length = len1 + len2

        def get_target(target):
            index1 = index2 = 0
            while True:
                # marginal check
                if index1 == len1:
                    return nums2[index2 + target - 1]
                if index2 == len2:
                    return nums1[index1 + target - 1]
                if target == 1:
                    return min(nums1[index1], nums2[index2])

                size = target // 2 - 1
                _index1 = min(index1 + size, len1 - 1)
                _index2 = min(index2 + size, len2 - 1)
                if nums1[_index1] > nums2[_index2]:
                    target -= _index2 - index2 + 1
                    index2 = _index2 + 1
                else:
                    target -= _index1 - index1 + 1
                    index1 = _index1 + 1

                # print(f"target:{target}, _index1:{_index1}, _index2:{_index2}, index1:{index1}, index2:{index2}")

        if length % 2:
            return get_target(length // 2 + 1)
        else:
            return (get_target(length // 2) + get_target(length // 2 + 1)) / 2

# 太狠了这题，折磨了两个小时
# 自己写全是问题，照着范例代码改，改着改着就改成李鬼了
# 深刻感受到自己算法力与代码力的双重不足
