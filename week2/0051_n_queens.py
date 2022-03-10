"""
n 皇后问题 研究的是如何将 n个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。
给你一个整数 n ，返回所有不同的 n 皇后问题 的解决方案。
每一种解法包含一个不同的 n 皇后问题 的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。
https://leetcode-cn.com/problems/n-queens
"""
from typing import List


class Solution:
    @staticmethod
    def solveNQueens(n: int) -> List[List[str]]:

        # — (0, k), | (1, k), \ (2, k), / (3, k)
        seen = [[False] * (2 * n - 1) for _ in range(4)]
        x_initial = 0
        board = ['.' * n for _ in range(n)]
        ans = []

        def search(y: int, x: int):
            nonlocal seen, cur_board
            if seen[0][y] or seen[2][y + x] or seen[3][y - x]:
                return
            else:
                seen[0][y] = seen[2][y + x] = seen[3][y - x] = True
                cur_board[y] = '.' * x + 'Q' + '.' * (n - x - 1)
                if x == n - 1:
                    ans.append(cur_board[:])
                else:
                    for y_next in range(n):
                        search(y_next, x + 1)
                seen[0][y] = seen[2][y + x] = seen[3][y - x] = False
                cur_board[y] = '.' * n

        for y_initial in range(n):
            cur_board = board[:]
            search(y_initial, x_initial)

        return ans


"""
Queen Nyanm (不是
很漂亮的题目
最开始推了一遍发现复杂度是O(n!)还以为自己想错了，一对答案果然是这么个离谱的数值
"""
