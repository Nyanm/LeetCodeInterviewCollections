"""
编写一个算法来判断一个数 n 是不是快乐数。
「快乐数」定义为：
对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和。
然后重复这个过程直到这个数变为 1，也可能是 无限循环 但始终变不到 1。
如果这个过程 结果为1，那么这个数就是快乐数。
如果 n 是 快乐数 就返回 true ；不是，则返回 false 。
https://leetcode-cn.com/problems/happy-number
"""


class Solution:
    @staticmethod
    def isHappy(n: int) -> bool:
        unhappy = {4, 16, 37, 58, 89, 145, 42, 20}
        while n is not 1:
            str_n = str(n)
            new_n = 0
            for char in str_n:
                new_n += int(char) ** 2
            if new_n in unhappy:
                return False
            n = new_n
        return True


"""
写得最快的一道题
本质脑筋急转弯查表秒一切
想起那个著名的“3X+1猜想”
"""
