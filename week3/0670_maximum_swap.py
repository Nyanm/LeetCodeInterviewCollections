"""
670. 最大交换
给定一个非负整数，你至多可以交换一次数字中的任意两位。返回你能得到的最大值。
https://leetcode-cn.com/problems/maximum-swap/
"""


class MonoStack:
    """
    Monotonic non-increasing stack
    """

    def __init__(self):
        self.__stack = []

    @property
    def stack(self):
        return self.__stack

    def push(self, item):
        """
        Push item into monotonic stack

        :param item: valid items: int, float, iterable[int, any, ...]
        """
        if type(item) == (int or float):
            while self.__stack and item > self.__stack[-1]:
                self.__pop()
        else:
            while self.__stack and item[0] > self.__stack[-1][0]:
                self.__pop()
            self.__stack.append(item)

    def __pop(self):
        return self.__stack.pop()


class Solution:
    @staticmethod
    def maximumSwap(num: int) -> int:
        mono = MonoStack()
        num_list = [int(dig) for dig in str(num)]
        for index in range(len(num_list)):
            mono.push([int(num_list[index]), index])
        for index in range(len(mono.stack)):
            if mono.stack[index][1] != index:
                s_index = index
                while s_index < len(mono.stack) - 1 and mono.stack[s_index][0] == mono.stack[s_index + 1][0]:
                    s_index += 1
                num_list[index], num_list[mono.stack[s_index][1]] = num_list[mono.stack[s_index][1]], num_list[index]
                return int(''.join(list(map(str, num_list))))
        # the perfect non-increasing array
        return num


"""
TP二面算法题
思路很简单，实现起来还怪麻烦的
"""
