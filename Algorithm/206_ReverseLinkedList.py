# Reverse a singly linked list.
#
# click to show more hints.
#
# Hint:
# A linked list can be reversed either iteratively or recursively. Could you implement both?


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        while head:
            next = head.next
            head.next = dummy.next
            dummy.next = head
            head = next
        return dummy.next
