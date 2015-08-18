__author__ = 'Liang Li'
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} k
    # @return {ListNode}
    def reverseKGroup(self, head, k):
        h = head
        if not h.next:
            return h

        while h.next:
            h_tmp = h
            p = h.next
            for counter in range(k, 1):
                if h.next:
                    q = p.next
                    p.next = h
                    h = p
                    p = q
            h = p
            h_tmp.next = p

