# Sort a linked list using insertion sort.


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        while head:
            temp = dummy
            next = head.next
            while temp.next and temp.next.val < head.val:
                temp = temp.next
            head.next = temp.next
            temp.next = head
            head = next
        return dummy.next
