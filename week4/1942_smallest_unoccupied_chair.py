"""
1942. 最小未被占据椅子的编号
有 n 个朋友在举办一个派对，这些朋友从 0 到 n - 1 编号。派对里有 无数 张椅子，编号为 0 到 infinity 。当一个朋友到达派对时，他会占据 编号最小 且未被占据的椅子。
比方说，当一个朋友到达时，如果椅子 0 ，1 和 5 被占据了，那么他会占据 2 号椅子。
当一个朋友离开派对时，他的椅子会立刻变成未占据状态。如果同一时刻有另一个朋友到达，可以立即占据这张椅子。
给你一个下标从 0 开始的二维整数数组 times ，其中 times[i] = [arrivali, leavingi] 表示第 i 个朋友到达和离开的时刻
同时给你一个整数 targetFriend 。所有到达时间 互不相同 。
请你返回编号为 targetFriend 的朋友占据的 椅子编号 。
https://leetcode-cn.com/problems/the-number-of-the-smallest-unoccupied-chair
"""
from typing import List
import heapq


class Solution:
    @staticmethod
    def smallestChair(times: List[List[int]], targetFriend: int) -> int:
        time_line = []  # [[time, is_come, index]], make sure that "leave" action before "come" action
        alive = [False for _ in range(len(times))]
        empty = [index for index in range(len(times))]

        for index in range(len(times)):
            come, leave = times[index]
            time_line.append([come, 1, index])
            time_line.append([leave, 0, index])
        time_line.sort(key=lambda x: (x[0], x[1]))

        for action in time_line:
            timestamp, is_come, index = action
            if is_come:
                if index == targetFriend:
                    return heapq.heappop(empty)
                alive[index] = heapq.heappop(empty)
            else:
                heapq.heappush(empty, alive[index])


"""
路走窄了，初见一直想怎么维护座位的集合，结果应该维护空座位的集合
"""
