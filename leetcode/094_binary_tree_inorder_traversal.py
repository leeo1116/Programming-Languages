__author__ = 'Liang Li'
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer[]}
    def inorderTraversal(self, root):
        node_list = []
        self.in_order_traverse(root, node_list)
        return node_list

    def in_order_traverse(self, root, node_list):
        # b.c.
        if not root:
            return
        self.in_order_traverse(root.left, node_list)
        node_list.append(root.val)
        self.in_order_traverse(root.right, node_list)

class Solution_iterative(Solution):
    def in_order_traverse_iterative(self, root):
        stack = []
        node_list = []
        current = root
        done = False
        while not done:
            if current:
                stack.append(current)
                current = current.left
            else:
                if not stack:
                    return node_list
                else:
                    current = stack[-1]
                    node_list.append(current.val)
                    stack.pop()
                    current = current.right

root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)
root.left.left = TreeNode(5)
root.right.left = TreeNode(4)
root.right.right = TreeNode(6)
root.right.right.right = TreeNode(7)

s = Solution()
print(s.inorderTraversal(root))
s = Solution_iterative()
print(s.in_order_traverse_iterative(root))