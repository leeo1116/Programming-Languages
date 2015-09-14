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
        if root.left is None:
            return self.min_binary_tree_depth(root.right)+1
        if root.right is None:
            return self.min_binary_tree_depth(root.left)+1
        return min(self.min_binary_tree_depth(root.left), self.min_binary_tree_depth(root.right))+1

root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)
root.left.left = TreeNode(5)
root.right.left = TreeNode(4)
root.right.right = TreeNode(6)
root.right.right.right = TreeNode(7)

s = Solution()
min_depth = s.min_binary_tree_depth(root)
print(min_depth)
