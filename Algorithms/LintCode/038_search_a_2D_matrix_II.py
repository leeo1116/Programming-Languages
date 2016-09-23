class Solution(object):
    def search_matrix(self, matrix, target):
        if not matrix or not matrix[0]:
            return 0
        row, col = 0, len(matrix[0])-1
        occurrence = 0
        while row < len(matrix) and col > -1:
            if matrix[row][col] == target:
                occurrence += 1
                col -= 1
            elif matrix[row][col] < target:
                row += 1
            else:
                col -= 1
        return occurrence

s = Solution()
print(s.search_matrix([[5]], 5))