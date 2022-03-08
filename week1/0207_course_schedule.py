"""
你这个学期必须选修 numCourses 门课程，记为0到numCourses - 1 。
在选修某些课程之前需要一些先修课程。 先修课程按数组prerequisites 给出，其中prerequisites[i] = [ai, bi] ，表示如果要学习课程ai 则 必须 先学习课程 bi 。
例如，先修课程对[0, 1] 表示：想要学习课程 0 ，你需要先完成课程 1 。
请你判断是否可能完成所有课程的学习？如果可以，返回 true ；否则，返回 false 。
https://leetcode-cn.com/problems/course-schedule
"""


from typing import List


class Solution:
    @staticmethod
    def canFinish(numCourses: int, prerequisites: List[List[int]]) -> bool:
        jump_table = [[] for _ in range(numCourses)]
        seen = [0 for _ in range(numCourses)]
        false_flag = 0
        for pre_tuple in prerequisites:
            jump_table[pre_tuple[1]].append(pre_tuple[0])

        def dfs(node: int):
            nonlocal seen, false_flag
            seen[node] = 1

            if jump_table[node]:
                for neigh in jump_table[node]:
                    if not seen[neigh]:
                        dfs(neigh)
                        if false_flag:
                            return
                    elif seen[neigh] == 1:
                        false_flag = 1
                        return
            seen[node] = 2

        for index in range(numCourses):
            if not seen[index]:
                dfs(index)
                if false_flag:
                    return False

        return True

# 呜呜DFS忘得好干净
