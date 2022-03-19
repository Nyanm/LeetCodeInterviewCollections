"""
215. 数组中的第K个最大元素
给定整数数组 nums 和整数 k，请返回数组中第 k 个最大的元素。
请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。
https://leetcode-cn.com/problems/kth-largest-element-in-an-array/
"""
from typing import List


class Solution:
    @staticmethod
    def findKthLargest(nums: List[int], k: int) -> int:
        length = len(nums)
        if length == 1:
            return nums[0]
        benchmark = sorted([nums[0], nums[-1], nums[length // 2]])[1]
        lt, eq, gt = length - 1, length - 1, 0
        while eq >= gt:
            if nums[eq] < benchmark:
                nums[lt], nums[eq] = nums[eq], nums[lt]
                lt, eq = lt - 1, eq - 1
            elif nums[eq] > benchmark:
                nums[gt], nums[eq] = nums[eq], nums[gt]
                gt += 1
            else:
                eq -= 1
        # print(f'nums:{nums}, benchmark:{benchmark}, gt:{gt} eq:{eq} lt:{lt}, target:{k}')
        if k - 1 < gt:
            return Solution.findKthLargest(nums[:gt], k)
        elif k - 1 > lt:
            return Solution.findKthLargest(nums[lt + 1:], k - lt - 1)
        return benchmark


"""
TAG 堆 二分
O(n) 要用主定理证明太麻烦了算了算了

参考 https://oi-wiki.org/basic/quick-sort/
第一次拿到这个题时非常开心地写了个最小堆，一遍AC，还想怎么这么水
重新学习快排时才发现这道题应该使用减治来获得更低的时间复杂度，顺带看了三路快排的内容
太年轻了还是
"""
