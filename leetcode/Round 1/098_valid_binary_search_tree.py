__author__ = 'liangl2'
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {boolean}
    def isValidBST(self, root):
        output = []
        self.in_order(root, output)

        for i in range(1, len(output)):
            if output[i-1] >= output[i]:
                return False

        return True

    def in_order(self, root, output):
        if root is None:
            return

        self.in_order(root.left, output)
        output.append(root.val)
        self.in_order(root.right, output)