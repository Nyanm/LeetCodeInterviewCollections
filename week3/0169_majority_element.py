"""
给定一个大小为 n 的数组，找到其中的多数元素。多数元素是指在数组中出现次数 大于 n // 2 的元素。
你可以假设数组是非空的，并且给定的数组总是存在多数元素。
https://leetcode-cn.com/problems/majority-element
"""
from typing import List


class Solution:
    @staticmethod
    def majorityElementMoore(nums: List[int]) -> int:
        cnt, majority = 0, 0
        for index in range(len(nums)):
            if not cnt:
                majority = nums[index]
                cnt += 1
                continue
            if majority == nums[index]:
                cnt += 1
            else:
                cnt -= 1
        return majority

    @staticmethod
    def majorityElement(nums: List[int]) -> int:

        def search(left: int, right: int) -> int:
            nonlocal nums
            if left == right:
                return nums[left]
            mid = (right - left) // 2 + left
            bisect_left = search(left, mid)
            bisect_right = search(mid + 1, right)
            if bisect_right == bisect_left:
                return bisect_left

            left_cnt, right_cnt = 0, 0
            for index in range(left, right + 1):
                left_cnt += (nums[index] == bisect_left)
                right_cnt += (nums[index] == bisect_right)
            return bisect_left if left_cnt > right_cnt else bisect_right

        return search(0, len(nums) - 1)


"""
二分法很有意思
Boyer-Moore投票算法纯纯的脑筋急转弯
随机法纯纯的[BUY SOME APPLES]
"""
