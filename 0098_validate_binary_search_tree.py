"""
给你一个二叉树的根节点 root ，判断其是否是一个有效的二叉搜索树。
有效 二叉搜索树定义如下：
节点的左子树只包含 小于 当前节点的数。
节点的右子树只包含 大于 当前节点的数。
所有左子树和右子树自身必须也是二叉搜索树。
https://leetcode-cn.com/problems/validate-binary-search-tree
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    @staticmethod
    def isValidBST(root: TreeNode) -> bool:
        seen = [-2 ** 31 - 1]

        def left_order(node):
            nonlocal seen
            left, right = node.left, node.right
            if left:
                left_order(left)
            seen.append(node.val)
            if right:
                left_order(right)

        left_order(root)

        for index in range(1, len(seen)):
            if seen[index - 1] >= seen[index]:
                return False

        return True


"""
金龙盘旋 POSSESSION 真是 好听！

有额外数据结构的题目不想生成测试例就得尝试一步写好
用了遍历和额外数组那么成绩第也是理所应当的嘛（心虚）
"""
