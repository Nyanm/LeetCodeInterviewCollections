"""
给定一个包含红色、白色和蓝色、共n 个元素的数组nums，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。

我们使用整数 0、1 和 2 分别表示红色、白色和蓝色。

必须在不使用库的sort函数的情况下解决这个问题。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sort-colors
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    @staticmethod
    def sortColors(nums: List[int]) -> None:

        def exchange(index_a, index_b):
            temp = nums[index_a]
            nums[index_a] = nums[index_b]
            nums[index_b] = temp

        index0, index1, index2 = -1, 0, len(nums)
        while index1 < len(nums):

            if not nums[index1]:
                index0 += 1
                if index1 == index0:
                    index1 += 1
                    continue
                else:
                    exchange(index0, index1)
            elif nums[index1] == 1:
                index1 += 1
                continue
            else:
                index2 -= 1
                if index1 >= index2:
                    index1 += 1
                    continue
                else:
                    exchange(index1, index2)

    @staticmethod
    def _sortColors(nums: List[int]) -> None:
        cnt = [0, 0, 0]
        for num in nums:
            cnt[num] += 1
        nums[:] = [0] * cnt[0] + [1] * cnt[1] + [2] * cnt[2]


"""
直接对可迭代对象赋值会改变其内存位置，相当于改动的不是对象内容，而是指向对象的指针
需要使用 iterable[:] 进行赋值

LeetCode的运行时间和内存消耗也就图一乐
"""
