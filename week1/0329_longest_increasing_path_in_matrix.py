"""
给定一个m x n 整数矩阵matrix ，找出其中 最长递增路径 的长度。
对于每个单元格，你可以往上，下，左，右四个方向移动。 你 不能 在 对角线 方向上移动或移动到 边界外（即不允许环绕）。
https://leetcode-cn.com/problems/longest-increasing-path-in-a-matrix
"""
from typing import List
import numpy as np


class Solution:
    @staticmethod
    def longestIncreasingPath(matrix: List[List[int]]) -> int:
        len_m, len_n = len(matrix), len(matrix[0])
        route_table = np.zeros((len_m, len_n), dtype=int)
        ori_list = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        max_cnt = 1

        def dfs(__m, __n):
            nonlocal max_cnt

            for ori in ori_list:
                nei_m = __m + ori[0]
                nei_n = __n + ori[1]

                if nei_m < 0 or nei_m >= len_m or nei_n < 0 or nei_n >= len_n:
                    continue
                if matrix[nei_m][nei_n] <= matrix[__m][__n]:
                    continue

                if not route_table[nei_m][nei_n]:
                    dfs(nei_m, nei_n)
                route_table[__m][__n] = max(route_table[__m][__n], route_table[nei_m][nei_n] + 1)
                max_cnt = max(max_cnt, route_table[__m][__n])

            if not route_table[__m][__n]:
                route_table[__m][__n] = 1  # 打则死路一条
                return

        for m in range(len_m):
            for n in range(len_n):
                if route_table[m][n]:
                    continue
                else:
                    dfs(m, n)

        return max_cnt

# 顺畅，很爽
