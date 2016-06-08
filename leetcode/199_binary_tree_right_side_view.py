# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []

        left_nodes = [root.val]
        right_nodes = [root.val]
        if root.right:
            right_nodes += self.rightSideView(root.right)
        if root.left:
            left_nodes += self.rightSideView(root.left)

        if root.right:
            if len(right_nodes) >= len(left_nodes):
                return right_nodes
            else:
                return right_nodes+left_nodes[len(right_nodes):]
        else:
            return left_nodes


t_root = TreeNode(4)
t_root.left = TreeNode(2)
t_root.right = TreeNode(7)
# t_root.left.left = TreeNode(1)
t_root.left.right = TreeNode(3)
# t_root.right.left = TreeNode(6)
# t_root.right.right = TreeNode(9)

s = Solution()
print(s.rightSideView(t_root))
