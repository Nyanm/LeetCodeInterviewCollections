"""
中位数是有序列表中间的数。如果列表长度是偶数，中位数则是中间两个数的平均值。
例如，
[2,3,4]的中位数是 3
[2,3] 的中位数是 (2 + 3) / 2 = 2.5
设计一个支持以下两种操作的数据结构：
void addNum(int num) - 从数据流中添加一个整数到数据结构中。
double findMedian() - 返回目前所有元素的中位数。
https://leetcode-cn.com/problems/find-median-from-data-stream

Your MedianFinder object will be instantiated and called as such:
obj = MedianFinder()
obj.addNum(num)
param_2 = obj.findMedian()
"""
import heapq


class MedianFinder:

    def __init__(self):
        self.small_heap = []  # biggest element at top
        self.big_heap = []  # smallest element at top
        self.small_cnt, self.big_cnt = 0, 0
        # Especially, small heap is a negative heap, which means all its elements are negative numbers
        # Remember to times a -1 when using it
        # abs(small_cnt - big_cnt) <= 1

    def addNum(self, num: int) -> None:

        if self.small_cnt == self.big_cnt:
            if not self.small_heap:
                heapq.heappush(self.big_heap, num)
                self.big_cnt += 1
                return
            if num >= self.big_heap[0]:
                heapq.heappush(self.big_heap, num)
                self.big_cnt += 1
                return
            else:
                heapq.heappush(self.small_heap, -num)
                self.small_cnt += 1
                return

        elif self.small_cnt > self.big_cnt:
            if num >= -self.small_heap[0]:
                heapq.heappush(self.big_heap, num)
                self.big_cnt += 1
                return
            else:
                big_in_small = -heapq.heappop(self.small_heap)
                heapq.heappush(self.small_heap, -num)
                heapq.heappush(self.big_heap, big_in_small)
                self.big_cnt += 1
                return

        elif self.small_cnt < self.big_cnt:
            if num <= self.big_heap[0]:
                heapq.heappush(self.small_heap, -num)
                self.small_cnt += 1
                return
            else:
                small_in_big = heapq.heappop(self.big_heap)
                heapq.heappush(self.big_heap, num)
                heapq.heappush(self.small_heap, -small_in_big)
                self.small_cnt += 1
                return

    def findMedian(self) -> float:
        if not self.small_cnt and not self.big_cnt:
            return False
        if self.small_cnt > self.big_cnt:
            return -self.small_heap[0]
        elif self.small_cnt < self.big_cnt:
            return self.big_heap[0]
        else:
            return (self.big_heap[0] - self.small_heap[0]) / 2


"""
看到这道题的第一眼就意识到该用AVL写，可惜就可惜在我不会写
从评论区学来一个双堆解法（

Python居然没有内置大根堆，不过题目居然也没有负数数据，双向偷鸡了属于是
"""
