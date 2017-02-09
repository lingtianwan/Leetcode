# Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        values = []
        while head:
            values.append(head.val)
            head = head.next
        return self.sortedArrayToBST(values)

    def sortedArrayToBST(self, array):
        n = len(array)
        if n == 0:
            return None
        if n == 1:
            return TreeNode(array[0])
        root = TreeNode(array[n/2])
        root.left = self.sortedArrayToBST(array[:n/2])
        root.right = self.sortedArrayToBST(array[n/2+1:])
        return root
