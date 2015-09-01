__author__ = 'liangl2'
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} head
    # @return {boolean}
    def isPalindrome(self, head):
        if not head:
            return True
        p = head
        fwd_list = []
        while p:
            fwd_list.append(p.val)
            p = p.next
        reverse_head = reverse_linked_list(head)
        reverse_list = []
        while reverse_head:
            reverse_list.append(reverse_head.val)
            reverse_head = reverse_head.next

        for i in range(len(fwd_list)):
            if fwd_list[i] != reverse_list[i]:
                return False
        return True

def reverse_linked_list(head):
    p = head
    q = p.next
    head.next = None
    while q:
        r = q.next
        q.next = p
        p = q
        q = r
    return p

def print_list(head):
    while head:
        print(head.val)
        head = head.next

head = ListNode(1)
head.next = ListNode(1)
head.next.next = ListNode(2)
head.next.next.next = ListNode(1)
# head.next.next.next.next = ListNode(5)
# head.next.next.next.next.next = ListNode(8)
# print_list(head)
# a = head
# print_list(a)
s = Solution()
print(s.isPalindrome(head))