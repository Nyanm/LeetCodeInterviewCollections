"""
给你一个只包含 '(' 和 ')' 的字符串，找出最长有效（格式正确且连续）括号子串的长度。
https://leetcode-cn.com/problems/longest-valid-parentheses/
"""


class Solution:
    @staticmethod
    def longestValidParentheses(s: str) -> int:
        left, right, pair = 0, 0, 0
        for index in range(len(s)):
            if s[index] == '(':
                left += 1
            else:
                right += 1
                if right > left:
                    right = left = 0
                elif right == left:
                    pair = max(left, pair)

        left, right, _pair = 0, 0, 0
        for index in range(len(s) - 1, -1, -1):
            if s[index] == ')':
                right += 1
            else:
                left += 1
                if right < left:
                    right = left = 0
                elif right == left:
                    _pair = max(left, _pair)

        return max(pair, _pair) * 2


"""
动规题目贪心硬算
栈解法非常有意思
"""
