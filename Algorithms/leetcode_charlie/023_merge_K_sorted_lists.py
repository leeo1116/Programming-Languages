__doc__ = """
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.
"""


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def __init__(self):
        pass

    def merge_K_sorted_lists_divide_conquer(self, lists):
        """

        :param lists:
        :return:
        """
        lists_len = len(lists)
        if not lists or lists_len < 1:
            return None
        if lists_len == 1:
            return lists[0]
        if lists_len == 2:
            return self.merge_two_sorted_lists(lists[0], lists[1])
        mid = lists_len // 2
        return self.merge_two_sorted_lists(self.mergeKLists(lists[:mid]),
                                           self.mergeKLists(lists[mid:]))

    def merge_two_sorted_lists(self, l1, l2):
        if not l1:
            return l2
        if not l2:
            return l1
        head = p = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                p.next = l1
                l1 = l1.next
            else:
                p.next = l2
                l2 = l2.next
            p = p.next
        if l1:
            p.next = l1
        if l2:
            p.next = l2
        return head.next