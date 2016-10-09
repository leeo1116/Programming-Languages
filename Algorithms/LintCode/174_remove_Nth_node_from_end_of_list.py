class ListNode(object):
    """
    Definition of ListNode
    """
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        Remove Nth node from end of list
        :param head:
        :param n:
        :return:
        """
        precursor = successor = head
        for i in range(n):
            if not precursor:
                return None
            precursor = precursor.next

        if not precursor:
            return head.next
        while precursor.next:
            precursor = precursor.next
            successor = successor.next
        successor.next = successor.next.next
        return head

