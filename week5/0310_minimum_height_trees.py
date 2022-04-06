"""
310. 最小高度树
树是一个无向图，其中任何两个顶点只通过一条路径连接。 换句话说，一个任何没有简单环路的连通图都是一棵树。
给你一棵包含 n 个节点的树，标记为 0 到 n - 1 。给定数字 n 和一个有 n - 1 条无向边的 edges 列表（每一个边都是一对标签）。
其中 edges[i] = [ai, bi] 表示树中节点 ai 和 bi 之间存在一条无向边。
可选择树中任何一个节点作为根。当选择节点 x 作为根节点时，设结果树的高度为 h 。
在所有可能的树中，具有最小高度的树（即，min(h)）被称为 最小高度树 。
请你找到所有的 最小高度树 并按 任意顺序 返回它们的根节点标签列表。
树的 高度 是指根节点和叶子节点之间最长向下路径上边的数量。
https://leetcode-cn.com/problems/minimum-height-trees
"""
from typing import List


class Solution:
    @staticmethod
    def findMinHeightTrees(n: int, edges: List[List[int]]) -> List[int]:
        edge_list, neigh_cnt = [[] for _ in range(n)], [0] * n
        for edge in edges:
            node1, node2 = edge
            edge_list[node1].append(node2)
            edge_list[node2].append(node1)
        border = []
        for index in range(n):
            neigh_cnt[index] = len(edge_list[index])
            if neigh_cnt[index] <= 1:
                border.append(index)

        seen = [False] * n

        def bfs(nodes: list):
            nonlocal seen
            _border = []
            for node in nodes:
                seen[node] = True
                for neigh in edge_list[node]:
                    if not seen[neigh]:
                        neigh_cnt[neigh] -= 1
                        if neigh_cnt[neigh] == 1:
                            _border.append(neigh)
            if not _border:
                return nodes
            else:
                return bfs(_border)

        return bfs(border)


"""
想了半天想了个O(n)方法超时了
内存消耗奇高
"""
