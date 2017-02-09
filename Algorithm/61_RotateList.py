# Given a list, rotate the list to the right by k places, where k is non-negative.
#
# For example:
# Given 1->2->3->4->5->NULL and k = 2,
# return 4->5->1->2->3->NULL.


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head is None or head.next is None or k == 0:
            return head
        count = 0
        dummy = ListNode(0)
        dummy.next = head
        p = dummy
        while p.next:
            p = p.next
            count += 1
        p.next = dummy.next
        step = count - (k % count)
        for i in range(step):
            p = p.next
        res = p.next
        p.next = None
        return res
