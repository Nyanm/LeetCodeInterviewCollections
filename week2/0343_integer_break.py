"""
给定一个正整数 n ，将其拆分为 k 个 正整数 的和（ k >= 2 ），并使这些整数的乘积最大化。
返回 你可以获得的最大乘积 。
"""


class Solution:
    @staticmethod
    def integerBreak(n: int) -> int:
        if n < 4:
            return n - 1
        cnt_3, remains = n // 3, n % 3
        if not remains:
            return 3 ** cnt_3
        elif remains == 1:
            cnt_3 -= 1
            cnt_2 = 2
        else:
            cnt_2 = 1
        return 3 ** cnt_3 * 2 ** cnt_2


"""
你以为是动规题，其实是一道脑筋急转弯
提示说有O(n)解，实际上有O(1)解，也不失为一种幽默
"""
