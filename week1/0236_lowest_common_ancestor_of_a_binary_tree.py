"""
给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。
https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree/
"""
from copy import deepcopy


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    @staticmethod
    def lowestCommonAncestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        p_path, q_path = [], []
        stack = []

        def dfs(node: TreeNode):
            nonlocal p_path, q_path, stack
            stack.append(node)

            if node == p:
                p_path = deepcopy(stack)
            if node == q:
                q_path = deepcopy(stack)

            left, right = node.left, node.right
            if left:
                dfs(left)
            if right:
                dfs(right)

            stack.pop()

        dfs(root)
        common = root
        for index in range(min(len(p_path), len(q_path))):
            if p_path[index].val == q_path[index].val:
                common = p_path[index]
        return common


"""
时间空间各击败5%用户
倒立刷分了属于是
但是它的复杂的真的是O(n)啊！一定是递归的问题！
"""
