"""
给你一个整数数组 nums，请你找出数组中乘积最大的非空连续子数组（该子数组中至少包含一个数字），并返回该子数组所对应的乘积。
测试用例的答案是一个32-位 整数。
子数组 是数组的连续子序列。
https://leetcode-cn.com/problems/maximum-product-subarray
"""

from typing import List


class Solution:
    # Double index solution
    # Failed
    @staticmethod
    def _maxProduct(nums: List[int]) -> int:
        length = len(nums)
        front, back = 1, 0
        product = nums[0]
        max_product = product
        if length < 2:
            return product
        while back < length:

            if front >= length:
                advance = product
            else:
                advance = product * nums[front]

            if (front - back) > 1:
                if back == length - 1:  # last element
                    draw = nums[-1]
                elif product:  # non 0 array
                    draw = product / nums[back]
                elif nums[back]:  # hidden 0 in array
                    draw = product
                else:
                    draw = nums[back]
                    for index in range(back + 1, min(front, length)):
                        draw *= nums[index]
            else:
                draw = - 2 ** 31

            if advance >= draw:
                product = advance
                front += 1
                if front > length:
                    back += 1
            else:
                product = draw
                back += 1
            max_product = max(product, max_product)
            print(f'front:{front}, back:{back}, advance:{advance}, draw:{draw}')

        return int(max_product)

    @staticmethod
    def maxProduct(nums: List[int]) -> int:
        max_product = nums[0]
        min_cur, max_cur = nums[0], nums[0]
        for index in range(1, len(nums)):
            max_temp, min_temp = max_cur, min_cur
            max_cur = max(max_temp * nums[index], min_temp * nums[index], nums[index])
            min_cur = min(max_temp * nums[index], min_temp * nums[index], nums[index])
            max_product = max(max_product, max_cur)
            # print(f'index[{index}]:{nums[index]}, max cur:{max_cur}, min_cur:{min_cur}, product:{max_product}')
        return max_product


"""
我是笨比，个动规写了这么久还绕死胡同里了，疯狂抓边界条件
"""
