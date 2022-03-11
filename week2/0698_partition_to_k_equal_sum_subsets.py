"""
给定一个整数数组  nums 和一个正整数 k，找出是否有可能把这个数组分成 k 个非空子集，其总和都相等。
https://leetcode-cn.com/problems/partition-to-k-equal-sum-subsets/
"""
from typing import List


class Solution:

    @staticmethod
    def canPartitionKSubsets(nums: List[int], k: int) -> bool:

        volume = sum(nums) // k
        seen = [False] * len(nums)
        nums.sort(reverse=True)

        def dfs(num_index: int, cur_volume: int, bucket_index: int) -> bool:

            nonlocal seen, nums
            if bucket_index == k:
                return all(seen)
            if cur_volume == volume:
                return dfs(0, 0, bucket_index + 1)

            for index in range(num_index, len(nums)):
                if not seen[index]:
                    if cur_volume + nums[index] <= volume:

                        seen[index] = True
                        if dfs(index + 1, cur_volume + nums[index], bucket_index):
                            return True
                        seen[index] = False

            return False

        return dfs(0, 0, 0)

    """ 
    # greedy (Failed)
    @staticmethod
    def canPartitionKSubsets(nums: List[int], k: int) -> bool:
        bucket = [0] * k
        volume = sum(nums) // k
        nums.sort()
        while nums:
            cur = nums.pop()
            for index in range(k):
                if bucket[index] + cur <= volume:
                    bucket[index] += cur
                    cur = -1
                    break
            if not cur == -1:
                return False
        for index in range(k):
            if bucket[index] != volume:
                return False
        return True
    """


"""
乍一看很像贪心的题，用贪心做了一下，果然错了（居然过了120+个测试例
本来以为会有什么精妙的算法，结果一查就是硬剪枝，指数时间复杂度
最后被我们寄予厚望的 状态压缩 也没有派上什么打得用场，在这道题里纯粹属于一个优化了一点内存使用的小技巧

铁超时

29行处需要注意继承现今的指针，又de了半天的虚空bug

铁超时
抄了个题解居然还是超时了，谔谔
"""
