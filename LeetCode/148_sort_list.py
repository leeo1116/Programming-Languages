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
        # Divide list into two parts
        p1, p2 = head.next, head
        while p1 and p1.next:
            p1 = p1.next.next
            p2 = p2.next
        h2 = p2.next
        p2.next = None
        list1 = self.sortList(head)
        list2 = self.sortList(h2)
        return self.merge(list1, list2)

    def merge(self, h1, h2):
        h = ListNode(0)
        head = h
        while h1 and h2:
            if h1.val < h2.val:
                h.next = h1
                h1 = h1.next
            else:
                h.next = h2
                h2 = h2.next
            h = h.next

        h.next = h1 if h1 else h2
        return head.next
