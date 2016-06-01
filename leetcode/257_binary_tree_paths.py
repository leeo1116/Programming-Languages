# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {string[]}
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :param root: tree root
        :return:
        """
        if not root:
            return []
        if not (root.left or root.right):
            return [str(root.val)]
        left = []
        right = []
        if root.left:
            for i in self.binaryTreePaths(root.left):
                left.append(str(root.val) + "->" + i)
        if root.right:
            for j in self.binaryTreePaths(root.right):
                right.append(str(root.val) + "->" + j)
        tree_path = left+right
        return tree_path


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
# root.right.right = TreeNode(7)

s = Solution()
print(s.binaryTreePaths(root))

