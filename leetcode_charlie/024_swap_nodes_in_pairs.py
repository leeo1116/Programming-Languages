__doc__ = """
Given a linked list, swap every two adjacent nodes and return its head.

For example,
Given 1->2->3->4, you should return the list as 2->1->4->3.

Your algorithm should use only constant space. You may not modify the values in the list, only nodes itself can be changed.
"""


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def __init__(self):
        pass

    def swap_nodes_in_pairs(self, head):
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
h = s.swap_nodes_in_pairs(head)
while h:
    print(h.val)
    h = h.next
