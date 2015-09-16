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
        if not l1 and l2:
            return l2
        elif not l2 and l1:
            return l1
        elif not l1 and not l2:
            return None
        l = l1 if l1.val < l2.val else l2
        while l1 and l2:
            if l1.val < l2.val:
                while l1 and l1.val < l2.val:
                    last_l1 = l1
                    l1 = l1.next
                last_l1.next = l2
            else:
                while l2 and l2.val <= l1.val:
                    last_l2 = l2
                    l2 = l2.next
                last_l2.next = l1
        return l

headA = ListNode(1)
# headA.next = ListNode(4)
# headA.next.next = ListNode(5)
# headA.next.next.next = ListNode(9)

headB = ListNode(1)
# headB.next = ListNode(3)
# headB.next.next = ListNode(7)
# headB.next.next.next = ListNode(8)


def print_list(head):
    while head:
        print(head.val)
        head = head.next

s = Solution()
headC = s.mergeTwoLists(headA, headB)
print_list(headC)