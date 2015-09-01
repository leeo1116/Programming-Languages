__author__ = 'liangl2'
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} k
    # @return {ListNode}
    def rotateRight(self, head, k):
        if not head:
            return head
        dh = ListNode(0)
        dh.next = head
        p1 = p2 = dh
        list_len = 0
        while p2.next:
            p2 = p2.next
            list_len += 1
        for i in range(list_len-k%list_len):
            p1 = p1.next

        p2.next = head
        head = p1.next
        p1.next = None
        return head

head = ListNode(1)
head.next = ListNode(3)
# head.next.next = ListNode(2)
# head.next.next.next = ListNode(6)
# head.next.next.next.next = ListNode(5)
# head.next.next.next.next.next = ListNode(8)

s = Solution()
head = s.rotateRight(head, 2)
while head:
    print(head.val)
    head = head.next

