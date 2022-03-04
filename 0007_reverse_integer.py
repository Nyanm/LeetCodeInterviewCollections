"""
给你一个 32 位的有符号整数 x ，返回将 x 中的数字部分反转后的结果。
如果反转后整数超过 32 位的有符号整数的范围[−231, 231− 1] ，就返回 0。
假设环境不允许存储 64 位整数（有符号或无符号）。
https://leetcode-cn.com/problems/reverse-integer
"""
import numpy as np


class Solution:
    @staticmethod
    def reverse(x: int) -> int:
        try:
            x = np.int32(x)
            if 0 < x:
                x = str(x)[::-1]
                x = np.int32(x)
                return int(x)
            elif x < 0:
                x = str(abs(x))[::-1]
                x = - np.int32(x)
                return int(x)
            else:
                return 0
        except OverflowError:
            return 0

    @staticmethod
    def _reverse(x: int) -> int:
        if 0 < x < 2 ** 31 - 1:
            x = str(x)[::-1]
            x = int(x)
            if x < 2 ** 31 - 1:
                return x
            else:
                return 0
        elif -2 ** 31 < x < 0:
            x = str(abs(x))[::-1]
            x = -int(x)
            if x > -2 ** 31:
                return x
            else:
                return 0
        else:
            return 0

# LeetCode编译器居然会把放不进int32的数揉吧揉吧放进去然后腆着脸报错，谔谔
