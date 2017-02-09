# Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).
#
# For example:
# Given binary tree [3,9,20,null,null,15,7],
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its level order traversal as:
# [
#   [3],
#   [9,20],
#   [15,7]
# ]


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        res = []
        tank = [root]
        while len(tank) > 0:
            node_val = []
            new_tank = []
            for node in tank:
                node_val.append(node.val)
                if node.left:
                    new_tank.append(node.left)
                if node.right:
                    new_tank.append(node.right)
            res.append(node_val)
            tank = new_tank[:]
        return res
