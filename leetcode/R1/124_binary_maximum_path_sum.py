__author__ = 'Liang Li'
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        Solution.max_sum = -(2 << 31)
        self.max_path_sum(root)
        return Solution.max_sum

    def max_path_sum(self, root):
        if not root:
            return 0
        left = max(0, self.max_path_sum(root.left))
        right = max(0, self.max_path_sum(root.right))
        Solution.max_sum = max(Solution.max_sum, left+right+root.val)
        return max(left, right)+root.val