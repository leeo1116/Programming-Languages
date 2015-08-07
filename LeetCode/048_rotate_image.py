__author__ = 'liangl2'
class Solution:
    # @param {integer[][]} matrix
    # @return {void} Do not return anything, modify matrix in-place instead.
    def rotate(self, matrix):
        matrix[::-1]
        for row in range(len(matrix)):
            for col in range(row+1, len(matrix[row])):
                tmp = matrix[row][col]
                matrix[row][col] = matrix[col][row]
                matrix[col][row] = tmp

        return matrix

print(Solution().rotate([[1, 2], [3, 4]]))

