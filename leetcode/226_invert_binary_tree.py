# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return
        if root.left:
            self.invertTree(root.left)
        if root.right:
            self.invertTree(root.right)
        root.left, root.right = root.right, root.left
        return root
    

def pre_order_traverse(root, nodes_list):
    if not root:
        return
    nodes_list.append(root.val)
    pre_order_traverse(root.left, nodes_list)
    pre_order_traverse(root.right, nodes_list)


t_root = TreeNode(4)
t_root.left = TreeNode(2)
t_root.right = TreeNode(7)
t_root.left.left = TreeNode(1)
t_root.left.right = TreeNode(3)
t_root.right.left = TreeNode(6)
t_root.right.right = TreeNode(9)

tree_nodes1 = []
pre_order_traverse(t_root, tree_nodes1)
print(tree_nodes1)

s = Solution()
s.invertTree(t_root)
tree_nodes2 = []
pre_order_traverse(t_root, tree_nodes2)
print(tree_nodes2)