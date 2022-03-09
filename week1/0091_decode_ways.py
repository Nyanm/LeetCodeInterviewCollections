"""
一条包含字母A-Z 的消息通过以下映射进行了 编码 ：
'A' -> "1"
'B' -> "2"
...
'Z' -> "26"

要 解码 已编码的消息，所有数字必须基于上述映射的方法，反向映射回字母（可能有多种方法）。例如，"11106" 可以映射为：
"AAJF" ，将消息分组为 (1 1 10 6)
"KJF" ，将消息分组为 (11 10 6)
注意，消息不能分组为 (1 11 06) ，因为 "06" 不能映射为 "F" ，这是由于 "6" 和 "06" 在映射中并不等价。
给你一个只含数字的 非空 字符串 s ，请计算并返回 解码 方法的 总数 。
题目数据保证答案肯定是一个 32 位 的整数。
https://leetcode-cn.com/problems/decode-ways
"""


def fib(n: int) -> int:
    a, b = 1, 0
    for i in range(n + 1):
        temp = b
        b = a + b
        a = temp
    return b


class Solution:
    @staticmethod
    def numDecodings(s: str) -> int:
        fibonacci = {1: 1, 2: 2, 3: 3, 4: 5, 5: 8, 6: 13, 7: 21, 8: 34, 9: 55, 10: 89, 11: 144, 12: 233, 13: 377,
                     14: 610, 15: 987, 16: 1597, 17: 2584, 18: 4181, 19: 6765, 20: 10946, 21: 17711, 22: 28657,
                     23: 46368, 24: 75025, 25: 121393, 26: 196418, 27: 317811, 28: 514229, 29: 832040, 30: 1346269,
                     31: 2178309, 32: 3524578, 33: 5702887, 34: 9227465, 35: 14930352, 36: 24157817, 37: 39088169,
                     38: 63245986, 39: 102334155, 40: 165580141, 41: 267914296, 42: 433494437, 43: 701408733,
                     44: 1134903170, 45: 1836311903}

        if not int(s[0]):
            return 0

        memo = [0] * len(s)

        for index in range(0, len(s)):
            if int(s[index]) == 0:
                if memo[index - 1] is not 1:
                    return 0
                memo[index] = memo[index - 1] = 0
                if index - 2 >= 0 and memo[index - 2] == 1:
                    memo[index - 2] = 2
                continue
            if index == len(s) - 1:
                memo[index] = 2
                continue
            if int(s[index:index + 2]) <= 26:
                memo[index] = 1
            else:
                memo[index] = 2

        ans, cnt = 1, 0
        for index in range(len(memo)):
            if memo[index] == 1:
                cnt += 1
            elif memo[index] == 2:
                cnt += 1
                ans *= fibonacci[cnt]
                cnt = 0

        return ans


"""
神志不清了，明天再写

让你尝尝打表的厉害罢！
痛苦程度能排进前三的题目，试了一万种边界条件，提交记录里一片红
"""
