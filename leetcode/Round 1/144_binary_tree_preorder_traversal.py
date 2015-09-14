__author__ = 'Liang Li'
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        node_list = []
        left = self.preorderTraversal(root.left)
        right = self.preorderTraversal(root.right)
        node_list = [root.val]+left+right
        return node_list

    def preorder_traversal(self, root):
        node_list = []
        node_stack = [root]
        while node_stack:
            node = node_stack.pop()
            if node:
                node_list.append(node.val)
                node_stack.append(node.right)
                node_stack.append(node.left)
        return node_list
