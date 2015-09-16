__author__ = 'liangl2'
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def swapPairs(self, head):
        h = head
        while h and h.next:
            p = h.next
            tmp = h.val
            h.val = p.val
            p.val = tmp

            h = p.next
        return head

head = ListNode(4)
head.next = ListNode(5)
head.next.next = ListNode(6)
head.next.next.next = ListNode(7)
head.next.next.next.next = ListNode(8)
head.next.next.next.next.next = ListNode(9)
s = Solution()
head = s.swapPairs(head)

while head:
    print(head.val)
    head = head.next