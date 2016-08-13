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

    def swap_pairs(self, head):
        if not (head and head.next):
            return head
        h = head.next
        p1 = head
        while p1 and p1.next:
            p2 = p1.next
            p1_tmp = p2.next
            if p1_tmp and p1_tmp.next:
                p1.next = p1_tmp.next
            else:
                p1.next = p1_tmp
            p2.next = p1
            p1 = p1_tmp

        return h

head = ListNode(4)
head.next = ListNode(5)
head.next.next = ListNode(6)
head.next.next.next = ListNode(7)
head.next.next.next.next = ListNode(8)
head.next.next.next.next.next = ListNode(9)
s = Solution()
# head = s.swapPairs(head)
h = s.swap_pairs(head)
while h:
    print(h.val)
    h = h.next