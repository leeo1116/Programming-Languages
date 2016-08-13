class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        nodes = preorder.split(',')
        diff = 1  # out_degree-in_degree
        for i, node in enumerate(nodes):
            diff -= 1
            if node != '#':
                diff += 2

            if i < len(nodes)-1 and diff < 1:  # diff < 0 for in-order, diff < -1 for post-order
                return False
        return diff == 0


s = Solution()
print(s.isValidSerialization("9,3,4,#,#,1,#,#,2,#,6,#,#"))