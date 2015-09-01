__author__ = 'Liang Li'
class Solution:
    # @param {integer[][]} matrix
    # @return {void} Do not return anything, modify matrix in-place instead.
    def setZeroes(self, matrix):
        row, col = [], []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    m, n = i, j
                    while m >= 0:

                    row.append(i)
                    col.append(j)

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i in row or j in col:
                    matrix[i][j] = 0

        return matrix

s = Solution()
print(s.setZeroes([[1, 2, 3], [2, 0, 5], [0, 3, 4]]))