__author__ = 'liangl2'
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def deleteDuplicates(self, head):
        if not head:
            return head
        p = head
        while p.next:
            if p.val == p.next.val:
                p.next = p.next.next
            else:
                p = p.next
        return head

head = ListNode(2)
head.next = ListNode(5)
head.next.next = ListNode(5)
head.next.next.next = ListNode(5)
head.next.next.next.next = ListNode(5)
head.next.next.next.next.next = ListNode(8)

s = Solution()
new_head = s.deleteDuplicates(head)
while new_head:
    print(new_head.val)
    new_head = new_head.next