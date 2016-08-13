__author__ = 'Liang Li'
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param two ListNodes
    # @return the intersected ListNode
    def getIntersectionNode(self, headA, headB):
        if not (headA and headB):
            return None
        pa, pb = headA, headB
        while pa is not pb:
            pa = pa.next if pa else headB
            pb = pb.next if pb else headA
        return pa

headA = ListNode(2)
headA.next = ListNode(5)
headA.next.next = ListNode(8)
headA.next.next.next = ListNode(3)

headB = ListNode(1)
headB.next = ListNode(3)
headB.next.next = ListNode(7)
headB.next.next.next = ListNode(6)
headB.next.next.next.next = headA.next.next
headB.next.next.next.next.next = headA.next.next.next

s = Solution()
head = s.getIntersectionNode(headA, headB)
print(head.val)
