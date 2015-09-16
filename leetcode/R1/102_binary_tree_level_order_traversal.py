__author__ = 'Liang Li'
from collections import deque
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        node_queue = deque([root])
        result = []

        while node_queue:
            i = 0
            level_nodes = []
            node_queue_len = len(node_queue)
            while i < node_queue_len:
                level_nodes.append(node_queue[i].val)
                if node_queue[i].left:
                    node_queue.append(node_queue[i].left)
                if node_queue[i].right:
                    node_queue.append(node_queue[i].right)

                i += 1
            while node_queue_len:
                node_queue.popleft()
                node_queue_len -= 1
            result.append(level_nodes)
        return result

root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)
root.left.left = TreeNode(5)
root.right.left = TreeNode(4)
root.right.right = TreeNode(6)
root.right.right.right = TreeNode(7)

s = Solution()
print(s.levelOrder(root))