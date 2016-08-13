__author__ = 'Liang Li'
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return root == None or self.is_symmetric(root.left, root.right)

    def is_symmetric(self, left, right):
        if left == None or right == None:
            return left == right
        if left.val != right.val:
            return False
        return self.is_symmetric(left.left, right.right) and self.is_symmetric(left.right, right.left)

class Solution_stack(object):
    def is_symmetric(self, root):
        if not root:
            return True
        node_stack = [[root.left, root.right]]
        while len(node_stack) > 0:
            pair = node_stack.pop(0)
            left = pair[0]
            right = pair[1]

            if not left and not right:
                continue
            if not left or not right:
                return False
            if left.val == right.val:
                node_stack.insert(0, [left.left, right.right])
                node_stack.insert(0, [left.right, right.left)])
            else:
                return False
        return True


