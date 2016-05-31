# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        p = head
        q = p.next
        while q:
            r = q.next
            q.next = p
            p = q
            q = r
        head.next = None
        return q

    def reverse_list_recursive(self, head):
        if not head or not head.next:  # not head: to check if the linked list is empty,
            # head.next: if there is only one node, just return that node head
            return head
        # recursion
        p = head.next
        head.next = None
        new_head = self.reverse_list_recursive(p)
        p.next = head
        return new_head


h = ListNode(1)
h.next = ListNode(2)
h.next.next = ListNode(3)
h.next.next.next = ListNode(4)

s = Solution()
new_h = s.reverse_list_recursive(h)
while new_h:
    print(new_h.val)
    new_h = new_h.next
