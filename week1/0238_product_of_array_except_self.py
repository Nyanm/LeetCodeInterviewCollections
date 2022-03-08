"""
给你一个整数数组nums，返回 数组answer，其中answer[i]等于nums中除nums[i]之外其余各元素的乘积。
题目数据 保证 数组nums之中任意元素的全部前缀元素和后缀的乘积都在 32 位 整数范围内。
请不要使用除法，且在O(n) 时间复杂度内完成此题。
https://leetcode-cn.com/problems/product-of-array-except-self
"""
from typing import List


class Solution:
    @staticmethod
    def productExceptSelf(nums: List[int]) -> List[int]:
        length = len(nums)
        ans = [1] * length
        rtl, ltr = 1, 1
        for index in range(length - 1):
            rtl *= nums[-index - 1]
            ltr *= nums[index]

            ans[index + 1] *= ltr
            ans[-index - 2] *= rtl

        return ans


"""
看了眼前缀和原理画下图就懂了
还推出了O(1)空间解，舒畅
"""
