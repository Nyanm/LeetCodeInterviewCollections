"""
3. 无重复字符的最长子串
给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串 的长度。
https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/
"""


class Solution:
    @staticmethod
    def lengthOfLongestSubstring(s: str) -> int:

        if not s:
            return 0

        seen = [False] * 128
        left, right = 0, 1
        seen[ord(s[left])] = True
        cnt = right - left

        while right < len(s):
            index = ord(s[right])
            if seen[index]:
                seen[ord(s[left])] = False
                left += 1
            else:
                seen[index] = True
                right += 1

            cnt = max(cnt, right - left)

        return cnt


if __name__ == '__main__':
    print(Solution.lengthOfLongestSubstring("abcabcb"))

"""
TAG 双指针 滑动窗口 哈希表
O(n) 每一次循环内的操作为常数时间，最多进行n次循环（左、右各指针前进n-1次）

较前的指针负责维护“最长”的性质，较后的指针负责维护“无重复”的性质
如果题目是 子序列 那么这道题就是一道经典DP题目
用数据集特性偷了个鸡（利用ord()获取符号索引，省去哈希表建表时间），但感觉性能没什么提升
"""
