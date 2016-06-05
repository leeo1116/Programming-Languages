# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None
        nums_len = len(nums)
        mid = (nums_len-1)//2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])
        return root

    # def sorted_arry_to_BST(self, nums, low, high):
    #     mid = low+(high-low)//2
    #     root = TreeNode(nums[mid])
    #     root.left = self.sorted_arry_to_BST(nums[low:mid], low, )


def pre_order_traverse(root):
    if not root:
        return
    pre_order_traverse(root.left)
    print(root.val)
    # if not (root.left or root.right):
    #     print(root.val)
    pre_order_traverse(root.right)


def pre_order_traverse_list(root, nodes):
    if not root:
        return
    pre_order_traverse_list(root.left, nodes)
    nodes.append(root.val)
    # if not (root.left or root.right):
    #     print(root.val)
    pre_order_traverse_list(root.right, nodes)
    return nodes

s = Solution()
r = s.sortedArrayToBST([1, 2, 3, 4, 5, 6, 7])
pre_order_traverse(r)
print(pre_order_traverse_list(r, []))


