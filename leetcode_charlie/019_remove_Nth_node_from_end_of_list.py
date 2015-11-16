import random
__doc__ = """
Given a linked list, remove the nth node from the end of list and return its head.

For example,

   Given linked list: 1->2->3->4->5, and n = 2.

   After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:
Given n will always be valid.
Try to do this in one pass.
"""


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def __init__(self):
        pass

    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        while not head:
            return head
        p, h = head, head
        while n and p:
            p = p.next
            n -= 1
        if not p:
            return head
        while p.next:
            p = p.next
            h = h.next
        h.next = h.next.next
        return head

i = 5
head = ListNode(0)
h = head
# while i:
#     h.next = ListNode(random.randint(1, 10))
#     h = h.next
#     i -= 1

list_value = [1, 2]
for i in list_value:
    h.next = ListNode(i)
    h = h.next

h = head.next
while h:
    print(h.val)
    h = h.next

s = Solution()
h = s.removeNthFromEnd(head.next, 2)
while h:
    print(h.val)
    h = h.next