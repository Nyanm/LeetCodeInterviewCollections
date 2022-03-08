"""
给定一个非负整数 num，反复将各个位上的数字相加，直到结果为一位数。返回这个结果。
https://leetcode-cn.com/problems/add-digits
"""


def addDigits(num: int) -> int:
    # Regular solution
    while num >= 10:
        str_num = str(num)
        num = 0
        for dig in str_num:
            num += int(dig)
    return num


def addDigits_o1(num: int) -> int:
    """
    As we can see, there are strict cycles through the increasing numbers
    number:  0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21
    dig sum: 0  1  2  3  4  5  6  7  8  9  1  2  3  4  5  6  7  8  9  1  2  3
    They follow a 1-9 cycle and 0 itself is an exception
    """
    if num >= 10:
        return num % 9
    else:
        return num
