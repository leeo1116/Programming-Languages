# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        return self.build_tree_helper(preorder, 0, inorder, 0, len(inorder)-1)

    def build_tree_helper(self, preorder, p_start, inorder, i_start, i_end):
        if p_start > len(preorder)-1 or i_start > i_end:
            return None
        root = TreeNode(preorder[p_start])

        root_inorder_index = 0
        for i in range(i_start, i_end+1):
            if inorder[i] == root.val:
                root_inorder_index = i

        root.left = self.build_tree_helper(preorder, p_start+1, inorder, i_start, root_inorder_index-1)
        root.right = self.build_tree_helper(preorder, p_start+root_inorder_index-i_start+1, inorder, root_inorder_index+1, i_end)
        return root
