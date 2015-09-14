__author__ = 'Liang Li'
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        h = head
        node_dict = {}
        while h and h.next:
            if node_dict.get(h.next, None):
                return True
            else:
                node_dict[h.next] = True
            h = h.next
        return False


    def has_cycle(self, head):
        try:
            slow = head
            fast = head.next
            while slow != fast:
                slow = slow.next
                fast = fast.next.next
            return True
        except:
            return False

headA = ListNode(1)
headA.next = ListNode(5)
headA.next.next = ListNode(8)
headA.next.next.next = headA

s = Solution()
print(s.hasCycle(headA))
