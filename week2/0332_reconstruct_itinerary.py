"""
332. 重新安排行程
给你一份航线列表 tickets ，其中 tickets[i] = [fromi, toi] 表示飞机出发和降落的机场地点。请你对该行程进行重新规划排序。
所有这些机票都属于一个从 JFK（肯尼迪国际机场）出发的先生，所以该行程必须从 JFK 开始。如果存在多种有效的行程，请你按字典排序返回最小的行程组合。
例如，行程 ["JFK", "LGA"] 与 ["JFK", "LGB"] 相比就更小，排序更靠前。
假定所有机票至少存在一种合理的行程。且所有的机票 必须都用一次 且 只能用一次。
https://leetcode-cn.com/problems/reconstruct-itinerary
"""
from collections import defaultdict
from functools import reduce
import heapq
from typing import List


class Solution:
    @staticmethod
    def findItineraryLegacy(tickets: List[List[str]]) -> List[str]:

        last_ticket, neighbor = {}, {}
        for index in range(len(tickets)):
            try:
                last_ticket[tickets[index][0] + tickets[index][1]] += 1
            except KeyError:
                last_ticket[tickets[index][0] + tickets[index][1]] = 1
            try:
                neighbor[tickets[index][0]].append(tickets[index][1])
            except KeyError:
                neighbor[tickets[index][0]] = [tickets[index][1]]
            try:
                neighbor[tickets[index][1]]
            except KeyError:
                neighbor[tickets[index][1]] = []
        for key in neighbor.keys():
            neighbor[key].sort()

        def dfs(node: str):
            nonlocal path, last_ticket

            path.append(node)
            if len(path) == len(tickets) + 1:
                assert 0
            for neigh in neighbor[node]:
                edge = node + neigh
                if last_ticket[edge]:
                    last_ticket[edge] -= 1
                    dfs(neigh)
                    last_ticket[edge] += 1
            path.pop()

        path = []
        try:
            dfs('JFK')
        except AssertionError:
            return path

    @staticmethod
    def findItinerary(tickets: List[List[str]]) -> List[str]:

        edges = defaultdict(list)
        for ticket in tickets:
            edges[ticket[0]].append(ticket[1])
        for key in edges.keys():
            heapq.heapify(edges[key])

        def dfs(node: str):
            nonlocal edges, path
            while edges[node]:
                neigh = heapq.heappop(edges[node])
                dfs(neigh)
            path.append(node)

        path = []
        dfs('JFK')
        return path[::-1]


"""
写了一长串的try expect被一句collections.defaultdict解决了
last_ticket也是不用维护的，在维护票堆时就自动保证了无重复性
在遍历完成后加入节点使得加入节点的时机变成了“找到路径后返回时”，即保证了顺序问题（答案的倒序），又避免了重复对路径的操作

题解，真的很强大！自己，真的很弱小！
"""
