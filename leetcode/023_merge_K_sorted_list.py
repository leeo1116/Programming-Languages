__author__ = 'Liang Li'
import heapq
# class ListNode:
def __init__(self, x):
    self.val = x
    self.next = None

class Solution:
    # @param {ListNode[]} lists
    # @return {ListNode}
    def mergeKLists_naive(self, lists):
        all = []
        for node in lists:
            while node:
                all.append(node.val)
                node = node.next
        all.sort()
        return all

    def merge_K_lists_divide_conquer(self, lists):
        n = len(lists)
        if not lists or n == 0:
            return None
        elif n == 1:
            return lists[0]
        elif n == 2:
            return self.merge_two_sorted_lists(lists[0], lists[1])
        else:
            mid = n//2
            return self.merge_K_lists_divide_conquer([self.merge_K_lists_divide_conquer(lists[:mid]), self.merge_K_lists_divide_conquer(lists[mid:])])

    def merge_two_sorted_lists(self, l1, l2):
        dummy = cur = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
                cur = cur.next
            else:
                cur.next = l2
                l2 = l2.next
                cur = cur.next
        if l1:
            cur.next = l1
        if l2:
            cur.next = l2
        return dummy.next

    def merge_K_lists(self, lists):
        if not lists:
            return None

        min_heap = [(l.val, l) for l in lists if l]
        heapq.heapify(min_heap)
        dummy = cur = ListNode(0)

        while min_heap:
            pop = heapq.heappop(min_heap)
            cur.next = pop[1]
            cur = cur.next
            if cur.next:
                heapq.heappush(min_heap, (cur.next.val, cur.next))

        return dummy.next


