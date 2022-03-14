"""
10. 正则表达式匹配
给你一个字符串 s 和一个字符规律 p，请你来实现一个支持 '.' 和 '*' 的正则表达式匹配。
'.' 匹配任意单个字符
'*' 匹配零个或多个前面的那一个元素
所谓匹配，是要涵盖整个字符串 s的，而不是部分字符串。
https://leetcode-cn.com/problems/regular-expression-matching
"""


class Solution:
    @staticmethod
    def isMatch(s: str, p: str) -> bool:
        is_star, p_new = [], ''
        for index in range(len(p)):
            if p[index] == '*':
                is_star[-1] = True
            else:
                is_star.append(False)
                p_new += p[index]
        memo = [[False] * (len(s) + 1) for _ in range((len(p_new) + 1))]
        memo[0][0] = True

        for y in range(1, len(p_new) + 1):
            p_char = p_new[y - 1]

            if is_star[y - 1]:  # star "*" wildcard

                if p_char == '.':  # period "." wild card
                    for x in range(0, len(s) + 1):
                        memo[y][x] = (memo[y - 1][x - 1] + memo[y - 1][x] + memo[y][x - 1]) > 0
                    continue

                else:  # normal latin characters
                    for x in range(0, len(s) + 1):
                        temp = ((memo[y][x - 1]) > 0) and (p_char == s[x - 1]) or (memo[y - 1][x])
                        memo[y][x] = temp
                    continue

            for x in range(1, len(s) + 1):  # normal rule
                if p_char == '.':  # period "." wild card
                    memo[y][x] = memo[y - 1][x - 1]
                else:  # normal latin characters
                    memo[y][x] = (memo[y - 1][x - 1]) and (p_char == s[x - 1])

        return memo[-1][-1]


"""
劲爆动规大题，写起来很爽
写过 44 通配符匹配 的情况下写这道题应该马上就有思路，但是实现起来还是有一点麻烦的
"""

