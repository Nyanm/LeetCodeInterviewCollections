"""
给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串 的长度。
https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/
"""


class Solution:
    @staticmethod
    def lengthOfLongestSubstring(s: str) -> int:
        seen = {}
        max_sub = 0
        floor, ceil = 0, 0
        while ceil < len(s):
            cur = s[ceil]
            try:
                if seen[cur]:
                    while seen[cur]:
                        seen[s[floor]] = 0
                        floor += 1
                else:
                    seen[cur] = 1
                    ceil += 1
            except KeyError:
                seen[cur] = 1
                ceil += 1
            max_sub = max(max_sub, ceil - floor)

        return max_sub

# 看题解忘了还有set这种好东西
