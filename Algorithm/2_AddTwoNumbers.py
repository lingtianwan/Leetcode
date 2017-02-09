# You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
#
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 == None or l2 == None:
            return None
        head = ListNode(0)
        res = head
        more = 0
        while l1 and l2:
            temp = l1.val + l2.val + more
            more = 0
            if temp >= 10:
                temp -= 10
                more = 1
            res.next = ListNode(temp)
            res = res.next
            l1 = l1.next
            l2 = l2.next
        x = None
        if l1:
            x = l1
        if l2:
            x = l2
        while x:
            temp = x.val + more
            more = 0
            if temp >= 10:
                temp -= 10
                more = 1
            res.next = ListNode(temp)
            res = res.next
            x = x.next
        if more == 1:
            res.next = ListNode(1)
        return head.next
