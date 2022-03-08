"""
给定一个包含 m × n个格子的面板，每一个格子都可以看成是一个细胞。每个细胞都具有一个初始状态： 1 即为 活细胞 （live），或 0 即为 死细胞 （dead）。每个细胞与其八个相邻位置（水平，垂直，对角线）的细胞都遵循以下四条生存定律：
如果活细胞周围八个位置的活细胞数少于两个，则该位置活细胞死亡；
如果活细胞周围八个位置有两个或三个活细胞，则该位置活细胞仍然存活；
如果活细胞周围八个位置有超过三个活细胞，则该位置活细胞死亡；
如果死细胞周围正好有三个活细胞，则该位置死细胞复活；
下一个状态是通过将上述规则同时应用于当前状态下的每个细胞所形成的，其中细胞的出生和死亡是同时发生的。给你 m x n 网格面板 board 的当前状态，返回下一个状态。
https://leetcode-cn.com/problems/game-of-life
"""
from typing import List


class Solution:
    @staticmethod
    def gameOfLife(board: List[List[int]]) -> None:
        len_y, len_x = len(board), len(board[0])
        nei_x = [-1, 0, 1, 1, 1, 0, -1, -1]
        nei_y = [1, 1, 1, 0, -1, -1, -1, 0]
        """
        Cell code:
        0 Normal dead cell
        1 Normal living cell
        2 Reincarnated cell
        3 Dying cell
        """
        for x in range(len_x):
            for y in range(len_y):

                alive_cnt = 0
                status = board[y][x]

                for index in range(8):
                    cur_x, cur_y = x + nei_x[index], y + nei_y[index]
                    if cur_x < 0 or cur_x >= len_x or cur_y < 0 or cur_y >= len_y:
                        continue
                    if board[cur_y][cur_x] in (1, 3):
                        alive_cnt += 1

                if status == 1:  # Living cell
                    if alive_cnt < 2 or alive_cnt > 3:
                        board[y][x] = 3
                    else:
                        board[y][x] = 1
                else:  # Dead cell
                    if alive_cnt == 3:
                        board[y][x] = 2
                    else:
                        board[y][x] = 0

        for x in range(len_x):
            for y in range(len_y):
                status = board[y][x]
                if status == 2:
                    board[y][x] = 1
                elif status == 3:
                    board[y][x] = 0

# "执行用时：48 ms , 在所有 Python3 提交中击败了 8.47% 的用户"
# 笑死
