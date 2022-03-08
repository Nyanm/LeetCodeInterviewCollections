"""
给定一个整数 n ，返回 n! 结果中尾随零的数量。
提示 n! = n * (n - 1) * (n - 2) * ... * 3 * 2 * 1
https://leetcode-cn.com/problems/factorial-trailing-zeroes/
"""
from math import factorial


class Solution:
    @staticmethod
    def trailingZeroes(n: int) -> int:
        cnt = 0
        while n >= 5:
            n = n // 5
            cnt += n
        return cnt


"""
到现在为止最短小的题目
本质脑筋急转弯
"""
