"""
395. 至少有 K 个重复字符的最长子串
给你一个字符串 s 和一个整数 k ，请你找出 s 中的最长子串。
要求该子串中的每一字符出现次数都不少于 k 。返回这一子串的长度。
https://leetcode-cn.com/problems/longest-substring-with-at-least-k-repeating-characters/
"""
from collections import defaultdict


class Solution:

    @staticmethod
    def longestSubstring(s: str, k: int) -> int:
        max_len = 0

        def get_length(_s: str):
            nonlocal max_len
            seen = defaultdict(list)
            for index in range(len(_s)):
                seen[_s[index]].append(index)
            bad_point = []
            for val in seen.values():
                if len(val) < k:
                    bad_point += val
            if not bad_point:
                max_len = max(max_len, len(_s))
                return
            bad_point = [-1] + bad_point + [len(_s)]
            for index in range(1, len(bad_point)):
                sub = _s[bad_point[index - 1] + 1:bad_point[index]]
                if len(sub) >= k and len(sub) > max_len:
                    get_length(sub)

        get_length(s)

        return max_len


"""
一次过，爽极
由于一层一个字典导致空间复杂度爆炸
"""
