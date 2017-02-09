# Given a singly linked list L: L0→L1→…→Ln-1→Ln,
# reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…
#
# You must do this in-place without altering the nodes' values.
#
# For example,
# Given {1,2,3,4}, reorder it to {1,4,2,3}.


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if head is None or head.next is None:
            return
        slow = head
        fast = head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        left = head
        right = slow.next
        slow.next = None
        dummy = ListNode(0)
        dummy.next = right
        p = right.next
        right.next = None
        while p:
            tmp = p
            p = p.next
            tmp.next = dummy.next
            dummy.next = tmp
        right = dummy.next
        while right:
            tmp1 = left.next
            tmp2 = right.next
            left.next = right
            right.next = tmp1
            left = tmp1
            right = tmp2
        return
