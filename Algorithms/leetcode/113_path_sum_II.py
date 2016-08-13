# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if not root:
            return []
        if root.val == sum and not root.left and not root.right:
            return [[root.val]]

        path_list = []
        left_path_list = self.pathSum(root.left, sum-root.val)
        right_path_list = self.pathSum(root.right, sum-root.val)

        for left_path in left_path_list:
            if left_path:
                path_list.append([root.val]+left_path)

        for right_path in right_path_list:
            if right_path:
                path_list.append([root.val]+right_path)
        return path_list


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(5)
root.left.right = TreeNode(6)
root.right.left = TreeNode(5)
root.right.right = TreeNode(4)

s = Solution()
print(s.pathSum(root, 8))
