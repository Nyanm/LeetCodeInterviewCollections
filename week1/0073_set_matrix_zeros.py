"""
给定一个 m x n 的矩阵，如果一个元素为 0 ，则将其所在行和列的所有元素都设为 0 。请使用 原地 算法。
https://leetcode-cn.com/problems/set-matrix-zeroes/
"""


from typing import List


class Solution:
    @staticmethod
    def setZeroes(matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        is_line, is_row = 0, 0
        if not matrix[0][0]:
            is_line = is_row = 0
        lines, rows = len(matrix), len(matrix[0])

        for line in range(lines):
            for row in range(rows):
                if matrix[line][row] == 0:
                    if line == 0:
                        is_line = 1
                    if row == 0:
                        is_row = 1
                    matrix[0][row] = matrix[line][0] = 0

        if lines == rows == 1:
            return
        elif lines > 1 and rows > 1:
            for line_sign in range(1, lines):
                if matrix[line_sign][0] == 0:
                    for index in range(rows):
                        matrix[line_sign][index] = 0
            for row_sign in range(1, rows):
                if matrix[0][row_sign] == 0:
                    for index in range(lines):
                        matrix[index][row_sign] = 0
        if is_line:
            for index in range(rows):
                matrix[0][index] = 0
        if is_row:
            for index in range(lines):
                matrix[index][0] = 0

# 热泪盈眶，被鞭打了这么久终于有一个一次过了
