# Definition for a  binary tree node
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.root = root
        self.stack = self.preorder_traverse(self.root)

    def hasNext(self):
        """
        :rtype: bool
        """
        if len(self.stack) != 0:
            return True
        else:
            return False

    def next(self):
        """
        :rtype: int
        """
        return self.stack.pop()

    def preorder_traverse(self, root):
        s = []
        if not root:
            return s
        if root.right:
            s += self.preorder_traverse(root.right)
        s.append(root.val)
        if root.left:
            s += self.preorder_traverse(root.left)
        return s




        # Your BSTIterator will be called like this:
        # i, v = BSTIterator(root), []
        # while i.hasNext(): v.append(i.next())


t_root = TreeNode(4)
t_root.left = TreeNode(2)
t_root.right = TreeNode(7)
t_root.left.left = TreeNode(1)
t_root.left.right = TreeNode(3)
t_root.right.left = TreeNode(6)
t_root.right.right = TreeNode(9)

bstIterObj = BSTIterator(t_root)
print(bstIterObj.preorder_traverse(t_root))

# there is a amortized solution. the idea is to push all the left nodes to a stack, after next() operation, add right
# nodes to the stack. Looks like splitting the pre-order traversal into two functions./parts
