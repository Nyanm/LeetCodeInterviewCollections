"""
我们给出了一个（轴对齐的）二维矩形列表 rectangles 。
对于 rectangle[i] = [x1, y1, x2, y2]，其中（x1，y1）是矩形 i 左下角的坐标， (xi1, yi1) 是该矩形 左下角 的坐标， (xi2, yi2) 是该矩形 右上角 的坐标。
计算平面中所有 rectangles 所覆盖的总面积。任何被两个或多个矩形覆盖的区域应只计算 一次 。
返回总面积。因为答案可能太大，返回 10 ^ 9 + 7 的模。
https://leetcode-cn.com/problems/rectangle-area-ii
"""
from typing import List
import bisect
import heapq


class Solution:
    @staticmethod
    def rectangleArea(rectangles: List[List[int]]) -> int:
        rec_cnt = len(rectangles)
        alive = [False] * rec_cnt
        y_segments = []  # a list of [y, index, is upper]
        area = 0

        def get_valid_length(__y_segments: list) -> int:

            valid, lowermost = [0], 10 ** 9
            y_alive, y_heap = [False] * rec_cnt, []  # a heap of [y_val, rec_index]
            for y_node in __y_segments:
                y_val, rec_index, is_upper = y_node

                # lower node(insert)
                if not is_upper:
                    y_alive[rec_index] = True
                    heapq.heappush(y_heap, [y_val, rec_index])

                    while not y_alive[y_heap[0][1]]:
                        heapq.heappop(y_heap)
                    lowermost = min(lowermost, y_heap[0][0])

                # upper node(delete)
                else:
                    while not y_alive[y_heap[0][1]]:
                        heapq.heappop(y_heap)
                    valid[-1] = y_val - lowermost

                    y_alive[rec_index] = False
                    try:
                        while not y_alive[y_heap[0][1]]:
                            heapq.heappop(y_heap)
                    except IndexError:
                        lowermost = 10 ** 9
                        valid.append(0)
                        continue

            return sum(valid)

        x_coordinate = []  # a list of [±x, index], negative x means that its right border
        for index in range(rec_cnt):
            # rectangle = [x1, y1, x2, y2] (x1 < x2, y1 < y2)
            x_coordinate.append([rectangles[index][0], index])
            x_coordinate.append([-rectangles[index][2], index])
        x_coordinate.sort(key=lambda x: abs(x[0]))

        for node_index in range(rec_cnt * 2):
            x_pos, index = x_coordinate[node_index]

            # left node
            if x_pos >= 0:
                alive[index] = True
                bisect.insort(y_segments, [rectangles[index][1], index, 0])
                bisect.insort(y_segments, [rectangles[index][3], index, 1])
                y_length = get_valid_length(y_segments)

            # right node
            else:
                alive[index] = False
                y_segments.remove([rectangles[index][1], index, 0])
                y_segments.remove([rectangles[index][3], index, 1])
                y_length = get_valid_length(y_segments)

            if node_index < rec_cnt * 2 - 1:
                area += y_length * (abs(x_coordinate[node_index + 1][0]) - abs(x_pos))

        return area % (10 ** 9 + 7)


if __name__ == '__main__':
    print(Solution.rectangleArea(rectangles=[[0, 0, 2, 2], [1, 1, 3, 3]]))
    print(Solution.rectangleArea([[22, 24, 67, 34], [23, 18, 39, 41], [10, 63, 80, 98]]))
    print(Solution.rectangleArea(rectangles=[[25, 20, 70, 27], [68, 80, 79, 100], [37, 41, 66, 76]]))

"""
提前垮起个拉拉肥批脸

大意了，一上手建了最大和最小两个堆去维护矩形们的最大上边界和最小下边界，还没有意识到自己的思维停留在一维扫描线的情况下
复盘一下，需要先在x轴上进行扫描，将扫描出来的切片存在数组中；
再以此对数组中的切片根据y轴进行扫描，得到切片的有效长度，再以x轴的扫描结果得到面积
y轴每个切片都要进行排序，最多对N个元素进行有限次堆操作，最多有2N个切片，时间复杂度为O(N^2log(N))
很难

做到了！投稿者：变态刷题人
好难啊好难啊好难啊好难啊好难啊好难啊好难啊好难啊
再看看线段树怎么写
"""

"""
rec_cnt = len(rectangles)
alive = [False] * rec_cnt
change_log = [[-1, 0]]  # a list of [x_coordinate, Δy]
y2_pos, y1_pos = [], []
highest, lowest = [], []  # highest maintains -y2
area = 0

for index in range(len(rectangles)):
    # rectangle = [x1, y1, x2, y2] (x1 < x2, y1 < y2)
    # (x1, y1) is the bottom-left corner, (x2, y2) is the top-right corner
    x1, y1, x2, y2 = rectangles[index]

    # a list of [-y2, x coordinate, index]
    y2_pos.append([-y2, x1, index])
    y2_pos.append([-y2, -x2, index])

    # a list of [y1, x coordinate, index]
    y1_pos.append([y1, x1, index])
    y1_pos.append([y1, -x2, index])

y2_pos.sort(key=lambda x: abs(x[1]))
y1_pos.sort(key=lambda x: abs(x[1]))

for index in range(rec_cnt * 2):
    y2_node, y1_node = y2_pos[index], y1_pos[index]
    change_flag = False
    higher, lower = 0, 0

    # left node
    if y2_node[1] >= 0:
        heapq.heappush(highest, y2_node)
        heapq.heappush(lowest, y1_node)
        alive[y2_node[2]] = True  # node_index = y2(1)_node[2]

        # maintaining highest heap
        while not alive[highest[0][2]]:
            heapq.heappop(highest)
        if highest[0][2] == y2_node[2]:  # that means the current node is the highest node
            change_flag = True
        higher = -highest[0][0]

        # maintaining lowest heap
        while not alive[lowest[0][2]]:
            heapq.heappop(lowest)
        if lowest[0][2] == y1_node[2]:
            change_flag = True
            lower = lowest[0][0]

    # right node
    else:
        alive[y2_node[2]] = False
        if not alive[highest[0][2]] or not alive[lowest[0][2]]:
            change_flag = True
            try:
                while not alive[highest[0][2]]:
                    heapq.heappop(highest)
                while not alive[lowest[0][2]]:
                    heapq.heappop(lowest)
                higher, lower = -highest[0][0], lowest[0][0]
            # empty heaps
            except IndexError:
                higher = lower = 0

    if change_flag:
        x_coordinate, delta_y = abs(y1_node[1]), higher - lower
        area += (x_coordinate - change_log[-1][0]) * change_log[-1][1]
        change_log.append([x_coordinate, delta_y])

return area % (10 ** 9 + 7)
"""
