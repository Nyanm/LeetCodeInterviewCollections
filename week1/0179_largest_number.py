"""
给定一组非负整数 nums，重新排列每个数的顺序（每个数不可拆分）使之组成一个最大的整数。
注意：输出结果可能非常大，所以你需要返回一个字符串而不是整数。
https://leetcode-cn.com/problems/largest-number/
"""
from typing import List
from functools import cmp_to_key


class Solution:
    @staticmethod
    def largestNumber(nums: List[int]) -> str:

        def get_larger(a: int, b: int) -> int:
            a, b = str(a), str(b)
            ab, ba = int(a + b), int(b + a)

            if ab < ba:
                return 1
            elif ab > ba:
                return -1
            else:
                return 0

        nums.sort(key=cmp_to_key(get_larger))
        large = ''
        for num in nums:
            large += str(num)
        if large[0] == '0':
            return '0'
        return large


"""
学到一招用functools.cmp_to_key客制化sort()的方法
最开始以为是贪心，结果确实是贪心，是不过不是我想的那种贪法
"""
