# Given a binary tree, find its minimum depth.
#
# The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        total = []
        def getDepth(node, depth):
            if node.left == None and node.right == None:
                total.append(depth + 1)
            if node.left is not None:
                getDepth(node.left, depth+1)
            if node.right is not None:
                getDepth(node.right, depth+1)
        getDepth(root, 0)
        res = min(total)
        return res
