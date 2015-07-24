__author__ = 'liangl2'
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} l1
    # @param {ListNode} l2
    # @return {ListNode}
    def mergeTwoLists(self, l1, l2):
        l = l1 if l1.val < l2.val else l2
        while l1 and l2:
            l1, l2 = p1, p2
            while l1.val < l2.val and l1:
                l1 = l1.next
            p1 = l1.next
            l1.next = l2

            else:
                l2.next = l1
                l2 = p2
        return l

headA = ListNode(2)
headA.next = ListNode(4)
headA.next.next = ListNode(5)
# headA.next.next.next = ListNode(9)

headB = ListNode(1)
headB.next = ListNode(3)
headB.next.next = ListNode(7)
# headB.next.next.next = ListNode(8)


def print_list(head):
    while head:
        print(head.val)
        head = head.next

s = Solution()
headC = s.mergeTwoLists(headA, headB)
print_list(headC)