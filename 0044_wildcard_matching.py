"""
给定一个字符串(s) 和一个字符模式(p) ，实现一个支持'?'和'*'的通配符匹配。
'?' 可以匹配任何单个字符。
'*' 可以匹配任意字符串（包括空字符串）。
两个字符串完全匹配才算匹配成功。

说明:
s可能为空，且只包含从a-z的小写字母。
p可能为空，且只包含从a-z的小写字母，以及字符?和*。
https://leetcode-cn.com/problems/wildcard-matching
"""


class Solution:
    @staticmethod
    def isMatch(s: str, p: str) -> bool:
        if not s:
            for char in p:
                if char is not '*':
                    return False
            return True
        len_s, len_p = len(s), len(p)
        memo = [[False] * (len_s + 1) for _ in range(len_p + 1)]
        memo[0][0] = True
        for index_p in range(1, len_p + 1):
            char_p = p[index_p - 1]
            for index_s in range(1, len_s + 1):
                char_s = s[index_s - 1]
                if char_p == '*':
                    for index_star in range(0, len_s + 1):
                        if memo[index_p - 1][index_star]:
                            memo[index_p][index_star:] = [True] * (len_s - index_star + 1)
                            break
                    break
                elif char_p == '?':
                    memo[index_p][index_s] = memo[index_p - 1][index_s - 1]
                else:
                    if char_p == char_s:
                        memo[index_p][index_s] = memo[index_p - 1][index_s - 1]
        return memo[-1][-1]


"""
空字符串确实给我整懵了
"""
