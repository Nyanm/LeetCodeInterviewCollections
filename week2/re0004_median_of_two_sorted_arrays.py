from typing import List


class Solution:
    @staticmethod
    def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
        target = (len(nums1) + len(nums2)) // 2
        is_odd = (len(nums1) + len(nums2)) % 2
        left1, left2 = 0, 0

        if not nums1 or not nums2:
            nums = nums1 + nums2
            if is_odd:
                return nums[target]
            else:
                return (nums[target - 1] + nums[target]) / 2

        advance = target
        while True:
            advance = max(min(advance // 2, len(nums1) - left1, len(nums2) - left2), 1)

            if left1 == len(nums1):
                left2 += target
                if is_odd:
                    return nums2[left2]
                else:
                    if left2:
                        return (max(nums2[left2 - 1], nums1[-1]) + nums2[left2]) / 2
                    else:
                        return (nums1[-1] + nums2[left2]) / 2

            if left2 == len(nums2):
                left1 += target
                if is_odd:
                    return nums1[left1]
                else:
                    if left1:
                        return (max(nums1[left1 - 1], nums2[-1]) + nums1[left1]) / 2
                    else:
                        return (nums2[-1] + nums1[left1]) / 2

            if not target:
                break

            if nums1[left1 + advance - 1] > nums2[left2 + advance - 1]:
                left2 += advance
            else:
                left1 += advance

            target -= advance

        if is_odd:
            return min(nums1[left1], nums2[left2])
        else:
            if left1 and left2:
                return (max(nums1[left1 - 1], nums2[left2 - 1]) + min(nums1[left1], nums2[left2])) / 2
            elif left1:
                return (nums1[left1 - 1] + min(nums1[left1], nums2[left2])) / 2
            else:
                return (nums2[left2 - 1] + min(nums1[left1], nums2[left2])) / 2


"""
TAG 二分
O(log(m+n)) 本质上在两个表上的二分查找

在这里应该建立起从题目条件中寻找答案的意识，比如说题目中给出了有序数组，那么十有八九就需要用二分来得到答案

回看范例代码，比自己的简洁出一个数量级（
测试例真阴间啊
"""
