__author__ = 'Liang Li'
# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        node_list = []
        left = self.postorderTraversal(root.left)
        right = self.postorderTraversal(root.right)
        node_list = left+right+[root.val]
        return node_list

    def postorder_traverse(self, root):
        if not root:
            return []
        node_list = []
        node_stack = [(root, False)]  # current node, is visited
        while node_stack:
            current_node, is_visited = node_stack.pop()
            if current_node:
                if is_visited:
                    node_list.append(current_node.val)
                else:
                    node_stack.append((current_node, True))
                    node_stack.append((current_node.right, False))
                    node_stack.append((current_node.left, False))
        return node_list

root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)
root.left.left = TreeNode(5)
root.right.left = TreeNode(4)
root.right.right = TreeNode(6)
root.right.right.right = TreeNode(7)

s  = Solution()
print(s.postorder_traverse(root))