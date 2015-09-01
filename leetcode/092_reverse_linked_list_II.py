__author__ = 'Liang Li'
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
# need revision
class Solution:
    # @param {ListNode} head
    # @param {integer} m
    # @param {integer} n
    # @return {ListNode}
    def reverseBetween(self, head, m, n):
        if not head:
            return head
        m_tmp = m
        h = head
        while m-2 > 0:
            h = h.next
            m -= 1
        pre_head = h
        h = h.next
        if not h:
            return head
        sub_head = h
        p = h.next
        while n-m_tmp:
            q = p.next
            p.next = h
            h = p
            p = q
            n -= 1
        pre_head.next = h
        sub_head.next = p
        return head

head = ListNode(1)
head.next = ListNode(1)
# head.next.next = ListNode(2)
# head.next.next.next = ListNode(1)
# head.next.next.next.next = ListNode(5)
# head.next.next.next.next.next = ListNode(8)

s = Solution()
head = s.reverseBetween(head, 1, 2)
while head:
    print(head.val)
    head = head.next

