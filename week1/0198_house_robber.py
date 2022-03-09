"""
你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。

给定一个代表每个房屋存放金额的非负整数数组，计算你 不触动警报装置的情况下 ，一夜之内能够偷窃到的最高金额。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/house-robber
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    @staticmethod
    def rob(nums: List[int]) -> int:
        max_money = 0
        memo = [0] * (len(nums) + 3)
        for index in range(len(nums)):
            memo[index + 3] = max(nums[index] + memo[index + 1], nums[index] + memo[index])
            max_money = max(max_money, memo[index + 3])
        return max_money


"""
19年秋王晟老师讲的第一道DP题，线状图的最大加权独立集问题
现在回看PPT中的证明过程仍十分受用
"""
