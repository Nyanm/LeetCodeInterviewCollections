"""
给你一个字符串 s 和一个字符串列表 wordDict 作为字典。请你判断是否可以利用字典中出现的单词拼接出 s 。
注意：不要求字典中出现的单词全部都使用，并且字典中的单词可以重复使用。
https://leetcode-cn.com/problems/word-break
"""
from typing import List


def get_index(__char: str) -> int:
    return ord(__char) - 97


class TrieNode:

    def __init__(self, is_end=False, father=None):
        self.alphabet = [None] * 26
        self.father = father
        self.is_end = is_end
        self.char = None

    def add_node(self, char: str):
        char_index = get_index(char)
        child = TrieNode(father=self)
        child.char = char
        self.alphabet[char_index] = child
        return child

    def set_end(self):
        self.is_end = True

    def get_child(self, char: str):
        child = self.alphabet[get_index(char)]
        if child:
            return child
        else:
            return False


class Solution:
    @staticmethod
    def wordBreak(s: str, wordDict: List[str]) -> bool:
        length = len(s)
        memo = [True] + [False] * length
        for back in range(length):
            for front in range(back + 1, length + 1):
                if s[back:front] in wordDict and memo[back]:
                    memo[front] = True
        return memo[-1]

    @staticmethod
    def _wordBreak(s: str, wordDict: List[str]) -> bool:
        # generate trie
        root = TrieNode()
        for word in wordDict:
            cur = root
            for char in word:
                child = cur.get_child(char)
                if not child:
                    child = cur.add_node(char)
                cur = child
            cur.set_end()

        # search by using DFS
        cur = root
        length = len(s)
        seen = {}
        index = 0
        while True:

            seen[cur] = True
            print(index)
            if index == length:
                if cur.is_end:
                    return True
                index -= 1
                cur = cur.father
                continue

            child = cur.get_child(s[index])
            if child:
                if not seen.__contains__(child):
                    cur = child
                    index += 1
                    continue

            root_child = root.get_child(s[index])
            if root_child and cur.is_end:
                cur = root_child
                index += 1
                seen = {}
                continue

            index -= 1
            cur = cur.father
            if not cur:
                return False


"""
草，之前还很开心地说写了个嵌套List的土炮写法，现在报应就来了，需要回溯的时候就不得不要用指针维护父子关系了
写不出来写不出来写不出来失败了失败了失败了失败了失败了怎么这么多状况
DP在这里竟像是暴力解法

后来想了想前缀树相较于DP更像是一个DFS一个BFS，DP蹚过了所有的坑，而Trie则尝试（借助良好的输入）一发入魂
挫败感好强
"""
