"""
260. 只出现一次的数字 III
给定一个整数数组 nums，其中恰好有两个元素只出现一次，其余所有元素均出现两次。 找出只出现一次的那两个元素。你可以按 任意顺序 返回答案。
进阶：你的算法应该具有线性时间复杂度。你能否仅使用常数空间复杂度来实现？
https://leetcode-cn.com/problems/single-number-iii
"""
from typing import List


class Solution:
    @staticmethod
    def singleNumber(nums: List[int]) -> List[int]:
        # calculate the XOR result of them all, which revels the differences between those two special numbers
        xor_res = 0
        for num in nums:
            xor_res = xor_res ^ num
        bit_1 = 0
        # get lowermost bit "1"
        while not xor_res % 2:
            xor_res = xor_res >> 1
            bit_1 += 1
        # divide them into two different groups
        xor_0, xor_1 = 0, 0
        for num in nums:
            if (num >> bit_1) % 2:
                xor_1 = xor_1 ^ num
            else:
                xor_0 = xor_0 ^ num
        return [xor_0, xor_1]


"""
好难一题目，尽管做了前两道不同数字，遇到这一题还是一点思路也没有
位运算，真的很强大！
"""
