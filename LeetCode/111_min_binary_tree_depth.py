__author__ = 'liangl2'
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer}
    def min_binary_tree_depth(self, root):
        if root is None:
            return 0
        while root:
            print(root.val)
            left_depth = 1+self.min_binary_tree_depth(root.left)
            right_depth = 1+self.min_binary_tree_depth(root.right)
            return left_depth
        if left_depth < right_depth:
            return left_depth
        else:
            return right_depth

root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)
root.left.left = TreeNode(5)
root.right.left = TreeNode(4)
root.right.right = TreeNode(6)
root.right.right.right = TreeNode(7)

# print(root.right.left.val)
s = Solution()
min_depth = s.min_binary_tree_depth(root)
print(min_depth)
