"""
Trie（发音类似 "try"）或者说 前缀树 是一种树形数据结构，用于高效地存储和检索字符串数据集中的键。这一数据结构有相当多的应用情景，例如自动补完和拼写检查。
请你实现 Trie 类：
Trie() 初始化前缀树对象。
void insert(String word) 向前缀树中插入字符串 word 。
boolean search(String word) 如果字符串 word 在前缀树中，返回 true（即，在检索之前已经插入）；否则，返回 false 。
boolean startsWith(String prefix) 如果之前已经插入的字符串word 的前缀之一为 prefix ，返回 true ；否则，返回 false 。
https://leetcode-cn.com/problems/implement-trie-prefix-tree

Your Trie object will be instantiated and called as such:
obj = Trie()
obj.insert(word)
param_2 = obj.search(word)
param_3 = obj.startsWith(prefix)
"""


class Trie:

    @staticmethod
    def __get_index(char: str) -> int:
        return ord(char) - 97

    def __init__(self):
        self.top = [None] * 27
        # 26 characters and 1 "end" flag

    def insert(self, word: str) -> None:
        cur = self.top
        for char in word:
            if cur[self.__get_index(char)]:
                cur = cur[self.__get_index(char)]
            else:
                cur[self.__get_index(char)] = [None] * 27
                cur = cur[self.__get_index(char)]
        cur[-1] = True

    def search(self, word: str) -> bool:
        cur = self.top
        for char in word:
            if cur[self.__get_index(char)]:
                cur = cur[self.__get_index(char)]
            else:
                return False
        if cur[-1]:
            return True
        else:
            return False

    def startsWith(self, prefix: str) -> bool:
        cur = self.top
        for char in prefix:
            if cur[self.__get_index(char)]:
                cur = cur[self.__get_index(char)]
            else:
                return False
        return True


"""
按理来说应该给每一个节点封一个class然后用指针互相指
但是现在正好有这样一种嵌套List的土炮写法，那为什么不用呢？
（不过timing确实拉了

字符种类多的时候可以用哈希储存子节点 
"""
