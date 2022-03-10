"""
树可以看成是一个连通且 无环 的 无向 图。
给定往一棵 n 个节点 (节点值 1～n) 的树中添加一条边后的图。添加的边的两个顶点包含在 1 到 n 中间，且这条附加的边不属于树中已存在的边。
图的信息记录于长度为 n 的二维数组 edges ，edges[i] = [ai, bi] 表示图中在 ai 和 bi 之间存在一条边。
请找出一条可以删去的边，删除后可使得剩余部分是一个有着 n 个节点的树。如果有多个答案，则返回数组 edges 中最后出现的边。
https://leetcode-cn.com/problems/redundant-connection
"""
from typing import List


class Union:

    def __init__(self, length: int):
        self.size, self.leader = [0], [0]
        for index in range(1, length + 1):
            self.leader.append(index)
            self.size.append(1)

    def find(self, node: int) -> int:
        stack = []
        while node is not self.leader[node]:
            stack.append(node)
            node = self.leader[node]
        for lower in stack:
            self.leader[lower] = node
            self.size[lower] = 1
        return node

    def check(self, node_a: int, node_b: int) -> bool:
        return self.find(node_a) == self.find(node_b)

    def union(self, node_a: int, node_b: int):
        leader_a, leader_b = self.find(node_a), self.find(node_b)
        if not leader_a == leader_b:
            if self.size[leader_a] > self.size[leader_b]:
                self.leader[leader_b] = self.leader[leader_a]
                self.size[leader_a] += self.size[leader_b]
            else:
                self.leader[leader_a] = self.leader[leader_b]
                self.size[leader_b] += self.size[leader_a]


class Solution:
    @staticmethod
    def findRedundantConnection(edges: List[List[int]]) -> List[int]:
        identity = Union(len(edges))
        for edge in edges:
            if identity.check(edge[0], edge[1]):
                return edge
            identity.union(edge[0], edge[1])


"""
打开大二写的并查集代码开始硬抄
优雅的数据结构
"""
