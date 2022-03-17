"""
240. 搜索二维矩阵 II
编写一个高效的算法来搜索 m x n 矩阵 matrix 中的一个目标值 target 。该矩阵具有以下特性：
每行的元素从左到右升序排列。
每列的元素从上到下升序排列。
https://leetcode-cn.com/problems/search-a-2d-matrix-ii
"""
from typing import List


class Solution:
    @staticmethod
    def searchMatrix(matrix: List[List[int]], target: int) -> bool:
        y_len, x_len = len(matrix), len(matrix[0])
        y, x = y_len - 1, 0
        while y >= 0 and x < x_len:
            if target > matrix[y][x]:
                x += 1
            elif target < matrix[y][x]:
                y -= 1
            else:
                return True
        return False


"""
脑筋急转弯
"""
