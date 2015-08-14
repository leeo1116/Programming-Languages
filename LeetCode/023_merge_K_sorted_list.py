__author__ = 'Liang Li'
# class ListNode:
def __init__(self, x):
    self.val = x
    self.next = None

class Solution:
    # @param {ListNode[]} lists
    # @return {ListNode}
    def mergeKLists(self, lists):
        min_node_val = lists[0].val
        for node in lists:
            if node.val < min_node_val:
                min_node_val = node.val
