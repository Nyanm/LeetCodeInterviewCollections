"""
给你一个包含 n 个整数的数组nums，判断nums中是否存在三个元素 a，b，c ，使得a + b + c = 0 ？请你找出所有和为 0 且不重复的三元组。
注意：答案中不可以包含重复的三元组。
https://leetcode-cn.com/problems/3sum
"""
from typing import List


class Solution:
    @staticmethod
    def threeSum(nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        length = len(nums)
        if length <= 2:
            return res
        for index1 in range(length - 2):
            index3 = length - 1
            if index1 > 0 and nums[index1 - 1] == nums[index1]:
                continue
            for index2 in range(index1 + 1, length - 1):
                # print(f'index1:{index1}, index2:{index2}, index3:{index3}')
                if (index2 > index1 + 1 and nums[index2 - 1] == nums[index2]) or index2 == index3:
                    continue
                while nums[index1] + nums[index2] + nums[index3] > 0 and index3 > index2 + 1:
                    index3 -= 1
                if nums[index1] + nums[index2] + nums[index3] == 0:
                    res.append([nums[index1], nums[index2], nums[index3]])

        return res


"""
这下真的激战一夜了
"""
