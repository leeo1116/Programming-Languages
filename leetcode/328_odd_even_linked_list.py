# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head

        even_head = head.next
        p1 = head.next.next
        p2 = head
        flag = 1
        while p1:
            tmp = p2.next
            p2.next = p1
            p2 = tmp
            flag += 1
            if p1.next:
                p1 = p1.next
            else:
                if flag % 2 == 0:
                    p1.next = even_head
                    p2.next = None
                else:
                    p2.next = even_head
                    p1.next = None
                break

        return head


h = ListNode(2)
h.next = ListNode(5)
h.next.next = ListNode(7)
h.next.next.next = ListNode(3)
# h.next.next.next.next = ListNode(4)

s = Solution()
new_head = s.oddEvenList(h)
while new_head:
    print(new_head.val)
    new_head = new_head.next
