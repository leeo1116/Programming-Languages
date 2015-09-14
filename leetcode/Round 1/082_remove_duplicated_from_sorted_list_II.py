__author__ = 'Liang Li'
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def deleteDuplicates(self, head):
        h = ListNode(0)
        h.next = head
        delete_val = None
        tail = h
        while head:
            if head and head.next and head.val == head.next.val:
                delete_val = head.val
            if delete_val == None or head.val != delete_val:
                tail.next = head
                tail = head
            head = head.next
        tail.next = None
        return h.next