__author__ = 'Liang Li'
# Definition for singly-linked list with a random pointer.
class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if not head:
            return None
        h = head
        head_copy = RandomListNode(h.label)
        h_copy = head_copy
        while h.next:
            h_copy.next = RandomListNode(h.next.label)
            h = h.next
            h_copy = h_copy.next
        h_copy.next = None

        h = head
        h_copy = head_copy
        while h:
            if h.random:
                h_copy.random = RandomListNode(h.random.label)
            h = h.next
            h_copy = h_copy.next

        return head_copy

head = RandomListNode(1)
head.next = RandomListNode(2)
head.next.next = RandomListNode(3)
head.next.next.next = RandomListNode(4)
head.next.next.next.next = RandomListNode(5)

head.random = head.next.next
head.next.random = head.next.next.next

s = Solution()
c_h = s.copyRandomList(head)

while c_h:
    print(c_h.label)
    c_h = c_h.next
