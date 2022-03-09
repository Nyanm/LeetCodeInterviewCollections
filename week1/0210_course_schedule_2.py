"""
现在你总共有 numCourses 门课需要选，记为 0 到 numCourses - 1。给你一个数组 prerequisites ，其中 prerequisites[i] = [ai, bi] ，表示在选修课程 ai 前必须先选修 bi 。
例如，想要学习课程 0 ，你需要先完成课程 1 ，我们用一个匹配来表示：[0,1] 。
返回你为了学完所有课程所安排的学习顺序。可能会有多个正确的顺序，你只要返回 任意一种 就可以了。如果不可能完成所有课程，返回 一个空数组 。
https://leetcode-cn.com/problems/course-schedule-ii
"""
from typing import List


class Solution:
    @staticmethod
    def findOrder(numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        jump_table = [[] for _ in range(numCourses)]
        for pre_tuple in prerequisites:
            jump_table[pre_tuple[1]].append(pre_tuple[0])

        seen = [0 for _ in range(numCourses)]
        route = []

        def dfs(cur: int):
            nonlocal seen, route
            seen[cur] = 1
            for node in jump_table[cur]:
                if seen[node] == 1:
                    raise SystemExit
                elif seen[node] == 2:
                    continue
                else:
                    dfs(node)
            route.append(cur)
            seen[cur] = 2

        try:
            for index in range(numCourses):
                if not seen[index]:
                    dfs(index)
        except SystemExit:
            return []

        route.reverse()
        return route


"""
RISE WITH ME RISE WITH ME RISE WITH ME 
RISE! UP!

和 207 课程表 完全一样的题目，加上了对路径的追踪
之前使用传出一个错误flag来跳出递归的嵌套，这次尝试了使用raise错误来强行退出多层嵌套
"""
