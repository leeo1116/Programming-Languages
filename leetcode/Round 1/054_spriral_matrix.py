__author__ = 'Liang Li'
class Solution:
    # @param {integer[][]} matrix
    # @return {integer[]}
    def spiralOrder(self, matrix):
        if len(matrix) == 0:
            return []
        elements = []
        row_begin, col_begin, row_end, col_end = 0, 0, len(matrix)-1, len(matrix[0])-1
        while row_begin <= row_end and col_begin <= col_end:
            # left to right
            for j in range(col_begin, col_end+1):
                elements.append(matrix[row_begin][j])
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

        return elements

s = Solution()
print(s.spiralOrder([[2,3]]))