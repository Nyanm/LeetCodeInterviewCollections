"""
279. 完全平方数
给你一个整数 n ，返回 和为 n 的完全平方数的最少数量 。
完全平方数 是一个整数，其值等于另一个整数的平方；换句话说，其值等于一个整数自乘的积。例如，1、4、9 和 16 都是完全平方数，而 3 和 11 不是。
https://leetcode-cn.com/problems/perfect-squares
"""
from math import sqrt


class Solution:

    # DP(backpack) solution - timeout
    @staticmethod
    def numSquaresDP(n: int) -> int:
        memo = [0] * (n + 1)
        for index in range(1, n + 1):
            min_cnt, inner = 5, 1
            while inner ** 2 <= index:
                min_cnt = min(min_cnt, memo[index - inner ** 2] + 1)
                inner += 1
            memo[index] = min_cnt

        return memo[-1]

    # Lagrange's four-square theorem solution
    @staticmethod
    def numSquares(n: int) -> int:
        # perfect square
        if int(sqrt(n)) ** 2 == n:
            return 1
        # sum of 4 perfect square numbers
        _n = n
        while not _n % 4:
            _n //= 4
        if not (_n - 7) % 8:
            return 4
        # now we have two answers: 2 or 3
        # check the validity of 2, meanwhile we can verify the answer 3
        index = 1
        while index ** 2 <= n:
            another = n - index ** 2
            if int(sqrt(another)) ** 2 == another:
                return 2
            index += 1
        return 3


"""
DP超时？？？
拉格朗日四平方数定理太偏门了，要是不看题解这辈子也做不出来
"""
