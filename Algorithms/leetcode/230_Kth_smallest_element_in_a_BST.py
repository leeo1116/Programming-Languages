# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        count = self.count_nodes(root.left)
        if k <= count:
            return self.kthSmallest(root.left, k)
        elif k > count+1:
            return self.kthSmallest(root.right, k-count-1)
        else:  # k == count+1
            return root.val

    def count_nodes(self, root):
        return 1+self.count_nodes(root.left)+self.count_nodes(root.right) if root else 0



root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(6)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(5)
root.right.right = TreeNode(7)

s = Solution()
print(s.kthSmallest(root, 2))