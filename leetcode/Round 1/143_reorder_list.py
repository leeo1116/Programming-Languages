__author__ = 'Liang Li'
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if not (head and head.next):
            return
        h1, h2 = self.split_list(head)
        h2 = self.reverse_list(h2)
        head = self.merge_list(h1, h2)
        return head

    def split_list(self, head):
        fast, slow = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        h2 = slow.next
        slow.next = None
        return head, h2

    def reverse_list(self, head):
        if not head:
            return head
        h = head
        p = h.next
        h.next = None
        while p:
            q = p.next
            p.next = h
            h = p
            p = q
        return h

    def merge_list(self, h1, h2):
        h = ListNode(0)
        head = h
        while h1 and h2:
            h1_next = h1.next
            h2_next = h2.next

            h.next = h1
            h = h.next
            h.next = h2
            h = h.next

            h1 = h1_next
            h2 = h2_next
        h.next = h1 if h1 else h2
        return head.next

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

s = Solution()
h = (s.reorderList(head))
while h:
    print(h.val)
    h = h.next