"""
根据 逆波兰表示法，求表达式的值。

有效的算符包括+、-、*、/。每个运算对象可以是整数，也可以是另一个逆波兰表达式。

注意两个整数之间的除法只保留整数部分。

可以保证给定的逆波兰表达式总是有效的。换句话说，表达式总会得出有效数值且不存在除数为 0 的情况。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/evaluate-reverse-polish-notation
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    @staticmethod
    def evalRPN(tokens: List[str]) -> int:
        def add(a: int, b: int) -> int:
            return a + b

        def minus(a: int, b: int) -> int:
            return a - b

        def times(a: int, b: int) -> int:
            return a * b

        def divide(a: int, b: int) -> int:
            return int(a / b)

        num_fun = {
            '+': add,
            '-': minus,
            '*': times,
            '/': divide
        }

        num_stack = []
        for char in tokens:
            try:
                fun = num_fun[char]
            except KeyError:
                num_stack.append(int(char))
                continue
            num2 = num_stack.pop()
            num1 = num_stack.pop()
            num_stack.append(fun(num1, num2))

        return num_stack[0]


"""
写道简单题抚慰一下我破碎的心灵
"""
