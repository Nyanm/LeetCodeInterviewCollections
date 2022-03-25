"""
14. 最长公共前缀
编写一个函数来查找字符串数组中的最长公共前缀。
如果不存在公共前缀，返回空字符串 ""。
https://leetcode-cn.com/problems/longest-common-prefix/
"""
from typing import List


class Solution:
    @staticmethod
    def longestCommonPrefix(strs: List[str]) -> str:
        index = 0
        while True:
            try:
                common = strs[0][index]
                for string in strs:
                    if string[index] != common:
                        return strs[0][:index]
                index += 1
            except IndexError:
                return strs[0][:index]


"""
Started at 15:09
Finished at 15:15
Duration: 6 min

体现算法思想为零
但是很快！
"""
