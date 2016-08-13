__doc__ = """
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of
the first two lists.
"""


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def __init__(self):
        pass

    def merge_two_sorted_list(self, l1, l2):
        if not l1:
            return l2
        if not l2:
            return l1
        h = l = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                l.next = l1
                l1 = l1.next
            else:
                l.next = l2
                l2 = l2.next
            l = l.next
        if l1:
            l.next = l1
        elif l2:
            l.next = l2
        return h.next


head1 = ListNode(0)
l1 = head1
list_value1 = [1, 2, 5]
for i in list_value1:
    l1.next = ListNode(i)
    l1 = l1.next

head2 = ListNode(0)
l2 = head2
list_value2 = [3, 4]
for i in list_value2:
    l2.next = ListNode(i)
    l2 = l2.next

l1 = head1.next
l2 = head2.next

while l1:
    print(l1.val, end=', ')
    l1 = l1.next
print()
while l2:
    print(l2.val, end=', ')
    l2 = l2.next
print()
s = Solution()
h = s.merge_two_sorted_list(head1.next, head2.next)

while h:
    print(h.val, end=', ')
    h = h.next
