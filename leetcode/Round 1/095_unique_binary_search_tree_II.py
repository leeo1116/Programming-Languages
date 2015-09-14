__author__ = 'Liang Li'
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {integer} n
    # @return {TreeNode[]}
    def generateTrees(self, n):
        return self.generate(1, n)

    def generate(self, start, stop):
        if start > stop:
            return [None]
        if start == stop:
            return [TreeNode(start)]
        tree_nodes = []
        for i in range(start, stop+1):
            # divide-and-conquer
            left = self.generate(start, i-1)
            right = self.generate(i+1, stop)
            for l in left:
                for r in right:
                    tmp = TreeNode(i)
                    tmp.left = l
                    tmp.right = r
                    tree_nodes.append(tmp)
        return tree_nodes


