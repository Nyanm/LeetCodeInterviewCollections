"""
给你一个字符串 s，找到 s 中最长的回文子串。
https://leetcode-cn.com/problems/longest-palindromic-substring/
"""
import numpy as np


class Solution:
    @staticmethod
    def longestPalindrome(s: str) -> str:
        ans = Solution.dp_solution(s)
        print(ans)
        return ans

    @staticmethod
    def dp_solution(s: str) -> str:
        length = len(s)
        memo = np.eye(length, dtype=np.uint8)
        index = [0, 1]

        for size in range(2, length + 1):
            for front in range(length):

                back = front + size - 1
                if back >= length:
                    break

                if s[front] == s[back]:
                    if size == 2:
                        memo[front][back] = 1
                    else:
                        memo[front][back] = memo[front + 1][back - 1]

                if back - front + 1 > index[1] - index[0] and memo[front][back]:
                    index = [front, back + 1]

        return s[index[0]:index[1]]

    @staticmethod
    def manacher_solution(s: str) -> str:
        pass

# 马拉车有缘再会
