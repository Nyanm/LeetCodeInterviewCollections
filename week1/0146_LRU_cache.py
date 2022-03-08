"""
请你设计并实现一个满足 LRU (最近最少使用) 缓存 约束的数据结构。
实现 LRUCache 类：
LRUCache(int capacity) 以 正整数 作为容量capacity 初始化 LRU 缓存
int get(int key) 如果关键字 key 存在于缓存中，则返回关键字的值，否则返回 -1 。
void put(int key, int value)如果关键字key 已经存在，则变更其数据值value ；如果不存在，则向缓存中插入该组key-value 。
如果插入操作导致关键字数量超过capacity ，则应该 逐出 最久未使用的关键字。
函数 get 和 put 必须以 O(1) 的平均时间复杂度运行。
https://leetcode-cn.com/problems/lru-cache

Your LRUCache object will be instantiated and called as such:
obj = LRUCache(capacity)
param_1 = obj.get(key)
obj.put(key,value)
"""


class DoublyLinkedNode:

    def __init__(self, front=None, back=None, val: int = None, key: int = None):
        self.front = front
        self.back = back
        self.val = val
        self.key = key


def link_node(front: DoublyLinkedNode, back: DoublyLinkedNode):
    front.back = back
    back.front = front


def delete_node(poor: DoublyLinkedNode, soft=False):
    poor.front.back = poor.back
    poor.back.front = poor.front
    if not soft:
        del poor


class LRUCache:

    def __init__(self, capacity: int):

        self.capacity = capacity
        self.element = 0
        self.hash = {}

        self.head = DoublyLinkedNode()
        self.tail = DoublyLinkedNode()
        link_node(self.head, self.tail)

    def get(self, key: int) -> int:
        try:
            cur = self.hash[key]
            if cur is False:  # deleted
                return -1

            res = cur.val
            delete_node(cur, soft=True)
            link_node(cur, self.head.back)
            link_node(self.head, cur)

            return res

        except KeyError:  # never been inserted
            return -1

    def put(self, key: int, value: int) -> None:
        try:
            if self.hash[key] is not False:
                self.hash[key].val = value
                self.get(key)
                return
        except KeyError:
            pass
        self.element += 1

        new_node = DoublyLinkedNode(val=value, key=key)
        link_node(new_node, self.head.back)
        link_node(self.head, new_node)
        self.hash[key] = new_node

        if self.element > self.capacity:
            old_node = self.tail.front
            self.hash[old_node.key] = False
            delete_node(old_node)
            self.element -= 1

    def glance(self):
        print(f'Number:{self.element}', end='  ')
        temp = self.head
        while temp.back:
            print(temp.val, end=' ')
            temp = temp.back
        print()

# 虽然跑起来效率像屎，但是好歹写出来了
