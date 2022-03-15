"""
64. 最小路径和
给定一个包含非负整数的 m x n 网格 grid ，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。
说明：每次只能向下或者向右移动一步。
https://leetcode-cn.com/problems/minimum-path-sum/
"""
from typing import List
import heapq


class Solution:

    # dijkstra solution
    @staticmethod
    def minPathSumDijkstra(grid: List[List[int]]) -> int:
        neighbor = [[0, 1], [1, 0]]
        len_y, len_x = len(grid), len(grid[0])
        seen = [[False] * len_x for _ in range(len_y)]
        seen[0][0] = True
        node_heap = [[grid[0][0], 0, 0]]  # a heap of [accumulated weight, y, x]
        while node_heap:
            val, y, x = heapq.heappop(node_heap)
            if y == len_y - 1 and x == len_x - 1:
                return val
            for delta in neighbor:
                _y, _x = y + delta[0], x + delta[1]
                if _y == len_y - 1 and _x == len_x - 1:
                    return val + grid[_y][_x]
                if _y < len_y and _x < len_x and not seen[_y][_x]:  # valid node
                    heapq.heappush(node_heap, [val + grid[_y][_x], _y, _x])
                    seen[_y][_x] = True

    # dynamic programming solution
    @staticmethod
    def minPathSum(grid: List[List[int]]) -> int:
        len_y, len_x = len(grid), len(grid[0])
        for y in range(len_y):
            for x in range(len_x):
                if y == x == 0:
                    continue
                if y == 0:
                    grid[y][x] = grid[y][x - 1] + grid[y][x]
                elif x == 0:
                    grid[y][x] = grid[y - 1][x] + grid[y][x]
                else:
                    grid[y][x] = min(grid[y - 1][x], grid[y][x - 1]) + grid[y][x]
        return grid[-1][-1]


"""
dijkstra不出意外地很慢，因为没有利用到图作为矩阵的特性
共m*n个节点，每个节点2个出度，最多对这些节点进行m*n次堆操作，堆大小m*n，单次操作时间log(m*n)，总计O(m*n*log(m*n))
很菜！

显然DP算法时间复杂度为O(m*n)，这是由于利用了单向图和出度限制的结果
怎么用了原地算法空间复杂度还是这么高
"""
