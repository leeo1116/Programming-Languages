# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.sum_root_to_leafs(root, 0)

    def sum_root_to_leafs(self, root, parents_sum):
        if not root:
            return 0
        if not (root.left or root.right):
            return parents_sum*10+root.val
        return self.sum_root_to_leafs(root.left, parents_sum*10+root.val)+self.sum_root_to_leafs(root.right, parents_sum*10+root.val)


root = TreeNode(1)
root.left = TreeNode(2)
# root.right = TreeNode(3)
# root.left.left = TreeNode(4)
# root.left.right = TreeNode(5)
# root.right.left = TreeNode(6)
# root.right.right = TreeNode(7)

s = Solution()
print(s.sumNumbers(root))