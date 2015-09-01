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
        if not head:
            return head
        head_dummy = ListNode(0)
        p = head
        q = head_dummy
        p_next = None
        while p:
            p_next = p.next
            while q.next and q.next.val < p.val:
                q = q.next
            p.next = q.next
            q.next = p

            q = head_dummy
            p = p_next
        return head_dummy.next
