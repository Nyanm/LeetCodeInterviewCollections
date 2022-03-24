"""
70. 爬楼梯
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
https://leetcode-cn.com/problems/climbing-stairs/
"""


class Solution:
    @staticmethod
    def climbStairs(n: int) -> int:
        if n <= 2:
            return n
        memo = [0, 1, 2]
        for index in range(3, n + 1):
            memo[index % 3] = memo[(index - 2) % 3] + memo[(index - 1) % 3]
        return memo[index % 3]


"""
基本DP+滚动数组
尝试一下速刷简单题，尽量压缩时间和代码量
"""
