"""
在一条环路上有 n个加油站，其中第 i个加油站有汽油gas[i]升。
你有一辆油箱容量无限的的汽车，从第 i 个加油站开往第 i+1个加油站需要消耗汽油cost[i]升。你从其中的一个加油站出发，开始时油箱为空。
给定两个整数数组 gas 和 cost ，如果你可以绕环路行驶一周，则返回出发时加油站的编号，否则返回 -1 。如果存在解，则保证它是唯一的。
https://leetcode-cn.com/problems/gas-station
"""
from typing import List


class Solution:
    @staticmethod
    def canCompleteCircuit(gas: List[int], cost: List[int]) -> int:
        if sum(gas) - sum(cost) < 0:
            return -1
        balance, min_bal, min_index = 0, 1001, 0
        for index in range(len(gas)):
            balance += (gas[index] - cost[index])
            if min_bal > balance:
                min_bal = balance
                min_index = index
        return (min_index + 1) % len(gas)  # next station


"""
多画图多找规律
wac.是神
"""
