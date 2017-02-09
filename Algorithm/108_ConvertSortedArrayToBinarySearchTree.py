# Given an array where elements are sorted in ascending order, convert it to a height balanced BST.


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        n = len(nums)
        if n == 0:
            return None
        if n == 1:
            return TreeNode(nums[0])
        root = TreeNode(nums[n // 2])
        left = self.sortedArrayToBST(nums[:n // 2])
        right = self.sortedArrayToBST(nums[n // 2 + 1:])
        root.left = left
        root.right = right
        return root
