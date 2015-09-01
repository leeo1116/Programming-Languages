__author__ = 'liangl2'
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} root
    # @param {TreeNode} p
    # @param {TreeNode} q
    # @return {TreeNode}
    def lowest_common_ancestor(self, root, p, q):
        if (p.val-root.val)*(q.val-root.val) <= 0:
            return root
        if p.val > root.val and q.val > root.val:
            return self.lowest_common_ancestor(root.right, p, q)
        elif p.val < root.val and q.val < root.val:
            return self.lowest_common_ancestor(root.left, p, q)


root = TreeNode(8)
root.left = TreeNode(6)
root.left.left = TreeNode(1)
root.left.right = TreeNode(4)
root.right = TreeNode(10)
root.right.left = TreeNode(9)
root.right.right = TreeNode(12)
root.right.right.left = TreeNode(11)

s = Solution()
p = TreeNode(11)
q = TreeNode(11)
LCA = s.lowest_common_ancestor(root, p, q)
print(LCA.val)


