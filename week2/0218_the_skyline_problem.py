"""
城市的 天际线 是从远处观看该城市中所有建筑物形成的轮廓的外部轮廓。给你所有建筑物的位置和高度，请返回 由这些建筑物形成的 天际线 。
每个建筑物的几何信息由数组 buildings 表示，其中三元组 buildings[i] = [lefti, righti, heighti] 表示：

lefti 是第 i 座建筑物左边缘的 x 坐标。
righti 是第 i 座建筑物右边缘的 x 坐标。
heighti 是第 i 座建筑物的高度。
你可以假设所有的建筑都是完美的长方形，在高度为 0  的绝对平坦的表面上。

天际线 应该表示为由 “关键点” 组成的列表，格式 [[x1,y1],[x2,y2],...] ，并按 x 坐标 进行 排序 。
关键点是水平线段的左端点。列表中最后一个点是最右侧建筑物的终点，y 坐标始终为 0 ，仅用于标记天际线的终点。此外，任何两个相邻建筑物之间的地面都应被视为天际线轮廓的一部分。

注意：输出天际线中不得有连续的相同高度的水平线。
例如 [...[2 3], [4 5], [7 5], [11 5], [12 7]...] 是不正确的答案；三条高度为 5 的线应该在最终输出中合并为一个：[...[2 3], [4 5], [12 7], ...]

https://leetcode-cn.com/problems/the-skyline-problem
"""
from typing import List
import heapq


class Solution:
    @staticmethod
    def getSkyline(buildings: List[List[int]]) -> List[List[int]]:

        coordinate, highest, alive = [], [], [False] * len(buildings)
        ans = []

        for index in range(len(buildings)):
            # a list of [-height, x coordinate, index]
            coordinate.append([-buildings[index][2], buildings[index][0], index])
            coordinate.append([-buildings[index][2], -buildings[index][1], index])
            # tricky trick to store left/right flag
        coordinate.sort(key=lambda x: abs(x[1]))

        for index in range(len(coordinate)):
            cur_node = coordinate[index]

            if cur_node[1] >= 0:  # left node
                heapq.heappush(highest, coordinate[index])
                alive[cur_node[2]] = True

                while not alive[highest[0][2]]:
                    heapq.heappop(highest)

                if highest[0][2] == cur_node[2]:
                    if ans:
                        if len(ans) > 1 and ans[-2][1] == -cur_node[0] and ans[-1][0] == cur_node[1]:
                            # two juxtapose building with same height
                            ans.pop()
                            continue
                        if ans[-1][1] == -cur_node[0]:  # same height
                            continue
                        if ans[-1][0] == cur_node[1]:  # same x coordinate
                            ans[-1][1] = max(-cur_node[0], ans[-1][1])
                            continue
                    ans.append([cur_node[1], -cur_node[0]])

            else:  # right node
                alive[coordinate[index][2]] = False

                if highest[0][2] == cur_node[2]:
                    while highest and not alive[highest[0][2]]:
                        heapq.heappop(highest)
                    if highest:
                        if cur_node[0] >= highest[0][0]:
                            continue
                        if ans and ans[-1][0] == -cur_node[1]:  # same x coordinate
                            ans[-1][1] = min(-cur_node[0], ans[-1][1], -highest[0][0])
                            continue
                        ans.append([-cur_node[1], -highest[0][0]])
                    else:
                        if ans and ans[-1][0] == -cur_node[1]:  # same x coordinate
                            ans[-1][1] = min(-cur_node[0], ans[-1][1], 0)
                            continue
                        ans.append([-cur_node[1], 0])

        return ans


"""
边界条件怎么这么多，垮起个拉拉肥批脸

日啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊！！！！！！！！！！！
我就好像一个在家补衣服的老婆子，我的孩子出去跑测试用例，每天晚上回家衣服都会破几个洞，我就点着油灯在电脑前补呀补补呀补，补到这件衣服我自己都认不出来了

孩子们：
    print(Solution.getSkyline([[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]])
          == [[2, 10], [3, 15], [7, 12], [12, 0], [15, 10], [20, 8], [24, 0]])
    print(Solution.getSkyline([[0, 2, 3], [2, 5, 3]])
          == [[0, 3], [5, 0]])
    print(Solution.getSkyline([[0, 3, 3], [1, 5, 3], [2, 4, 3], [3, 7, 3]])
          == [[0, 3], [7, 0]])
    print(Solution.getSkyline([[4, 9, 10], [4, 9, 15], [4, 9, 12], [10, 12, 10], [10, 12, 8]])
          == [[4, 15], [9, 0], [10, 10], [12, 0]])
    print(Solution.getSkyline([[9, 100, 74], [74, 99, 145], [88, 99, 99]])
          == [[9, 74], [74, 145], [99, 74], [100, 0]])
    print(Solution.getSkyline([[0, 5, 7], [5, 10, 7], [5, 10, 12], [10, 15, 7], [15, 20, 7], [15, 20, 12], [20, 25, 7]])
          == [[0, 7], [5, 12], [10, 7], [15, 12], [20, 7], [25, 0]])
          
真的写麻了
"""
