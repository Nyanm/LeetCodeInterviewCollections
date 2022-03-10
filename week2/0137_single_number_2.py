"""
给你一个整数数组 nums ，除某个元素仅出现 一次 外，其余每个元素都恰出现 三次 。请你找出并返回那个只出现了一次的元素。
https://leetcode-cn.com/problems/single-number-ii/
"""
from typing import List


class Solution:
    @staticmethod
    def singleNumber(nums: List[int]) -> int:
        a, b = 0, 0
        for x in nums:
            b = ~a & (b ^ x)  # b_i+1 = a_i'·(b_i XOR x_i)
            a = ~b & (a ^ x)  # a_i+1 = a_i·b_i'·x' + a_i'·b_i·x_i = b_i+1'·(a_i XOR x_i)
        return b


"""
数电解法震撼我妈一整年……
实际上想到了，既然每个重复元素都会准确地出现三次，那么一定要拿数组的和做文章，只是怎么也想不到位运算这个层面
核心是三进制，但是需要在位层面上实现

写一半发现不会求电路，上手画一下状态转移表就出来了
现在就是非常地对不起数电老师（
最后还简化了电路，震惊

收获很大，必可活用于下一次
太菜了我

震惊
"""
