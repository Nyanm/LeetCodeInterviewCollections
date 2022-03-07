"""
给定两个字符串text1 和text2，返回这两个字符串的最长 公共子序列 的长度。如果不存在 公共子序列 ，返回 0 。
一个字符串的子序列是指这样一个新的字符串：它是由原字符串在不改变字符的相对顺序的情况下删除某些字符（也可以不删除任何字符）后组成的新字符串。
例如，"ace" 是 "abcde" 的子序列，但 "aec" 不是 "abcde" 的子序列。
两个字符串的 公共子序列 是这两个字符串所共同拥有的子序列。
https://leetcode-cn.com/problems/longest-common-subsequence
"""


class Solution:
    @staticmethod
    def longestCommonSubsequence(text1: str, text2: str) -> int:
        len_1, len_2 = len(text1), len(text2)
        memo = [[0] * (len_1 + 1) for _ in range(len_2 + 1)]
        for index2 in range(1, len_2 + 1):
            for index1 in range(1, len_1 + 1):
                if text1[index1 - 1] == text2[index2 - 1]:
                    memo[index2][index1] = memo[index2 - 1][index1 - 1] + 1
                else:
                    memo[index2][index1] = max(memo[index2][index1 - 1], memo[index2 - 1][index1])
        return memo[-1][-1]


"""
最开始写的时候路走窄了，最后还是题解救我狗命
"""
