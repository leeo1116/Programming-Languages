# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        inorder_len = len(inorder)
        postorder_len = len(postorder)
        if not inorder_len or not postorder or inorder_len != postorder_len:
            return None
        inorder_node_index_dict = {}
        for i, node in enumerate(inorder):
            inorder_node_index_dict[node] = i
        return self.build_tree_helper(inorder, 0, inorder_len-1, postorder, 0, postorder_len-1, inorder_node_index_dict)

    def build_tree_helper(self, inorder, i_start, i_stop, postorder, p_start, p_stop, inorder_node_index_dict):
        if i_start > i_stop or p_start > p_stop:
            return None
        root = TreeNode(postorder[p_stop])
        root_inorder_index = inorder_node_index_dict[root.val]
        root.left = self.build_tree_helper(inorder, i_start, root_inorder_index-1, postorder, p_start,
                                           p_start+root_inorder_index-1-i_start, inorder_node_index_dict)
        root.right = self.build_tree_helper(inorder, root_inorder_index + 1, i_stop, postorder,
                                            p_start+root_inorder_index-i_start, p_stop-1, inorder_node_index_dict)
        return root


s = Solution()
print(s.buildTree([1,3,2], [3,2,1]))

