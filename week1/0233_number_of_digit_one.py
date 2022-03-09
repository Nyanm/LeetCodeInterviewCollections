"""
给定一个整数 n，计算所有小于等于 n 的非负整数中数字 1 出现的个数。
https://leetcode-cn.com/problems/number-of-digit-one/
"""


class Solution:
    @staticmethod
    def countDigitOne(n: int) -> int:
        length = len(str(n))
        cnt_1, res = 0, 0
        for dig in range(length - 1, -1, -1):
            base = 10 ** dig
            num = n // base
            n = n % base

            # high digits
            if dig > 0:
                res += cnt_1 * num * base
            if dig == 0:
                res += cnt_1 * (num + 1)

            # self digit
            if num > 1:
                res += base
            if num == 1 and dig == 0:
                res += 1

            # low digits
            res += dig * (10 ** (dig - 1)) * num

            if num == 1:
                cnt_1 += 1

        return int(res)


"""
写了好几个小时的劲爆大题……人都给写麻了
算法什么的只能图一乐，真难题还得看数学题
"""
