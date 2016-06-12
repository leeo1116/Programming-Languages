# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if not head:
            return None
        if not head.next:
            return TreeNode(head.val)
        slow, fast = head, head.next.next
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        mid_node = slow.next  # root
        slow.next = None  # cut in the middle
        root = TreeNode(mid_node.val)
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(mid_node.next)
        return root
    #     return self.sorted_list_to_BST(head, None)
    #
    # def sorted_list_to_BST(self, start, stop):
    #     if not start or start == stop:
    #         return start
    #
    #     mid_list_node = self.find_middle_list_node(start, stop)
    #     root = TreeNode(mid_list_node.val)
    #
    #     left_sub_tree = self.sorted_list_to_BST(start, mid_list_node)
    #     if left_sub_tree:
    #         root.left = TreeNode(left_sub_tree.val)
    #     else:
    #         root.left = None
    #
    #     right_sub_tree = self.sorted_list_to_BST(mid_list_node.next, stop)
    #     if right_sub_tree:
    #         root.right = TreeNode(right_sub_tree.val)
    #     else:
    #         root.right = None
    #
    #     return root
    #
    # def find_middle_list_node(self, start, stop):
    #     if not start:
    #         return start
    #     p1 = p2 = start
    #     while p2 != stop and p2.next != stop:
    #         p2 = p2.next.next
    #         p1 = p1.next
    #     return p1


head = ListNode(0)
head.next = ListNode(1)
head.next.next = ListNode(2)
head.next.next.next = ListNode(3)
head.next.next.next.next = ListNode(5)
head.next.next.next.next.next = ListNode(8)

s = Solution()
s.sortedListToBST(head).val
# while head:
#     print(head.val)
#     head = head.next
