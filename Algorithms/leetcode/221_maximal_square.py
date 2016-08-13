class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:
            return 0
        row = len(matrix)
        col = len(matrix[0])
        max_edge = 0

        # b[i][j] represent the edge length of the largest square ending at position (i, j)
        b = [[0 for _ in range(col + 1)] for _ in range(row + 1)]
        for i in range(1, row + 1):
            for j in range(1, col + 1):
                if matrix[i - 1][j - 1] == '1':
                    b[i][j] = min(b[i][j - 1], b[i - 1][j], b[i - 1][j - 1]) + 1
                    max_edge = max(max_edge, b[i][j])
        return max_edge * max_edge
