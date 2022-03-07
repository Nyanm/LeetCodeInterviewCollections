"""
给你一个m * n的网格，其中每个单元格不是0（空）就是1（障碍物）。每一步，您都可以在空白单元格中上、下、左、右移动。
如果您 最多 可以消除 k 个障碍物，请找出从左上角 (0, 0) 到右下角 (m-1, n-1) 的最短路径，并返回通过该路径所需的步数。如果找不到这样的路径，则返回 -1。
https://leetcode-cn.com/problems/shortest-path-in-a-grid-with-obstacles-elimination
"""
from typing import List


class Solution:
    @staticmethod
    def shortestPath(grid: List[List[int]], k: int) -> int:
        len_x, len_y = len(grid[0]), len(grid)
        if len_x == 1 and len_y == 1:
            return 0
        k = min(k, len_y + len_x - 3)
        node_queue = [[0, 0, k]]
        directions = ((-1, 0), (1, 0), (0, -1), (0, 1))
        seen = {(0, 0, k)}
        cnt = 0

        while node_queue:
            new_queue = []
            cnt += 1

            for node in node_queue:
                node_y, node_x, node_k = node

                for dy, dx in directions:
                    y, x = node_y + dy, node_x + dx

                    if 0 <= y < len_y and 0 <= x < len_x:
                        if not grid[y][x] and (y, x, node_k) not in seen:
                            if y == len_y - 1 and x == len_x - 1:
                                return cnt
                            new_queue.append([y, x, node_k])
                            seen.add((y, x, node_k))
                        elif grid[y][x] and node_k > 0 and (y, x, node_k - 1) not in seen:
                            new_queue.append([y, x, node_k - 1])
                            seen.add((y, x, node_k - 1))

            node_queue = new_queue
        return -1


"""
对着题解看了半天才发现是边界条件写错一条，造成数据量爆炸
好笑的是即使这样多跑一会也能得出正确答案
"""
