"""
188. 买卖股票的最佳时机 IV
给定一个整数数组 prices ，它的第 i 个元素 prices[i] 是一支给定的股票在第 i 天的价格。
设计一个算法来计算你所能获取的最大利润。你最多可以完成 k 笔交易。
注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iv
"""
from typing import List


class Solution:
    @staticmethod
    def maxProfit(k: int, prices: List[int]) -> int:
        if not k or not prices:
            return 0
        memo = [prices[0], 0] * k  # nth lowermost, nth profit
        for index in range(len(prices)):
            memo[0] = min(memo[0], prices[index])  # lowermost of all
            memo[1] = max(memo[1], prices[index] - memo[0])  # maximum profit in just one investment
            for sell in range(2, k * 2, 2):
                memo[sell] = min(memo[sell], prices[index] - memo[sell - 1])
                memo[sell + 1] = max(memo[sell + 1], prices[index] - memo[sell])
        return memo[-1]


"""
对着股票3抄出来的，核心思想在3里就很明确了
几个空测试例纯属脑子有坑
"""
