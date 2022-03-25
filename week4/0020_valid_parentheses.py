"""
20. 有效的括号
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。
有效字符串需满足：
左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
https://leetcode-cn.com/problems/valid-parentheses
"""


class Solution:
    @staticmethod
    def isValid(s: str) -> bool:
        stack, left = [], ['(', '[', '{']
        parentheses_table = {')': '(', ']': '[', '}': '{'}
        for char in s:
            if char in left:
                stack.append(char)
            else:
                try:
                    if stack[-1] == parentheses_table[char]:
                        stack.pop()
                    else:
                        return False
                except IndexError:
                    return False
        return stack == []


if __name__ == '__main__':
    print(Solution.isValid(')('))

"""
started at 15:21
finished at 15:26
duration: 5 min 

栈的最最最基本应用
"""
