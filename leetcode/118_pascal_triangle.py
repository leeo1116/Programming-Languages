__author__ = 'liangl2'
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        pre_row = [1]
        pascal = []
        for i in range(1, numRows+1):
            row = i*[1]
            if i > 2:
                for j in range(i):
                    if 0 < j < i-1:
                        row[j] = pre_row[j-1]+pre_row[j]
            pre_row = row
            pascal.append(row)
        return pascal

s = Solution()
print(s.generate(5))

