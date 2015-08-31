__author__ = 'Liang Li'
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        h, p = head, head
        q = h
        while p:
            while q:
                if q.val < p.val:
                    q_pre = q
                    q = q.next
            q_pre.next = p
            p.next = q
