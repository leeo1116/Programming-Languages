__author__ = 'Liang Li'
class Solution:
    # @param {integer[][]} grid
    # @return {integer}
    def minPathSum(self, grid):
        row = len(grid)
        col = len(grid[0])

        for i in range(row):
            for j in range(col):
                if i == 0 and j == 0:
                    grid[i][j] = grid[i][j]
                elif i == 0 and j != 0:
                    grid[i][j] += grid[i][j-1]
                elif j == 0 and i != 0:
                    grid[i][j] += grid[i-1][j]
                else:
                    grid[i][j] += min(grid[i-1][j], grid[i][j-1])
        return grid[i][j]

s = Solution()
print(s.minPathSum([[1]]))