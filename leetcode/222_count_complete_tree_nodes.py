# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        left_h = right_h = 0
        l = root
        r = root
        while l:
            l = l.left
            left_h += 1
        while r:
            r = r.right
            right_h += 1
        if left_h == right_h:
            return (1 << left_h)-1
        return 1+self.countNodes(root.left)+self.countNodes(root.right)


t_root = TreeNode(4)
t_root.left = TreeNode(2)
t_root.right = TreeNode(7)
t_root.left.left = TreeNode(1)
t_root.left.right = TreeNode(3)
t_root.right.left = TreeNode(6)
t_root.right.right = TreeNode(9)

s = Solution()
print(s.countNodes(t_root))
