"""
63. 不同路径 II
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为 “Start” ）。
机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为 “Finish”）。
现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？
网格中的障碍物和空位置分别用 1 和 0 来表示。
https://leetcode-cn.com/problems/unique-paths-ii
"""
from functools import reduce
from typing import List


class Solution:
    @staticmethod
    def uniquePathsWithObstacles(obstacleGrid: List[List[int]]) -> int:
        y_len, x_len = len(obstacleGrid), len(obstacleGrid[0])
        y_initial, x_initial = 0, 1
        if obstacleGrid[0][0]:
            return 0
        if y_len == 1 or x_len == 1:
            return int(sum(reduce(lambda _x, _y: _x + _y, obstacleGrid)) == 0)
        while y_initial < y_len and not obstacleGrid[y_initial][0]:
            obstacleGrid[y_initial][0] = -1
            y_initial += 1
        while x_initial < x_len and not obstacleGrid[0][x_initial]:
            obstacleGrid[0][x_initial] = -1
            x_initial += 1
        for y in range(1, y_len):
            for x in range(1, x_len):
                if obstacleGrid[y][x]:
                    continue
                obstacleGrid[y][x] = (obstacleGrid[y - 1][x] != 1) * obstacleGrid[y - 1][x] + \
                                     (obstacleGrid[y][x - 1] != 1) * obstacleGrid[y][x - 1]
        return -min(obstacleGrid[-1][-1], 0)


"""
敲错一个参数导致，重新提交五次
实现了空间复杂度O(1)的原地算法
"""
