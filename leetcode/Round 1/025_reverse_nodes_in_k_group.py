__author__ = 'Liang Li'
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} k
    # @return {ListNode}
    def reverseKGroup(self, head, k):
        if not head or k < 2:
            return head

        head_tmp = head
        for i in range(k-1):
            head_tmp = head_tmp.next
            if not head_tmp:
                return head
        h = None
        p = head
        for i in range(k):
            q = p.next
            p.next = h
            h = p
            p = q

        head.next = self.reverseKGroup(p, k)
        return head_tmp

    def reverse_nodes_in_k_group_iterative(self, head, k):
        if not head or k < 2:
            return head

        h_tmp = head
        for i in range(k-1):
            h_tmp = h_tmp.next
            if not h_tmp:
                return head
        final_head = h_tmp

        p = head
        q = head
        while p:
            h = p
            p = h.next
            tail = q
            for i in range(k):
                q = p.next
                p.next = h
                h = p
                p = q
            tail.next = h
        return final_head

head = ListNode(1)
head.next = ListNode(4)
head.next.next = ListNode(5)
head.next.next.next = ListNode(9)

s = Solution()
final_head = s.reverse_nodes_in_k_group_iterative(head, 3)
while final_head:
    print(final_head.val)
    final_head = final_head.next
