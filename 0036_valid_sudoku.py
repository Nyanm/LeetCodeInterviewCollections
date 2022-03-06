"""
请你判断一个9 x 9 的数独是否有效。只需要 根据以下规则 ，验证已经填入的数字是否有效即可。

数字1-9在每一行只能出现一次。
数字1-9在每一列只能出现一次。
数字1-9在每一个以粗实线分隔的3x3宫内只能出现一次。（请参考示例图）

注意：
一个有效的数独（部分已被填充）不一定是可解的。
只需要根据以上规则，验证已经填入的数字是否有效即可。
空白格用'.'表示。
https://leetcode-cn.com/problems/valid-sudoku
"""
from typing import List


class Solution:
    @staticmethod
    def isValidSudoku(board: List[List[str]]) -> bool:
        for outer in range(9):
            valid_cache = [[False] * 9 for _ in range(3)]

            for inner in range(9):
                # line check
                val = board[outer][inner]
                if val != '.':
                    if valid_cache[0][int(val) - 1]:
                        return False
                    valid_cache[0][int(val) - 1] = True

                # row check
                val = board[inner][outer]
                if val != '.':
                    if valid_cache[1][int(val) - 1]:
                        return False
                    valid_cache[1][int(val) - 1] = True

                # block check
                val = board[(outer % 3) * 3 + inner % 3][(outer // 3) * 3 + inner // 3]
                if val != '.':
                    if valid_cache[2][int(val) - 1]:
                        return False
                    valid_cache[2][int(val) - 1] = True

        return True


"""
起晚了，早上写道简单题娱乐一下
"""
