class Solution:
    @staticmethod
    def longestPalindrome(s: str) -> str:
        # add meaningless characters into string
        s = ('(#%s#)' % '#'.join(s))

        # manacher
        memo = [0] * len(s)
        border, center = 0, 0
        max_cnt, max_index = -1, 0
        for index in range(1, len(s) - 1):
            index_sym = center * 2 - index

            # set arm length of s[index]
            if border > index:
                memo[index] = min(border - index, memo[index_sym])
            else:
                memo[index] = 0

            # expand arm length
            while s[index + memo[index] + 1] == s[index - memo[index] - 1]:
                memo[index] += 1

            # renew LPS count and index
            if memo[index] > max_cnt:
                max_cnt = memo[index]
                max_index = index

            # expand border (if necessary)
            if memo[index] + index > border:
                center = index
                border = memo[index] + index

        # reconstruct longest palindromic substring
        return s[max_index - max_cnt + 1:max_index + max_cnt:2]


"""
TAG 动态规划 字符串
O(n) 遍历一次元素，虽然其中有一个while循环，但是对于每个元素来说都只会（被其他元素）扩展一次

非常有代表性的动态规划问题，完美地体现了动态规划存储子问题解的思想
参考 https://zhuanlan.zhihu.com/p/70532099 代码实现很漂亮，跑起来很快，python语法糖很甜
"""
