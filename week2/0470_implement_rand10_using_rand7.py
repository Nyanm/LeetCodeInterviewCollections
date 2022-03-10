"""
给定方法rand7 可生成 [1,7] 范围内的均匀随机整数，试写一个方法 rand10 生成 [1,10] 范围内的均匀随机整数。
你只能调用 rand7() 且不能调用其他方法。请不要使用系统的 Math.random() 方法。
每个测试用例将有一个内部参数 n，即你实现的函数 rand10() 在测试时将被调用的次数。请注意，这不是传递给 rand10() 的参数。
https://leetcode-cn.com/problems/implement-rand10-using-rand7
"""
from random import randint


# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7
def rand7() -> int:
    return randint(1, 7)


class Solution:
    @staticmethod
    def rand10() -> int:
        cur = 100
        check_up = {
            11: 1, 12: 2, 13: 3, 14: 4, 15: 5, 16: 6, 17: 7, 21: 8, 22: 9, 23: 10,
            24: 1, 25: 2, 26: 3, 27: 4, 31: 5, 32: 6, 33: 7, 34: 8, 35: 9, 36: 10,
            37: 1, 41: 2, 42: 3, 43: 4, 44: 5, 45: 6, 46: 7, 47: 8, 51: 9, 52: 10,
            53: 1, 54: 2, 55: 3, 56: 4, 57: 5, 61: 6, 62: 7, 63: 8, 64: 9, 65: 10
        }
        while cur > 65:
            cur = rand7() + 10 * rand7()
        return check_up[cur]


"""
打表好累
"""
