__doc__ = """
 Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

You may not alter the values in the nodes, only nodes itself may be changed.

Only constant memory is allowed.

For example,
Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5
"""


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def __init__(self):
        pass

    def reverse_nodes_in_k_group(self, head, k):
        """
        :type head: ListNode
        :type k: integer
        :param head: head of a linked list
        :param k: group number
        :rtype h: ListNode
        :return h: new head
        """
        n = k
        if not (head and n):
            return head
        # Get Kth node, and cut the list
        p1 = head
        while n-1 and p1:
            p1 = p1.next
            n -= 1

        if not p1:
            return head
        else:
            head1 = p1.next
            p1.next = None

        # Reverse cut list
        p2 = head
        p3 = p2.next
        while p3:
            p4 = p3.next
            p3.next = p2
            p2 = p3
            p3 = p4
        h = p2
        # Concatenate cut list with remaining list
        head.next = self.reverse_nodes_in_k_group(head1, k)

        return h


head = ListNode(4)
head.next = ListNode(5)
head.next.next = ListNode(6)
head.next.next.next = ListNode(7)
head.next.next.next.next = ListNode(8)
head.next.next.next.next.next = ListNode(9)
s = Solution()
h = s.reverse_nodes_in_k_group(head, 2)

while h:
    print(h.val)
    h = h.next
