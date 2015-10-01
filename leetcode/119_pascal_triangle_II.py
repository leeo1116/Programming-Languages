__author__ = 'liangl2'
class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        pre_row = [1]
        row = [1]
        for i in range(rowIndex+1):
            row = (i+1)*[1]
            if i > 1:
                for j in range(i):
                    if 0 < j < i:
                        row[j] = pre_row[j-1]+pre_row[j]
            pre_row = row
        return row
s = Solution()
print(s.getRow(2))