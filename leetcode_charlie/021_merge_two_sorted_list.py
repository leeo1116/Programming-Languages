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
