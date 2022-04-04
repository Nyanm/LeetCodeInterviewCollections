"""
72. 编辑距离
给你两个单词 word1 和 word2， 请返回将 word1 转换成 word2 所使用的最少操作数  。
你可以对一个单词进行如下三种操作：
插入一个字符
删除一个字符
替换一个字符
https://leetcode-cn.com/problems/edit-distance
"""


class Solution:
    @staticmethod
    def minDistance(word1: str, word2: str) -> int:
        memo = [[0] * (len(word1) + 1) for _ in range(len(word2) + 1)]
        # if we are matching a empty string ''
        for index in range(len(word1) + 1):
            memo[0][index] = index
        for index in range(len(word2) + 1):
            memo[index][0] = index

        for outer in range(1, len(word2) + 1):
            for inner in range(1, len(word1) + 1):
                if word2[outer - 1] == word1[inner - 1]:  # match successfully
                    memo[outer][inner] = memo[outer - 1][inner - 1]
                    continue
                # add: memo[outer - 1][inner] + 1
                # delete: memo[outer][inner - 1] + 1
                # change:  memo[outer - 1][inner - 1] + 1
                memo[outer][inner] = min(memo[outer - 1][inner], memo[outer][inner - 1], memo[outer - 1][inner - 1]) + 1
        return memo[-1][-1]


"""
DP转移方程和代码都很好理解……但是对问题的抽象太难太难了，下辈子才能领悟到这一层
"""
