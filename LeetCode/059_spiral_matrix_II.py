__author__ = 'liangl2'
class Solution:
    # @param {integer} n
    # @return {integer[][]}
    def generateMatrix(self, n):
        if n == 0:
            return []
        matrix = [[0]*n]*n
        row_begin, col_begin, row_end, col_end = 0, 0, n-1, n-1
        while row_begin <= row_end and col_begin <= col_end:
            # left to right
            for j in range(col_begin, col_end+1):
                matrix[row_begin][j] =
            row_begin += 1

            # top to bottom
            for j in range(row_begin, row_end+1):
                elements.append(matrix[j][col_end])
            col_end -= 1

            if row_begin <= row_end:
                # right to left
                for j in range(col_end, col_begin-1, -1):
                    elements.append(matrix[row_end][j])
                row_end -= 1
            if col_begin <= col_end:
                # bottom to top
                for j in range(row_end, row_begin-1, -1):
                    elements.append(matrix[j][col_begin])
                col_begin += 1

        return matrix