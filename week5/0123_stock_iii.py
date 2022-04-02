"""
123. 买卖股票的最佳时机 III
给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。
设计一个算法来计算你所能获取的最大利润。你最多可以完成 两笔 交易。
注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iii
"""
from typing import List


class Solution:
    @staticmethod
    def maxProfitNSpace(prices: List[int]) -> int:
        first = [0] * len(prices)
        lowermost = prices[0]
        for index in range(1, len(prices)):
            lowermost = min(lowermost, prices[index])
            first[index] = max(prices[index] - lowermost, first[index - 1])
        profit, max_profit = 0, 0
        for index in range(len(prices) - 2, -1, -1):
            profit = max(0, (prices[index + 1] - prices[index]) + profit)
            max_profit = max(max_profit, profit + first[index])
        return max_profit

    @staticmethod
    def maxProfit(prices: List[int]) -> int:
        first, lowermost, second, second_low = 0, prices[0], 0, prices[0]
        for index in range(1, len(prices)):
            lowermost = min(lowermost, prices[index])
            first = max(prices[index] - lowermost, first)
            second_low = min(second_low, prices[index] - first)
            second = max(second, prices[index] - second_low)
        return second


"""
想了个O(n)空间复杂度的解出来，正向反向DP
题解的O(1)解相当于在一次遍历中同时推进两次购买行程，非常巧妙
"""
