"""
路径 被定义为一条从树中任意节点出发，沿父节点-子节点连接，达到任意节点的序列。同一个节点在一条路径序列中 至多出现一次 。该路径 至少包含一个 节点，且不一定经过根节点。
路径和 是路径中各节点值的总和。
给你一个二叉树的根节点 root ，返回其 最大路径
https://leetcode-cn.com/problems/binary-tree-maximum-path-sum
"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    @staticmethod
    def maxPathSum(root: Optional[TreeNode]) -> int:
        max_val = -1000

        def preorder(node):
            nonlocal max_val
            left_val, right_val = 0, 0

            if not node.left and not node.right:
                # lowermost node
                max_val = max(max_val, node.val)

            if node.left:
                preorder(node.left)
                left_val = node.left.val
            if node.right:
                preorder(node.right)
                right_val = node.right.val

            max_val = max(node.val + left_val, node.val + right_val, node.val + left_val + right_val, max_val, node.val)
            node.val = max(node.val + left_val, node.val + right_val, node.val)

        preorder(root)
        return max_val


"""
笑死，写了个巨长无比的max()
空间效率意外地高，然后递归嘛，时间长也是正常的（自慢）
"""
