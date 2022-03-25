"""
297. 二叉树的序列化与反序列化
序列化是将一个数据结构或者对象转换为连续的比特位的操作，进而可以将转换后的数据存储在一个文件或者内存中，同时也可以通过网络传输到另一个计算机环境，采取相反方式重构得到原数据。
请设计一个算法来实现二叉树的序列化与反序列化。这里不限定你的序列 / 反序列化算法执行逻辑，你只需要保证一个二叉树可以被序列化为一个字符串并且将这个字符串反序列化为原始的树结构。
https://leetcode-cn.com/problems/serialize-and-deserialize-binary-tree
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    @staticmethod
    def serialize(root: TreeNode) -> str:
        if not root:
            return '[None]'
        nodes, is_valid = [root], root
        str_serial = ''
        while is_valid:
            is_valid = False
            new_nodes = []
            for node in nodes:
                if node:
                    str_serial += '%d,' % node.val
                else:
                    str_serial += 'None,'
                    continue

                if node.left:
                    new_nodes.append(node.left)
                    is_valid = True
                else:
                    new_nodes.append(None)
                if node.right:
                    new_nodes.append(node.right)
                    is_valid = True
                else:
                    new_nodes.append(None)
            nodes = new_nodes
        return '[%s]' % str_serial

    @staticmethod
    def deserialize(data: str) -> TreeNode:
        node_list = eval(data)
        node_num = len(node_list)
        if node_list[0] is not None:
            node_list[0] = TreeNode(node_list[0])
        father = 0
        for index in range(1, node_num):
            if node_list[index] is not None:
                node_list[index] = TreeNode(node_list[index])
                is_left = index % 2
                while not node_list[int(father)]:
                    father += 1
                if is_left:
                    node_list[int(father)].left = node_list[index]
                else:
                    node_list[int(father)].right = node_list[index]
            father += 0.5
        return node_list[0]


if __name__ == '__main__':
    test_node = Codec.deserialize('[4, 5, None,4,6,None,None,7,None,8,None,None,9,10]')
    print(test_node.right.right.left.val)
    test_str = Codec.serialize(test_node)
    # print(test_str)
