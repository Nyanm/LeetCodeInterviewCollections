"""
一个机器人位于一个 m x n网格的左上角 （起始点在下图中标记为 “Start” ）。
机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为 “Finish” ）。
问总共有多少条不同的路径？
https://leetcode-cn.com/problems/unique-paths
"""


class Solution:
    @staticmethod
    def uniquePaths(m: int, n: int) -> int:
        if m == 1 or n == 1:
            return 1
        memo = [[1] * m for _ in range(n)]
        for outer in range(1, n):
            for inner in range(1, m):
                memo[outer][inner] = memo[outer - 1][inner] + memo[outer][inner - 1]
        return memo[-1][-1]


"""
前略，画图找规律
高中数学概率题写过一万道这种路径数，可惜现在是一点也想不起来了
最后DP的成绩比求组合的成绩好得多，盲猜是因为阶乘是个特别费时间的运算
"""
