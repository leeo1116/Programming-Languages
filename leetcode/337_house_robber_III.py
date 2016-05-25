# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def rob(self, root):
        node_val_dict = {}
        return self.rob_helper(root, node_val_dict)

    def rob_helper(self, root, node_val_dict):
        """
        :type root: TreeNode
        :type node_val_dict: dict
        :rtype: int
        """
        if not root:
            return 0
        if node_val_dict.get(root, None):
            return node_val_dict.get(root)

        left_max = right_max = 0
        # rob root
        if root.left:
            left_max = self.rob_helper(root.left.left, node_val_dict) + self.rob_helper(root.left.right, node_val_dict)
        if root.right:
            right_max = self.rob_helper(root.right.left, node_val_dict) + self.rob_helper(root.right.right, node_val_dict)

        # not rob root
        root_max = self.rob_helper(root.left, node_val_dict) + self.rob_helper(root.right, node_val_dict)

        # max money that can be robbed with root
        money_max = max(left_max+right_max+root.val, root_max)
        node_val_dict[root] = money_max
        return money_max


t = TreeNode(3)
t.left = TreeNode(5)
t.right = TreeNode(4)
s = Solution()
print(s.rob(t))
