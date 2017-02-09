# Given a binary tree, return all root-to-leaf paths.
#
# For example, given the following binary tree:
#
#    1
#  /   \
# 2     3
#  \
#   5
# All root-to-leaf paths are:
#
# ["1->2->5", "1->3"]


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {string[]}
    def binaryTreePaths(self, root):
        self.ans = []
        if root is None:
            return self.ans
        def addPath(root, path):
            if root.left is None and root.right is None:
                self.ans += path,
            if root.left:
                addPath(root.left, path + "->" + str(root.left.val))
            if root.right:
                addPath(root.right, path + "->" + str(root.right.val))
        addPath(root, str(root.val))
        return self.ans
