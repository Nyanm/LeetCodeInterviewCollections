"""
请你来实现一个myAtoi(string s)函数，使其能将字符串转换成一个 32 位有符号整数（类似 C/C++ 中的 atoi 函数）。
函数myAtoi(string s) 的算法如下：
读入字符串并丢弃无用的前导空格
检查下一个字符（假设还未到字符末尾）为正还是负号，读取该字符（如果有）。 确定最终结果是负数还是正数。 如果两者都不存在，则假定结果为正。
读入下一个字符，直到到达下一个非数字字符或到达输入的结尾。字符串的其余部分将被忽略。
将前面步骤读入的这些数字转换为整数（即，"123" -> 123， "0032" -> 32）。如果没有读入数字，则整数为 0 。必要时更改符号（从步骤 2 开始）。
如果整数数超过 32 位有符号整数范围 [−231, 231− 1] ，需要截断这个整数，使其保持在这个范围内。
具体来说，小于 −231 的整数应该被固定为 −231 ，大于 231− 1 的整数应该被固定为 231− 1 。
返回整数作为最终结果。
注意：
本题中的空白字符只包括空格字符 ' ' 。
除前导空格或数字后的其余字符串外，请勿忽略 任何其他字符
https://leetcode-cn.com/problems/string-to-integer-atoi
"""
import re


class Solution:
    @staticmethod
    def _myAtoi(s: str) -> int:
        pattern = re.compile(r'\d+')
        abs_res = pattern.search(s)
        abs_num = int(s[abs_res.span()[0]:abs_res.span()[1]])
        flag_index = abs_res.span()[0] - 1
        if flag_index >= 0 and s[flag_index] == '-':
            abs_num = -abs_num
        return abs_num

    @staticmethod
    def myAtoi(s: str) -> int:
        flag, index = 1, 0
        for index in range(len(s)):
            if s[index] == ' ':
                continue
            elif s[index] == '-':
                index += 1
                flag = -1
                break
            elif s[index] == '+':
                index += 1
                break
            elif s[index] in ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0'):
                break
            else:
                return 0
        num_str = ''
        for _index in range(index, len(s)):
            try:
                num_str += str(int(s[_index]))
            except ValueError:
                break
        if num_str:
            num_int = int(num_str) * flag
            if num_int > 2 ** 31 - 1:
                return 2 ** 31 - 1
            elif num_int < -2 ** 31:
                return -2 ** 31
            return num_int
        else:
            return 0

"""
抄了个很好看的解法
def myAtoi(self, s: str) -> int:
    return max(min(int(*re.findall('^[\+\-]?\d+', s.lstrip())), 2**31 - 1), -2**31)
缺德题目真的是
"""
