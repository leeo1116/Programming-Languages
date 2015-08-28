__author__ = 'liangl2'
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not (head and head.next):
            return head
        p, p1, p2 = head, head, head
        while p2 != None and p2.next != None:
            p = p1
            p1 = p1.next
            p2 = p2.next.next
        p.next = None
        h1 = self.sortList(head)
        h2 = self.sortList(p1)
        return self.merge(h1, h2)

    def merge(self, h1, h2):
        if not h1:
            return h2
        if not h2:
            return h1
        if h1.val < h2.val:
            h1.next = self.merge(h1.next, h2)
            return h1
        else:
            h2.next = self.merge(h1, h2.next)
            return h2

